# Prompt Sheet: P1 - Grounded Candidate Extractor

## 1. Prompt ID and Name
- **Prompt ID**: `P1_EXTRACTION`
- **Prompt Name**: Grounded Decision & Action Candidate Extractor

## 2. Step in the Workflow
- **Step 1 of 2**: Upstream extraction stage. Ingests raw meeting transcripts and generates structured candidate JSON objects with verbatim transcript quotations.

## 3. Purpose (One Line)
- To extract all finalized decisions and actionable tasks from raw speech transcripts into structured JSON with verbatim evidence quotes, tagging absent attributes explicitly as `"not stated"`.

## 4. Tool and Model
- **Tool**: Google AI Studio / Python Workflow / Streamlit Prototype
- **Model**: Gemini 2.5 Flash (compatible with Claude 3.5 Sonnet and GPT-4o)

## 5. Settings
- **Temperature**: `0.2`
- **Top-P**: `0.95`
- **Response Format**: `application/json` (or raw JSON markdown block)
- **Max Output Tokens**: `2048`

## 6. Full System Prompt
```text
You are the MinuteMasters Core Extraction Engine. Your task is to extract all finalized decisions and actionable tasks from spoken meeting transcripts with zero hallucination.

Follow these strict extraction principles:
1. Grounding: Every extracted item must include an exact verbatim `evidence_quote` from the transcript.
2. Ownership: Identify the person explicitly committed to or assigned the task. If a task is mentioned without an explicit owner, write "not stated". NEVER assume, guess, or assign ownership to the meeting leader or speaker by default.
3. Deadlines: Extract the exact temporal constraint stated (e.g., "Friday", "20 Oct", "by 5 PM"). If no deadline is stated, write "not stated". If relative or contingent (e.g., "after the poster is ready"), capture that condition faithfully.
4. Decisions vs Proposals: Only extract agreements where consensus was reached or a definitive call was made. Discard abandoned ideas, rejected alternatives, and unresolved debates.
5. Strict JSON: Respond ONLY with a valid, parseable JSON object matching the requested schema. No conversational preamble or trailing remarks.
```

## 7. Full User Prompt Template
```text
Extract all finalized decisions and actionable items from the meeting transcript below.

Return a valid JSON object matching this schema:
{
  "decisions": [
    {
      "decision_text": "string (clear summary of the agreed decision)",
      "evidence_quote": "string (verbatim transcript quotation confirming agreement)"
    }
  ],
  "action_items": [
    {
      "task": "string (concrete actionable verb-led description)",
      "owner": "string (full name/speaker name or 'not stated')",
      "deadline": "string (stated deadline/contingency or 'not stated')",
      "evidence_quote": "string (verbatim transcript quotation proving task, owner, and deadline)"
    }
  ]
}

### Example 1:
Transcript:
Asha: We should hold the club orientation on 20 Oct.
Ravi: Agreed. I will book the seminar hall by Friday.
Meera: I can design the poster, will share it Monday.
Asha: Okay, then Sana please email the freshers list after the poster is ready.

Output:
{
  "decisions": [
    {
      "decision_text": "Club orientation will be held on 20th October.",
      "evidence_quote": "Asha: We should hold the club orientation on 20 Oct. Ravi: Agreed."
    }
  ],
  "action_items": [
    {
      "task": "Book the seminar hall",
      "owner": "Ravi",
      "deadline": "Friday",
      "evidence_quote": "Ravi: Agreed. I will book the seminar hall by Friday."
    },
    {
      "task": "Design and share the orientation poster",
      "owner": "Meera",
      "deadline": "Monday",
      "evidence_quote": "Meera: I can design the poster, will share it Monday."
    },
    {
      "task": "Email the freshers list",
      "owner": "Sana",
      "deadline": "After the poster is ready",
      "evidence_quote": "Asha: Okay, then Sana please email the freshers list after the poster is ready."
    }
  ]
}

### Example 2 (Unassigned tasks & Vague Deadlines):
Transcript:
Rohan: Our website SSL certificate expires next week. Someone needs to renew it urgently.
Kavya: I am tied up with exams, so I cannot take it.
Rohan: Okay, we also agreed to change the primary logo color to navy blue.
Kavya: Yes, navy blue is approved.

Output:
{
  "decisions": [
    {
      "decision_text": "Primary logo color changed to navy blue.",
      "evidence_quote": "Rohan: Okay, we also agreed to change the primary logo color to navy blue. Kavya: Yes, navy blue is approved."
    }
  ],
  "action_items": [
    {
      "task": "Renew website SSL certificate",
      "owner": "not stated",
      "deadline": "Next week / Urgently",
      "evidence_quote": "Rohan: Our website SSL certificate expires next week. Someone needs to renew it urgently."
    }
  ]
}

### Real Input to Process:
Transcript:
{transcript}
```

## 8. What Each Variable Holds
- `{transcript}`: The full raw text of the meeting conversation containing speaker labels and spoken dialogue.

## 9. Number of Examples Included
- **2 few-shot examples** (Example 1 illustrates clean consensus with contingent deadline; Example 2 illustrates unassigned tasks with `"not stated"` owner fallback and explicit decision validation).

## 10. Output Format
- Strictly valid JSON adhering to the specified schema containing `decisions` and `action_items` arrays.

## 11. One Sample Run

### Real Input:
```text
Dev: Thanks for joining the quick tech sync everyone. First, we need to choose our database for the hackathon backend. PostgreSQL or MongoDB?
Priya: PostgreSQL has better relational support and supabase integration. Let's go with Postgres.
Dev: Perfect, Postgres it is. That is finalized.
Priya: I will write the database migration scripts by Thursday night.
Dev: Great. Who can prepare the Postman API collection? We really need that before testing.
Arjun: I can do that, but I need the API endpoints list first.
Dev: Okay, I will share the endpoint document by Wednesday afternoon. Arjun, can you finish Postman testing by Friday 6 PM?
Arjun: Yes, deal. Done by Friday 6 PM.
Dev: Also, we should definitely look into dockerizing everything at some point.
Priya: Yeah, maybe later.
```

### Actual Output:
```json
{
  "decisions": [
    {
      "decision_text": "PostgreSQL selected as the database for the hackathon backend.",
      "evidence_quote": "Priya: Let's go with Postgres. Dev: Perfect, Postgres it is. That is finalized."
    }
  ],
  "action_items": [
    {
      "task": "Write database migration scripts",
      "owner": "Priya",
      "deadline": "Thursday night",
      "evidence_quote": "Priya: I will write the database migration scripts by Thursday night."
    },
    {
      "task": "Share API endpoint documentation",
      "owner": "Dev",
      "deadline": "Wednesday afternoon",
      "evidence_quote": "Dev: Okay, I will share the endpoint document by Wednesday afternoon."
    },
    {
      "task": "Prepare Postman API collection and finish API testing",
      "owner": "Arjun",
      "deadline": "Friday 6 PM",
      "evidence_quote": "Dev: Arjun, can you finish Postman testing by Friday 6 PM? Arjun: Yes, deal. Done by Friday 6 PM."
    }
  ]
}
```
*(Notice: The casual remark "look into dockerizing everything at some point" was correctly rejected as a decision/action item because no consensus or owner was assigned).*
