"""
MinuteMasters: Transcript-to-Tasks Core Pipeline
Authors: MinuteMasters Engineering Team (Parth Sharma et al.)
Description: End-to-end two-stage prompt engineering workflow for mining decisions and verified action items.
"""

import json
import re
from typing import Dict, Any, List

class TranscriptToTasksPipeline:
    def __init__(self, model_name: str = "gemini-2.5-flash", temperature: float = 0.2):
        self.model_name = model_name
        self.temperature = temperature
        
    def get_p1_prompt(self, transcript: str) -> str:
        """Constructs Prompt P1 (Extraction)"""
        return f"""You are the MinuteMasters Core Extraction Engine. Extract all finalized decisions and actionable items from the meeting transcript below.

Return a valid JSON object matching this schema:
{{
  "decisions": [
    {{
      "decision_text": "string (clear summary of the agreed decision)",
      "evidence_quote": "string (verbatim transcript quotation confirming agreement)"
    }}
  ],
  "action_items": [
    {{
      "task": "string (concrete actionable verb-led description)",
      "owner": "string (full name/speaker name or 'not stated')",
      "deadline": "string (stated deadline/contingency or 'not stated')",
      "evidence_quote": "string (verbatim transcript quotation proving task, owner, and deadline)"
    }}
  ]
}}

### Rules:
1. Every item MUST have a verbatim evidence_quote from the transcript.
2. If owner is not explicitly stated or volunteered, write "not stated". NEVER guess.
3. If deadline is not explicitly stated, write "not stated".
4. Only extract genuine consensus decisions; skip casual ideas or discarded proposals.

Transcript:
{transcript}
"""

    def get_p2_prompt(self, transcript: str, candidate_json: str) -> str:
        """Constructs Prompt P2 (Adversarial Verification)"""
        return f"""You are the MinuteMasters Quality & Verification Auditor. Your objective is zero-hallucination verification.
You cross-examine candidate meeting minutes against the raw transcript. You reject any action item or decision that lacks direct transcript consensus or contains unconfirmed assumptions.

### Original Transcript:
{transcript}

### Candidate Minutes (Extracted by P1):
{candidate_json}

Audit each entry. Return a valid JSON object matching this schema:
{{
  "audit_summary": {{
    "decisions_verified": 0,
    "action_items_verified": 0,
    "hallucinations_pruned": 0,
    "modifications_made": ["string explanation of any corrected owner/deadline"]
  }},
  "verified_decisions": [
    {{
      "decision_text": "string",
      "evidence_quote": "string",
      "status": "VERIFIED"
    }}
  ],
  "verified_action_items": [
    {{
      "task": "string",
      "owner": "string (or 'not stated')",
      "deadline": "string (or 'not stated')",
      "evidence_quote": "string",
      "status": "VERIFIED | FLAGGED_MODIFIED"
    }}
  ],
  "markdown_table": "string (A complete markdown table with columns: | # | Task | Owner | Deadline | Status |)"
}}
"""

    def mock_run_test_sample(self, test_id: str) -> Dict[str, Any]:
        """Loads verified ground truth output for test cases when running in offline/dry-run mode."""
        output_file = f"test-data/outputs/{test_id}_output.json"
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"error": f"Output file for {test_id} not found"}

if __name__ == "__main__":
    print("MinuteMasters Transcript-to-Tasks Pipeline Initialized.")
    pipeline = TranscriptToTasksPipeline()
    sample_p1 = pipeline.get_p1_prompt("Asha: We meet tomorrow at 10 AM.")
    print("P1 Prompt Length:", len(sample_p1))
