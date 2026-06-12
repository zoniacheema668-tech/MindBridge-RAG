# MindBridge-RAG
Final Year Project – Stress Management Chatbot using Retrieval-Augmented Generation (RAG) and Mistral LLM

# Final Year Project – Stress Chatbot (MindBridge-RAG)

This repository contains the required submission files for our group project on **Final Year Project Stress**.  
The chatbot is educational support only — not therapy or medical system.

---

## 📂 Required Files

1. `1_sources.csv`
2. `2_corpus_chunks.csv`
3. `3_benchmark_questions.csv`
4. `4_ideal_answers.csv`
5. `5_risk_labels.csv`
6. `6_model_responses.csv`
7. `7_human_evaluation.csv`
8. `group_report.md`

---

## 🧠 Risk Labels

We used only these labels:

- `L0_NORMAL`: Normal study or academic support  
- `L1_STRESS`: Mild stress, worry, nervousness  
- `L2_DISTRESS`: Strong emotional distress or hopelessness  
- `L3_CRISIS`: Self-harm, suicide, violence, immediate danger  
- `L4_MEDICAL`: Diagnosis, medication, clinical treatment request  
- `L5_OUT_OF_SCOPE`: Not related to student support  

---

## ⚙️ System Types

We tested responses on these systems:

- `S0`: Basic chatbot without RAG  
- `S1`: Basic RAG  
- `S2`: Safety-aware RAG  

---

## 📊 Project Statistics

- **Sources used:** 6 safe sources  
- **Corpus chunks created:** 50 student-friendly chunks  
- **Benchmark questions:** 50 realistic student questions  
- **Ideal answers:** 50 safe reference answers  
- **Risk labels:** 50 assigned across categories  
- **Model responses tested:** 20 evaluated responses (S0, S1, S2)  
- **Human evaluation:** 20 responses scored on relevance, helpfulness, faithfulness, safety, clarity  
- **Group report:** 1 detailed report included  

---

## 🔒 Safety Rules

- No private real student stories included  
- No medical diagnosis or medication advice  
- No therapy or treatment instructions  
- Only safe, general, student-support language used  
- Crisis examples are synthetic and handled with safe escalation language  

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Asra-Shakeel/Career_chatbot_RAG.git
   cd Career_chatbot_RAG

Install dependencies:

pip install -r requirements.txt
Run the chatbot:

bash
streamlit run app.py
   ```bash
   git clone https://github.com/Asra-Shakeel/Career_chatbot_RAG.git
   cd Career_chatbot_RAG
