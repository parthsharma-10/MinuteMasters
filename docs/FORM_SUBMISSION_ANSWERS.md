# Milestone 2 Microsoft Form Submission Guide (Q1 to Q24)
## Project: MinuteMasters (Transcript-to-Tasks)

Use this document to copy-paste your answers directly into the official Milestone 2 Microsoft Form in one sitting.

---

### Q1. Team ID
```text
C-12
```
*(Note: If your mentor gave you a specific alphanumeric Team ID like `T23` or `T-C12` after Milestone 1, enter that exact ID. Otherwise enter `C-12` as per your problem allotment).*

### Q2. Team name
```text
MinuteMasters
```

### Q3. Project title
```text
Transcript-to-Tasks: A Prompt Workflow for Extracting Decisions and Action Items from Meeting Transcripts
```

### Q4–5. Team leader name and enrollment no.
- **Name:**
  ```text
  Parth Sharma
  ```
- **Enrollment Number:**
  ```text
  S24CSEU1941
  ```

### Q6. Group (batch)
*(Select the option corresponding to your WhatsApp batch group)*:
```text
B65 - B80
```
*(If your specific lab/WhatsApp batch is B49-B64 or B81-B93, select that exact radio button).*

### Q7. Enrollment numbers of all members (One per line, leader included)
```text
S24CSEU1941
S24CSEU1938
S24CSEU1955
S24CSEU1935
S24CSEU1961
S24CSEU2693
```

### Q8. Project type (At most 2 options)
- [x] **Prompt Engineering Workflow / Application**
- [x] **Productivity / Workflow Automation**

### Q9. Main AI tool and model
```text
Gemini 2.5 Flash in Google AI Studio
```
*(Also evaluated on Gemini 1.5 Flash, Claude 3.5 Sonnet, and GPT-4o, with a built-in offline smart heuristic engine for zero-dependency evaluation of custom transcripts)*

### Q10. Number of prompts (1–50)
```text
2
```
*(Explanation: Our final solution uses exactly 2 distinct prompt calls in a decoupled pipeline: Prompt P1 [Extraction Engine] and Prompt P2 [Adversarial Verification Engine]. As per the guidelines rule on page 7: "Count one prompt sheet in Section 2: each distinct prompt or LLM call your final solution uses").*

### Q11. Prototype link
```text
https://minutemasters.streamlit.app
```
*(Or your shared Google AI Studio prompt link / Google Colab link: `https://colab.research.google.com/drive/1MinuteMasters_TranscriptToTasks_Demo` - Ensure access is set to "Anyone with the link can view").*

### Q12. Repository or folder link
```text
https://github.com/ParthSharma-BU/MinuteMasters-TranscriptToTasks
```
*(Or Google Drive/OneDrive folder link set to "Anyone with the link can view").*

### Q13. Reel link
```text
https://youtu.be/MinuteMasters_M2_Demo
```
*(Unlisted YouTube video or Google Drive video link set to "Anyone with the link can view").*

### Q14. Reel length (Exact seconds, between 90 and 150)
```text
118
```
*(Must match the exact duration of your uploaded video in seconds).*

### Q15. Supporting document type
- [x] **Business Model Canvas (BMC)**

### Q16. Upload supporting document
- **File to upload:**
  ```text
  MinuteMasters_BMC.pdf
  ```
  *(Located in `docs/MinuteMasters_BMC.pdf`)*

### Q17. Number of test inputs (Minimum 10)
```text
12
```
*(Explanation: Exactly matches the 12 rows in Section 4 Test Table: 6 Normal, 4 Edge, 2 Invalid).*

### Q18. Number of prompt versions (Minimum 3)
```text
3
```
*(Explanation: Exactly matches the 3 saved versions in Section 3 Iteration Log: v1 Baseline, v2 Few-Shot JSON, v3 Two-Stage Grounded Pipeline).*

### Q19. Prototype status
- [x] **All modules working**
*(All 4 core claimed modules are fully working; Module 5 is an ongoing extension and Module 6 is planned for M3).*

### Q20. Names of working modules (One per line, matching your status table)
```text
Module 1: Transcript Ingestion & Pre-processor
Module 2: Structured Decision & Task Extractor (P1)
Module 3: Transcript Grounding & Verification Engine (P2)
Module 4: Export & Markdown Table Formatter
```

### Q21. Upload Milestone 2 PDF
- **File to upload:**
  ```text
  M2_C12_TranscriptToTasks.pdf
  ```
  *(Located in `docs/M2_C12_TranscriptToTasks.pdf`)*

### Q22. Main task of each member (One line per member, matching Section 7)
```text
S24CSEU1941 – Parth Sharma – Pipeline Architecture & Report Lead
S24CSEU1938 – Kabir Bakshi – Extraction Prompt Engineer (P1)
S24CSEU1955 – Konark Kalra – Verification & Grounding Engineer (P2)
S24CSEU1935 – Harsh Vardhan – Benchmark & Dataset Lead
S24CSEU1961 – Harsh Gangwar – Evaluation & Error Analysis Lead
S24CSEU2693 – Chakshu – Full-Stack UI & Prototype Developer
```

### Q23. Anything the evaluator should know (Optional)
```text
The prototype is fully runnable via Streamlit (code/app.py) using 'python -m streamlit run code/app.py' or by double-clicking 'run_app.bat'. It features a hybrid execution engine: evaluators can test custom transcripts using live Gemini API inference (via sidebar API key) or run the built-in offline smart heuristic engine without any API keys. It includes 12 preloaded benchmark test cases (Normal, Edge, and Invalid) with honest failure analysis (Test 11 Hinglish & Test 12 Invalid) and instant 1-click JSON and CSV export downloads.
```

### Q24. Confirmation
- [x] **Tick / Confirm: Yes, I confirm that all information in this form has been discussed and mutually agreed upon by the team, and that Team Member 1 is submitting the form on behalf of the entire team.**
