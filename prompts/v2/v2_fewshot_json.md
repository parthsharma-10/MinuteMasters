# Prompt Version 2 (Few-Shot JSON Schema)

## Metadata
- **Version**: 2.0 (Intermediate Iteration)
- **Author**: Konark Kalra & Harsh Vardhan
- **Date**: 15 November 2026
- **Tool / Model**: Gemini 2.5 Flash / Claude 3.5 Sonnet
- **Settings**: Temperature = 0.5
- **Workflow Step**: Single-step structured JSON extraction

---

## System Prompt
```text
You are an expert executive secretary and project manager. Your job is to extract clear decisions and action items from transcripts into strictly valid JSON format.
```

## User Prompt Template
```text
Extract all finalized decisions and actionable tasks from the following transcript into the specified JSON format.

JSON Schema:
{
  "decisions": [
    "string"
  ],
  "action_items": [
    {
      "task": "string (concise description)",
      "owner": "string (person responsible)",
      "deadline": "string (time or date)"
    }
  ]
}

### Example 1:
Transcript:
Asha: Let's lock in the orientation date for 20th Oct.
Ravi: Agreed, 20th Oct is final. I will book the seminar hall by Friday.
Meera: I'll design the poster and send it by Monday morning.

Output:
{
  "decisions": [
    "Club orientation will take place on 20th October."
  ],
  "action_items": [
    {
      "task": "Book the seminar hall",
      "owner": "Ravi",
      "deadline": "Friday"
    },
    {
      "task": "Design and share the orientation poster",
      "owner": "Meera",
      "deadline": "Monday morning"
    }
  ]
}

### Now process this transcript:
Transcript:
{transcript}
```

---

## Variable Dictionary
- `{transcript}`: Meeting transcript text to be parsed.

---

## Few-Shot Examples Included
- **Count**: 1 in-context example.

---

## Output Format
- Valid JSON object matching schema.

---

## Observed Limitations & Failure Modes
1. **Schema Breakages in Complex Runs**: Out of 10 experimental runs, the model included introductory conversational text ("Here is your JSON:") 3 times, causing JSON parsing exceptions.
2. **Missing Owner Confusion**: When an owner was absent ("We need to print posters"), the model filled `owner: "Team"` or guessed the meeting organizer instead of explicitly tagging it as unknown.
3. **No Verifiability**: No source quotation was provided, making it impossible for a downstream human or software validator to confirm if the LLM hallucinated a commitment.
