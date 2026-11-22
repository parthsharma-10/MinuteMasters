# Business Model Canvas (BMC)
## Project: MinuteMasters (Transcript-to-Tasks)
**Document Type:** Business Model Canvas (BMC)  
**Team Name:** MinuteMasters  
**Team Leader:** Parth Sharma (S24CSEU1941)  
**Team Members:** Kabir Bakshi, Konark Kalra, Harsh Vardhan, Harsh Gangwar, Chakshu  
**Date:** 22 November 2026 | **Version:** 2.0  

---

### Executive Summary
MinuteMasters is a specialized, hallucination-resistant prompt engineering workflow that converts unstructured spoken meeting transcripts into verifiable decisions and action items with guaranteed task-owner-deadline binding. Designed to solve the "meeting follow-up collapse" documented in Jabra's 2026 global workplace research, MinuteMasters targets student clubs, university administrative bodies, and high-velocity engineering startups with a lightweight, privacy-first, zero-hallucination meeting intelligence platform.

---

## The 9 Blocks of the Business Model Canvas

### 1. Customer Segments
* **Primary (Academic & Campus):** Student club presidents, hackathon organizers, competitive coding team leads, and university committee note-takers (e.g., Bennett University societies) who lose actionable follow-ups in unstructured WhatsApp/verbal discussions.
* **Secondary (Startups & SME Tech Teams):** Early-stage engineering teams (5–30 engineers) running daily standups and sprint planning who find enterprise tools (Otter.ai, Teams Copilot) opaque, inaccurate, or prohibitively expensive ($20–$30/user/month).
* **Tertiary (Faculty & Research Labs):** Academic research groups and departmental committees needing compliant, auditable, and citation-backed meeting minutes for grants and administrative records.

### 2. Value Propositions
* **Zero-Hallucination Action Binding:** Two-stage adversarial verification ensures no task is assigned unless the speaker explicitly volunteered or accepted.
* **Deterministic Fallback Transparency:** Missing owners or ambiguous deadlines are explicitly tagged as `"not stated"` rather than being fabricated.
* **Verbatim Grounding & Auditability:** Every decision and task is linked directly to a word-for-word transcript evidence quote.
* **Frictionless Export:** Instantly generates RFC 8259-compliant JSON for Jira/Linear/GitHub Issues and clean Markdown tables for Slack/WhatsApp.
* **Cost Efficiency:** Consumes minimal token overhead (approx. $0.0003 per meeting on Gemini 2.5 Flash), offering a 90% cost reduction compared to legacy meeting recording bots.

### 3. Channels
* **Direct Web Application (Streamlit / Next.js):** Browser-based paste-and-extract interface for instant ad-hoc transcript processing.
* **Google Workspace & Meet Extension:** Chrome browser extension capturing transcripts directly from Google Meet or Zoom web.
* **GitHub Marketplace & Developer CLI:** Python CLI and GitHub Action for automated standup transcript summarization in software repos.
* **Campus Word-of-Mouth & Student Society Deployments:** Pilot deployments across campus student clubs and project batches.

### 4. Customer Relationships
* **Transparent & Trust-Centric:** Clear distinction between verified facts and unstated ambiguities; users inspect supporting citations on hover.
* **Self-Service Onboarding:** No-configuration start; users paste transcripts and immediately receive formatted markdown action checklists.
* **Community-Driven Open Testing:** Fictional benchmark transcripts published open-source for community validation and model comparison.

### 5. Revenue Streams
* **Freemium Tier (Free Forever):** Web UI access for students and individuals processing up to 15 meeting transcripts per month.
* **Campus & Student Society Pass ($2.99 / semester / team):** Unlimited transcript parsing, custom club templates, and bulk CSV export.
* **Developer & Team SaaS ($6 / seat / month):** Direct Jira, Linear, Slack, and Google Calendar API integrations, custom few-shot schema tuning, and SOC2/GDPR on-premise privacy proxy.
* **Enterprise API Licensing:** Pay-per-transcript API for universities and enterprise knowledge bases ($0.02 per processed transcript).

### 6. Key Resources
* **Proprietary Two-Stage Prompt Architecture:** Highly optimized P1 (Extraction) and P2 (Verification) prompts engineered with adversarial constraints and calibrated few-shot exemplars.
* **Curated Evaluation Benchmark:** 12+ meticulously hand-labeled transcripts containing messy speech, changed decisions, and code-switching edge cases.
* **Technical Infrastructure:** Streamlit Cloud hosting, Python orchestration library, and Google AI Studio / Gemini API integration.
* **Human Intellectual Capital:** 6-member engineering team specializing in prompt design, evaluation metrics, and full-stack implementation.

### 7. Key Activities
* **Prompt Optimization & Error Analysis:** Continuous evaluation of prompt variants against hallucination metrics, deadline parsing, and speaker binding.
* **Pipeline Engineering:** Maintaining low-latency, deterministic multi-turn model chaining and schema enforcement.
* **Benchmark Expansion:** Curating challenging edge-case datasets (multilingual code-switching, overlapping interruptions, contradictory votes).
* **User Feedback Loops:** Gathering user testing data from club secretaries and team leads to refine edge-case handling.

### 8. Key Partners
* **Foundation Model Providers:** Google Cloud / Google AI Studio (Gemini 2.5 Flash), Anthropic, and OpenAI providing resilient API inference.
* **University Ecosystem:** Bennett University student societies, project committees, and faculty mentors providing real-world testing environments and feedback.
* **Open Source Developer Ecosystem:** Streamlit, LangChain, and Python open-source community providing rapid prototyping tools.

### 9. Cost Structure
* **LLM API Inference Costs:** Variable token costs per run (~$0.0003 per meeting on Gemini 2.5 Flash; ~$0.002 on GPT-4o-mini).
* **Hosting & Compute Infrastructure:** Streamlit Cloud / Vercel hosting for prototype and web application ($0–$20/month).
* **Domain & Security Infrastructure:** SSL certificates, DNS routing, and testing domain maintenance ($15/year).
* **Development & Evaluation Overhead:** Team engineering hours (student project sweat equity), local testing, and documentation generation.
