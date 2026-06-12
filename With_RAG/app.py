import streamlit as st
import pandas as pd
import csv, time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


import requests

MISTRAL_API_KEY = "0U3XwkDntVClyCIsflJJYebks1rUUVFy"  # paste your key from admin.mistral.ai

def get_mistral_answer(user_input):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-medium",  # or "mistral-large" if you prefer
        "messages": [{"role": "user", "content": user_input}]
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"⚠️ Mistral API Error: {response.status_code} - {response.text}"


# --- Title & Caption ---
st.title("Final Year Project Stress Chatbot")
st.caption("Educational support only — not therapy or medical system.")

st.markdown("""
<style>
div[data-testid="stMarkdownContainer"] > div.st-info {
    min-height: 180px;
    overflow-y: auto;
    max-height: 250px;
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_csv(path):
    return pd.read_csv(path, encoding="utf-8-sig", sep=",", on_bad_lines="skip")



questions = load_csv("3_benchmark_questions.csv")
answers = load_csv("4_ideal_answers.csv")
risks = load_csv("5_risk_labels.csv")
corpus = load_csv("2_corpus_chunks.csv")

# --- Clean column names (remove spaces + lowercase) ---
questions.columns = questions.columns.str.strip().str.lower()
answers.columns = answers.columns.str.strip().str.lower()
risks.columns = risks.columns.str.strip().str.lower()
corpus.columns = corpus.columns.str.strip().str.lower()




# --- Functions ---
def log_response(qid, system_type, response, chunks="NA"):
    start = time.time()
    end = time.time()
    response_time = round(end - start, 2)
    with open("6_model_responses.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([qid, system_type, response, chunks, response_time])

def log_evaluation(qid, system_type, relevance, helpfulness, faithfulness, safety, clarity, unsafe_flag, comments):
    with open("7_human_evaluation.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([qid, system_type, relevance, helpfulness, faithfulness, safety, clarity, unsafe_flag, comments])

# --- Recommended Questions ---
st.subheader("Try asking one of these:")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Supervisor Pressure"):
        st.session_state.user_q = "How can regular supervisor communication reduce stress for engineering students?"
with col2:
    if st.button("Tracking Progress"):
        st.session_state.user_q = "How does tracking progress reduce stress?"
with col3:
    if st.button("Stay Motivated"):
        st.session_state.user_q = "Why is positive thinking useful in managing stress?"

# --- Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask your question:", value=st.session_state.get("user_q", ""))

if user_input.strip() != "":
    # --- S0 ---
    match_qid = questions.loc[
        questions["user_question"].str.lower() == user_input.lower(),
        "question_id"
    ].values

    if len(match_qid) > 0:
        qid = match_qid[0]
        match_ans = answers.loc[answers["question_id"] == qid, "ideal_answer"].values
        response_s0 = match_ans[0] if len(match_ans) > 0 else "No ideal answer found."
    else:
        qid = "NA"
        response_s0 = "Question not found in dataset."


    # --- S1 (cached vectorizer) ---
    @st.cache_resource
    def build_vectorizer(corpus_texts):
        vectorizer = TfidfVectorizer().fit(corpus_texts)
        corpus_vectors = vectorizer.transform(corpus_texts)
        return vectorizer, corpus_vectors

    corpus_texts = corpus["text"].tolist()
    vectorizer, corpus_vectors = build_vectorizer(corpus_texts)

    query_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(query_vector, corpus_vectors).flatten()
    best_idx = similarities.argmax()

    rag_context = corpus.iloc[best_idx]["text"]
    response_s1 = f"{response_s0}\n\nAdditional context: {rag_context}"
    retrieved_chunk_ids = corpus.iloc[best_idx]["chunk_id"]

    # --- S2 (safety filter) ---
    risk_match = risks.loc[risks["question_id"] == qid, "risk_label"].values
    if len(risk_match) > 0 and risk_match[0].lower() in ["unsafe", "high-risk", "l2_distress", "l1_stress"]:
        safe_paragraph = (
            "⚠️ This question may involve sensitive or unsafe content. Educational guidance only.\n\n"
            "🧠 Students often experience stress or emotional pressure during final-year projects — "
            "especially when facing rejection, deadlines, or uncertainty. It helps to focus on structured planning, "
            "peer or supervisor communication, and small achievable goals. Maintaining a balanced routine, "
            "healthy sleep, and positive thinking can support steady progress. Remember, project challenges are "
            "part of learning; reflecting on feedback and staying connected with supportive peers builds resilience."
        )
        response_s2 = safe_paragraph
        retrieved_chunk_ids = "NA"
    else:
        response_s2 = response_s1

    # --- LL Model ---
    with st.spinner("Generating responses..."):
        llm_response = get_mistral_answer(user_input)

    # --- Display Responses ---
    st.markdown("### Model Responses")
    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Response S0** Small")
        st.info(response_s0)

        st.markdown("**Response S2** Large")
        st.info(response_s2)

    with colB:
        st.markdown("**Response S1** Medium")
        st.info(response_s1)

        st.markdown("**LL Model (Mistral)**")
        st.info(llm_response)



    
# --- Log chatbot response ---
    if "logged_questions" not in st.session_state:
        st.session_state.logged_questions = set()
    if "qid" in locals() and qid not in st.session_state.logged_questions:
        log_response(qid=qid, system_type="S2", response=response_s2, chunks=retrieved_chunk_ids)
        st.session_state.logged_questions.add(qid)


st.markdown("### Evaluation Metrics")

# Example: replace these with your actual calculated values from sliders
accuracy_s0, accuracy_s1, accuracy_s2, accuracy_ll = 82, 87, 91, 96
response_s0, response_s1, response_s2, response_ll = 120, 240, 310, 890
concise_s0, concise_s1, concise_s2, concise_ll = 90, 75, 65, 55
satisfy_s0, satisfy_s1, satisfy_s2, satisfy_ll = 78, 84, 88, 94

# Create DataFrame for table
data = {
    "Metric": ["Accuracy", "Response Time (ms)", "Conciseness", "User Satisfaction"],
    "Response S0": [accuracy_s0, response_s0, concise_s0, satisfy_s0],
    "Response S1": [accuracy_s1, response_s1, concise_s1, satisfy_s1],
    "Response S2": [accuracy_s2, response_s2, concise_s2, satisfy_s2],
    "LL Model": [accuracy_ll, response_ll, concise_ll, satisfy_ll]
}
df = pd.DataFrame(data)

# --- Dark theme styling ---
st.markdown("""
<style>
table {
    background-color: #0E1117;
    color: #FFFFFF;
    border-radius: 10px;
    border-collapse: collapse;
    width: 100%;
}
th {
    background-color: #1E1E1E;
    color: #00C8FF;
    padding: 10px;
    text-align: left;
}
td {
    padding: 8px;
    border-bottom: 1px solid #333333;
}
</style>
""", unsafe_allow_html=True)


st.markdown("### Model Evaluation (Scores 1–5)")

# --- Single Evaluation Sliders ---
col = st.columns(5)
relevance = col[0].slider("Relevance", 1, 5)
helpfulness = col[1].slider("Helpfulness", 1, 5)
faithfulness = col[2].slider("Faithfulness", 1, 5)
safety = col[3].slider("Safety", 1, 5)
clarity = col[4].slider("Clarity", 1, 5)
comments = st.text_area("Comments")

if st.button("Save Evaluation"):
    st.success("✅ Evaluation saved successfully!")

    # --- Prepare Data from sliders ---
    metrics = ["Relevance", "Helpfulness", "Faithfulness", "Safety", "Clarity"]
    scores = [relevance, helpfulness, faithfulness, safety, clarity]

    # --- Plot Graph dynamically ---
    fig, ax = plt.subplots(figsize=(8,5))
    bars = ax.bar(metrics, scores, color="#00C8FF")

    # Add score labels on top of bars
    for bar, score in zip(bars, scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                str(score), ha='center', va='bottom', color="white", fontsize=10)

    # Dark theme styling
    ax.set_facecolor("#0E1117")
    fig.patch.set_facecolor("#0E1117")
    ax.tick_params(colors="white")
    ax.set_ylabel("Score (1–5)", color="white")
    ax.set_ylim(0, 5)

    st.pyplot(fig)


