# Changelog — MinuteMasters (Transcript-to-Tasks)
All notable changes, engineering iterations, and milestone achievements are documented in this file.

## [Milestone 2] - 2026-11-22
### Added
- **Two-Stage Decoupled Prompt Pipeline:**
  - Implemented `P1_EXTRACTION` (Grounded Candidate Extractor) with strict RFC 8259 JSON schema and verbatim citation requirements.
  - Implemented `P2_VERIFICATION` (Adversarial Verification Engine) for zero-hallucination fact checking against source text.
- **Evaluation Harness & Benchmark:**
  - Curated 12 full-text meeting transcripts in `test-data/inputs/` (T01 through T12).
  - Built comprehensive ground-truth answer keys and verified model outputs in `test-data/outputs/`.
  - Added honest edge-case failure analyses for Code-Switching (T11) and Non-Meeting Text Rejection (T12).
- **Interactive Prototype Application:**
  - Built interactive Streamlit application (`code/app.py`) featuring model selection, test case loading, pipeline visualization, and CSV/JSON export.
  - Developed pure Python orchestrator (`code/transcript_pipeline.py`).
  - Created executable Jupyter/Colab notebook (`code/TranscriptToTasks_Prototype.ipynb`) with outputs pre-saved.
- **Architectural Documentation & Diagrams:**
  - Created 4 detailed Mermaid flowcharts: Prompt Workflow, Task Decomposition, Input-Output Flow, and System Architecture.
  - Authored Business Model Canvas (BMC) covering all 9 strategic blocks.
  - Created second-by-second video reel script (118 seconds) and storyboard in `docs/REEL_SCRIPT.md`.
  - Created copy-pasteable Q1-Q24 Microsoft Form submission guide.

### Changed
- **Sampling Temperature Calibration:** Reduced temperature from default (1.0) to 0.2 on P1 and 0.1 on P2 to enforce deterministic schema compliance.
- **Fallback Rule Refinement:** Replaced model guesswork on absent owners/deadlines with explicit `"not stated"` tagging, directly addressing feedback from senior Ojas Vats.
- **Format Hardening:** Replaced conversational markdown bullet points with parseable JSON structures backed by verbatim quote anchors.

---

## [Iteration 2.2] - 2026-11-19
### Added
- Senior mentor consultation with Ojas Vats (past club president). Integrated feedback:
  - Added test cases for overlapping speech and interrupted proposals.
  - Formalized policy of marking missing owners as `"not stated"` rather than assigning to the speaker.
- Created `test-data/inputs/T07_mess_committee_edge.txt` and `test-data/inputs/T08_sports_meet_changed_decision.txt`.

### Changed
- Refactored `v2` prompt into two separate prompt sheets (`P1` and `P2`).
- Achieved 100% JSON schema validity across 10 test runs on Gemini 2.5 Flash and Claude 3.5 Sonnet.

---

## [Iteration 2.1] - 2026-11-15
### Added
- Prompt Version 2 (`v2_fewshot_json.md`): Introduced JSON schema and 1 few-shot in-context example.
- Initial benchmark on 5 sample transcripts.

### Fixed
- Fixed inconsistent output formatting from Milestone 1 baseline; established structured JSON output.

### Discovered Limitations
- JSON broke in 3 out of 10 runs due to conversational preamble.
- Model still hallucinated owners on unassigned tasks (e.g., assigning tasks to the person who asked the question).

---

## [Milestone 1] - 2026-11-10
### Added
- Initial project registration under Problem C-12: *Transcript-to-Tasks*.
- Team formation: 6 members led by Parth Sharma.
- Defined core problem context based on Jabra 2026 workplace meeting statistics (58% wasted time, 91% unclear action items).
- Baseline prompt v1 (`v1_baseline.md`) drafted and tested on synthetic club orientation transcript.
