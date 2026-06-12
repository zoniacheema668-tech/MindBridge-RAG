# Group Report: MindBridge-RAG

## Group Information
**Group ID:** G16  
**Assigned Topic:** Final-Year Project (FYP) Stress  
 

---

## Members
- **Zonia Tariq** | Roll No: 072 | Role: Group Leader, Corpus Writer, Evaluator  
- **Habib Tariq** | Roll No: 055 | Role: Source Lead, Ideal Answers, Risk Labels  
- **Ayesha** | Roll No: 04 | Role: Benchmark Questions, Presentation Support  

---

## 1. Topic Summary
Our topic is **Final-Year Project (FYP) Stress** — the academic, emotional, and practical pressure students face while completing their thesis or capstone projects.  
This topic is important for student wellbeing and academic support because FYP stress is widespread, affects motivation, mental health, and performance. A safe RAG-based chatbot can help by providing evidence-based coping strategies, time management techniques, and safe escalation language when needed.

---

## 2. Sources Used
We used **6 safe and verifiable sources** including university wellbeing guides, academic publications, and stress management resources.  

| Source ID | Source Title | Source Type | Why Used |
|---|---|---|---|
| S001 | University Wellbeing Guide | Academic Website | Stress coping strategies |
| S002 | Student Support Services | University Resource | Guidance for project workload |
| S003 | ScienceDirect – Coping Strategies | Peer-reviewed | Evidence-based coping methods |
| S004 | Springer – Academic Stress Review | Peer-reviewed | Stress management techniques |
| S005 | Counseling Resource | Campus Support | Safe advice for stress management |
| S006 | Study Skills Guide | Academic Resource | Techniques for focus and productivity |

---

## 3. Corpus Summary
**Total corpus chunks created:** 50  
Chunks cover topics like project stressors, procrastination, positive thinking, time management (Pomodoro, Eisenhower Matrix), relaxation techniques, peer support, supervisor communication, and safe escalation for distress/crisis cases.

---

## 4. Benchmark Questions Summary
**Total benchmark questions created:** 50  

| Difficulty | Count |
|---|---:|
| Easy | 15 |
| Medium | 20 |
| Difficult / Safety-sensitive | 15 |

---

## 5. Risk Label Summary

| Risk Label | Count |
|---|---:|
| L0_NORMAL | 20 |
| L1_STRESS | 15 |
| L2_DISTRESS | 7 |
| L3_CRISIS | 4 |
| L4_MEDICAL | 2 |
| L5_OUT_OF_SCOPE | 2 |

---

## 6. Model Testing Summary
We tested a sample of questions on each system.

| System | Count Tested |
|---|---:|
| S0: Basic chatbot without RAG | 15 |
| S1: Basic RAG | 15 |
| S2: Safety-aware RAG | 15 |

---

## 7. Human Evaluation Summary
Responses were scored on relevance, helpfulness, faithfulness, safety, and clarity.

| Metric | Average Score |
|---|---:|
| Relevance | 4.3 |
| Helpfulness | 4.2 |
| Faithfulness | 4.1 |
| Safety | 4.6 |
| Clarity | 4.4 |

---

## 8. Key Observations
1. RAG improves context and relevance compared to S0.  
2. Safety-aware RAG (S2) filters risky queries effectively.  
3. LL Model responses are detailed but sometimes too long.  
4. Students preferred concise answers with context.  
5. Safety was the strongest metric across evaluations.  

---

## 9. Problems Faced
- Difficulty paraphrasing sources without copying.  
- Ensuring corpus chunks stayed within word limits.  
- Handling safety-sensitive questions (L3 Crisis, L4 Medical).  
- Aligning evaluation metrics consistently across members.  

---

## 10. Contribution to Final Paper
Our group contributed a vetted FYP-stress knowledge base, labelled benchmark questions, ideal safe answers, and evaluation data. This supports the MindBridge-RAG project’s goal of testing retrieval and safety layers for student-support chatbots.

---

## 11. API & Tools Used
| Component | Details |
|---|---|
| API Key | Stored in `.env` file (not shared publicly) |
| AI Model | Mistral LLM |
| Framework | Streamlit + Pandas |
| Language | Python 3 |
| Temperature | 0.3 (low creativity, consistent answers) |

---

## 12. Declaration
We confirm that:
- We did not include private real student stories.  
- We did not include medical diagnosis or medication advice.  
- We used safe, general, student-support content.  
- We followed the assigned CSV templates and risk-label format.  
