# Group Report: MindBridge-RAG

**Assigned Topic:** Final Year Project Stress  
 

## 1. Topic Summary
Our assigned topic is **Final Year Project Stress**.  
This topic is highly relevant to student wellbeing because final-year projects often cause anxiety, workload pressure, and stress. The chatbot provides educational support, stress management strategies, and safe guidance without offering medical or therapeutic advice.

---

## 2. Sources Used
We used **6 safe sources** including university wellbeing pages, academic support sites, and stress management guides. These sources were paraphrased into corpus chunks.

| Source ID | Source Title | Source Type | Why Used |
|---|---|---|---|
| S001 | University Wellbeing Page | Academic Website | Provides stress coping strategies |
| S002 | Student Support Services | Academic Website | Guidance for project workload |
| S003 | Academic Skills Page | University Resource | Tips for planning and scheduling |
| S004 | Counseling Resource | Campus Support | Safe advice for stress management |
| S005 | Study Skills Guide | Academic Resource | Techniques for focus and productivity |

---

## 3. Corpus Summary
**Total corpus chunks created:** 50  
We created short, paraphrased text chunks (80–150 words each) focusing on project stress, time management, positive thinking, and safe coping strategies.

---

## 4. Benchmark Questions Summary
**Total benchmark questions created:** 40  

| Difficulty | Count |
|---|---:|
| Easy | 10 |
| Medium | 15 |
| Difficult / Safety-sensitive | 15 |

---

## 5. Risk Label Summary

| Risk Label | Count |
|---|---:|
| L0_NORMAL | 10 |
| L1_STRESS | 10 |
| L2_DISTRESS | 8 |
| L3_CRISIS | 5 |
| L4_MEDICAL | 4 |
| L5_OUT_OF_SCOPE | 3 |

---

## 6. Model Testing Summary

| System | Count Tested 
|-----   |
| S0:Basic chatbot without RAG | 15 |
| S1:Basic RAG | 15 |
| S2:Safety-aware RAG | 15 |

---

## 7. Human Evaluation Summary
We evaluated responses on relevance, helpfulness, faithfulness, safety, and clarity.

| Metric | Average Score |
|---|---:|
| Relevance | 4.2 |
| Helpfulness | 4.0 |
| Faithfulness | 4.1 |
| Safety | 4.5 |
| Clarity | 4.3 |

---

## 8. Key Observations
1. RAG improves context and relevance compared to S0.  
2. Safety-aware RAG (S2) successfully filters risky queries.  
3. LL Model responses are detailed but sometimes over‑explain.  
4. Students preferred concise answers with additional context.  
5. Human evaluation confirmed safety as the strongest metric.

---

## 9. Problems Faced
- Difficulty in paraphrasing sources without copying.  
- Ensuring corpus chunks stayed within word limits.  
- Handling safety‑sensitive questions (L3 Crisis, L4 Medical).  
- Aligning evaluation metrics consistently across members.

---

## 10. Contribution to Final Paper
Our group contributed by preparing safe sources, corpus chunks, benchmark questions, ideal answers, risk labels, and evaluation data. This ensures the final MindBridge-RAG paper has a complete dataset and analysis for stress management support.

---

## 11. Declaration
We confirm that:
- We did not include private real student stories.  
- We did not include medical diagnosis or medication advice.  
- We used safe, general, student-support content.  
- We followed the assigned CSV templates and risk-label format.
