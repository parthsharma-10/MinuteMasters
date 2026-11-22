# MinuteMasters — Transcript-to-Tasks

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://minutemasters.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> **A Grounded Prompt Workflow for Extracting Verified Decisions and Action Items from Messy Spoken Meeting Transcripts**  
> *SCSE4041 Mini Project — Milestone 2 Submission | Bennett University*

---

## 📌 Project Overview
In student clubs, research groups, and engineering startups, critical decisions get buried in long, unstructured spoken conversations. Meeting minutes are recorded late, partially, or not at all, leaving owners and deadlines ambiguous.

According to **Jabra's 2026 Global Workplace Report**:
- **58%** of meeting time is considered unproductive.
- **59%** of meetings require a subsequent follow-up meeting.
- **91%** of meeting attendees leave with unclear or ambiguous action items.
*(Source: [Jabra Thought Leadership 2026](https://www.jabra.com/thought-leadership/billion-dollar-brain-drain))*

**Transcript-to-Tasks** introduces a two-stage prompt engineering workflow that converts raw transcripts into structured, verified RFC 8259 JSON and human-auditable action tables. Every extracted task is tied to a **verbatim transcript quote**, and unassigned attributes are deterministically marked as `"not stated"`, completely eliminating AI owner hallucinations.

---

## 👥 MinuteMasters Team Roster

| Member Full Name | Enrollment No. | Official Email ID | Milestone 2 Ownership |
|---|---|---|---|
| **Parth Sharma** (Team Leader) | **S24CSEU1941** | s24cseu1941@bennett.edu.in | Pipeline Architect & Report Lead |
| **Kabir Bakshi** | **S24CSEU1938** | S24CSEU1938@bennett.edu.in | Extraction Prompt Engineer (P1) |
| **Konark Kalra** | **S24CSEU1955** | S24CSEU1955@bennett.edu.in | Verification Engineer (P2) |
| **Harsh Vardhan** | **S24CSEU1935** | S24CSEU1935@bennett.edu.in | Benchmark & Dataset Lead |
| **Harsh Gangwar** | **S24CSEU1961** | S24CSEU1961@bennett.edu.in | Evaluation & Error Analysis Lead |
| **Chakshu** | **S24CSEU2693** | S24CSEU2693@bennett.edu.in | Full-Stack UI & Prototype Developer |

---

## 🔗 Key Submission Links
- **Prototype Link (Q11):** [MinuteMasters Streamlit Prototype](https://minutemasters.streamlit.app) *(or open `code/TranscriptToTasks_Prototype.ipynb` in Google Colab)*
- **Repository Link (Q12):** [MinuteMasters GitHub Repository](https://github.com/ParthSharma-BU/MinuteMasters-TranscriptToTasks)
- **Video Reel Link (Q13):** [YouTube Unlisted Demo](https://youtu.be/MinuteMasters_M2_Demo) *(Exact length: **118 seconds**)*
- **Milestone 2 PDF:** [`docs/M2_C12_TranscriptToTasks.pdf`](docs/M2_C12_TranscriptToTasks.pdf)
- **Supporting Document (BMC):** [`docs/MinuteMasters_BMC.pdf`](docs/MinuteMasters_BMC.pdf)

---

## 🏗️ Architecture & Two-Stage Pipeline

```
Raw Transcript ──► [Prompt P1: Candidate Extractor] ──► Candidate JSON
                         (Temp=0.2, Grounding)              │
                                                            ▼
Raw Transcript ────────────────────────────────────► [Prompt P2: Verification Auditor]
                                                            │ (Temp=0.1, Adversarial)
                                                            ▼
                                                   Verified JSON & Markdown Table
```

1. **Stage 1 (Prompt P1 — Extraction):** Ingests raw conversation and extracts candidate decisions and action items with verbatim quotes. Applies fallback: missing owners/deadlines &rarr; `"not stated"`.
2. **Stage 2 (Prompt P2 — Adversarial Verification):** Cross-checks candidate JSON against the source transcript. Discards fabricated items, verifies speaker consent, checks deadline realism, and generates the final auditable action checklist.

---

## 📊 Milestone 2 Official Audit Counts

| Metric | Required / Allowed | MinuteMasters Actual | Exact Match in PDF |
|---|---|---|---|
| **Number of Final Prompts (Q10)** | 1 – 50 | **2** (`P1_EXTRACTION` & `P2_VERIFICATION`) | Section 2(c) |
| **Number of Test Inputs (Q17)** | Minimum 10 | **12** (6 Normal, 4 Edge, 2 Invalid) | Section 4.1 |
| **Number of Prompt Versions (Q18)**| Minimum 3 | **3** (v1 Baseline, v2 JSON, v3 Production) | Section 3.3 |
| **Reel Duration (Q14)** | 90 – 150 seconds | **118 seconds** | `docs/REEL_SCRIPT.md` |
| **Prototype Working Modules (Q20)**| All Claimed Working | **4 Working Modules** | Section 3.2 |

---

## 📁 Repository Directory Layout

```text
MinuteMasters-TranscriptToTasks/
├── README.md                           # Project guide & team overview
├── CHANGELOG.md                        # Dated history from M1 to M2
├── requirements.txt                    # Python dependencies
├── prompts/
│   ├── v1/v1_baseline.md              # Milestone 1 Baseline prompt
│   ├── v2/v2_fewshot_json.md          # Milestone 2 Intermediate JSON prompt
│   ├── v3/v3_verified_constraints.md  # Grounded constraint engineering notes
│   └── final/
│       ├── P1_extraction_prompt.md     # Production Extraction Prompt Sheet
│       └── P2_verification_prompt.md   # Production Verification Prompt Sheet
├── code/
│   ├── app.py                          # Interactive Streamlit Web App
│   ├── transcript_pipeline.py          # Pure Python pipeline orchestrator
│   └── TranscriptToTasks_Prototype.ipynb # Jupyter notebook with executed outputs
├── test-data/
│   ├── test_dataset.json               # 12-test evaluation matrix
│   ├── inputs/                         # 12 synthetic transcripts (T01 - T12)
│   └── outputs/                        # 12 verified outputs (T01 - T12)
└── docs/
    ├── M2_C12_TranscriptToTasks.pdf    # Master Milestone 2 PDF
    ├── M2_C12_TranscriptToTasks.html   # Print-ready HTML version
    ├── MinuteMasters_BMC.pdf           # Supporting Business Model Canvas PDF
    ├── MinuteMasters_BMC.html          # Print-ready BMC HTML version
    ├── REEL_SCRIPT.md                  # 118-second video storyboard
    ├── FORM_SUBMISSION_ANSWERS.md      # Copy-pasteable Q1-Q24 Form Guide
    └── diagrams/                       # Mermaid diagrams (Workflow, Architecture, etc.)
```

---

## 🚀 Quickstart: Running the Prototype Locally

### 1. Clone the Repository
```bash
git clone https://github.com/ParthSharma-BU/MinuteMasters-TranscriptToTasks.git
cd MinuteMasters-TranscriptToTasks
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit Web App
```bash
streamlit run code/app.py
```
Open your browser at `http://localhost:8501`. You can test preloaded sample cases or paste your own meeting transcript!

---

## 🔒 Security & Privacy
- **Zero API Keys in Repository:** No hardcoded credentials exist anywhere in the code.
- **Privacy-Safe Data:** All 12 evaluation transcripts are entirely fictional; no real personal data is stored.
