# Prompt Version 3 (Grounded Extraction & Constraint Engineering)

## Metadata
- **Version**: 3.0 (Milestone 2 Production Pipeline Architecture)
- **Author**: Harsh Gangwar, Chakshu & Parth Sharma
- **Date**: 19 November 2026
- **Tool / Model**: Gemini 2.5 Flash / GPT-4o / Claude 3.5 Sonnet
- **Settings**: Temperature = 0.2, Top-P = 0.95
- **Workflow Step**: Two-Prompt Decoupled Pipeline (P1: Grounded Extraction, P2: Cross-Verification)

---

## Architectural Shift in v3
Instead of attempting single-turn extraction and validation simultaneously, v3 splits the problem into two distinct, specialized prompts:
1. **Prompt P1 (Candidate Extraction)**: Focuses on exhaustive recall, extracting every decision and action candidate along with an exact verbatim quote (`evidence_quote`). Uses explicit fallback values: `"not stated"` for missing owners or deadlines.
2. **Prompt P2 (Adversarial Verification)**: Operates as an independent auditor. It receives the original transcript and P1's candidate JSON, verifies that every `evidence_quote` exists verbatim, validates whether the owner explicitly committed or consented, checks if deadlines are real or hallucinated, prunes rejected/superseded proposals, and produces the finalized verified JSON and markdown summary table.

---

## System Prompt (P1 Extraction)
```text
You are MinuteMasters Core Extraction Engine, an analytical AI specialized in mining meeting minutes from raw spoken transcripts. You strictly ground all findings in verbatim textual evidence. You never infer, guess, or fabricate owners, deadlines, or decisions. If an attribute is absent from the transcript, you must record it as "not stated".
```

## System Prompt (P2 Verification)
```text
You are MinuteMasters Quality & Verification Auditor. Your objective is zero-hallucination verification. You cross-examine candidate meeting minutes against the raw transcript. You reject any action item or decision that lacks direct transcript consensus or contains unconfirmed assumptions.
```

---

## What Changed Since v2 and Why
1. **Decoupled Architecture**: Separating extraction from verification prevents the LLM from confirming its own confirmation biases.
2. **Strict Fallback Semantics**: Replaced guesswork with mandatory `"not stated"` labels, directly implementing feedback from senior Ojas Vats.
3. **Mandatory Verbatim Evidence Quotes**: Every task and decision must cite the exact transcript utterance.
4. **Low Temperature (0.2)**: Reduced sampling temperature from 0.5 to 0.2 to maximize deterministic compliance with the JSON schema.
5. **Empirical Results**: Valid JSON in 10/10 runs; zero hallucinated owners; 92% accuracy on complex edge cases with changed decisions or unassigned tasks.
