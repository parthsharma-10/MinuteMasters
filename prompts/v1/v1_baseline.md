# Prompt Version 1 (Baseline)

## Metadata
- **Version**: 1.0 (Milestone 1 Baseline)
- **Author**: Parth Sharma & Kabir Bakshi
- **Date**: 10 November 2026
- **Tool / Model**: ChatGPT (GPT-4o) / Gemini 1.5 Flash
- **Settings**: Temperature = Default (1.0)
- **Workflow Step**: Single-step unstructured extraction

---

## System Prompt
```text
You are a helpful meeting assistant.
```

## User Prompt Template
```text
Read the meeting transcript below and list the decisions made and the action items. For each action item give the task, the owner and the deadline.

Transcript:
{transcript}
```

---

## Variable Dictionary
- `{transcript}`: Raw unstructured meeting transcript containing speaker labels and conversational turns.

---

## Few-Shot Examples Included
- **Count**: 0 (Zero-shot)

---

## Output Format
- Unstructured free-form plain text or bulleted markdown list.

---

## Observed Limitations & Failure Modes
1. **Unpredictable Formatting**: The model switches arbitrarily between bullet points, nested lists, and paragraph summaries, making automated downstream parsing impossible.
2. **Owner Hallucination**: When a speaker says "Someone should email the freshers", v1 arbitrarily assigns ownership to the speaker or the last person who spoke.
3. **Deadline Guessing**: Infers implicit deadlines (e.g. interprets "soon" as "in a few days" or invents specific calendar dates not in transcript).
4. **False Decisions**: Classifies casual suggestions, brainstorming banter, or discarded proposals as finalized organizational decisions.
