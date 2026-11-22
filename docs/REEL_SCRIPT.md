# MinuteMasters — Milestone 2 Video Reel Script & Storyboard
## Title: Transcript-to-Tasks: Zero-Hallucination Meeting Intelligence
**Total Target Duration:** **118 seconds** *(Strictly within the mandatory 90–150s range)*  
**Speakers:** Parth Sharma (Voice-over) & Chakshu (Screen Navigation)  
**Format:** Horizontal / 1080p Screen Recording with Crisp Voice-over & Captions  

---

## Second-by-Second Storyboard & Recording Script

### Part 1: Problem Definition (0:00 – 0:11 | Duration: ~11 seconds)
- **Visual on Screen:**  
  Start on the title slide of MinuteMasters showing the Bennett University logo, team members, and a split screen of a messy 50-line WhatsApp/Zoom meeting transcript with unanswered questions.
- **On-Screen Text Overlay:**  
  *58% of meeting time wasted | 91% leave with unclear action items (Jabra 2026)*
- **Voiceover (Parth):**  
  > "In student clubs, dev teams, and campus committees, crucial decisions get lost inside messy meeting conversations. Notes are written late or incompletely, so tasks are forgotten. Jabra's 2026 research found that 91% of workers leave meetings with unclear action items. We built **Transcript-to-Tasks** to fix this."

---

### Part 2: Prompt Experiment: Before & After (0:11 – 0:48 | Duration: ~37 seconds)
- **Visual on Screen (0:11 – 0:28):**  
  Show the screen displaying **Prompt Version 1 (Baseline)** in a text editor or ChatGPT.  
  Highlight the baseline prompt: `"Read the meeting transcript below and list the decisions made and the action items..."`  
  Click run on a transcript with an unassigned task (*"Someone needs to renew the SSL certificate urgently"*).  
  Zoom in on the flawed output: The model guesses that the meeting organizer is the owner: `Owner: Rohan`.
- **On-Screen Text Overlay (Red Callout):**  
  *Baseline v1 Failure: Hallucinated Owner + Unstructured Text*
- **Voiceover (Parth):**  
  > "Here is our Milestone 1 baseline prompt. Notice how vague it is. When someone says 'Someone needs to renew the SSL certificate', the baseline model hallucinates an owner, guessing Rohan just because he spoke. In our tests, v1 hallucinated owners in nearly 40% of cases."

- **Visual on Screen (0:28 – 0:48):**  
  Transition cleanly to **Prompt Version 3 (Production Pipeline)**.  
  Show the two-stage decoupled architecture: Prompt P1 with strict JSON schema and `"not stated"` fallback, followed by Prompt P2 Verification.  
  Show the improved output for the exact same sentence:  
  `Task: Renew website SSL certificate | Owner: not stated | Deadline: Urgently | Status: VERIFIED`.
- **On-Screen Text Overlay (Green Callout):**  
  *Prompt v3 Grounded Pipeline: Zero Hallucination + Exact Verbatim Quotes*
- **Voiceover (Parth):**  
  > "In Version 3, we decoupled extraction from verification and enforced mandatory verbatim evidence quotes with a strict 'not stated' fallback. Now, the model refuses to guess: it tags the owner as 'not stated', quotes the exact transcript line, and verifies it. Hallucinations dropped to zero."

---

### Part 3: Working Demo on Real Input (0:48 – 1:38 | Duration: ~50 seconds)
- **Visual on Screen (0:48 – 1:00):**  
  Open the live **Streamlit Web Application Prototype** (`code/app.py`).  
  Mouse hovers over the sidebar showing model selection (Gemini 2.5 Flash, Temp=0.2).  
  From the dropdown, select **T01: Club Orientation Planning**.  
  Show the transcript loaded in the text area.
- **Voiceover (Parth):**  
  > "Now, let’s see the full solution running live in our Streamlit web prototype. We select our Club Orientation transcript with three speakers: Asha, Ravi, and Meera, planning a venue booking, a poster, and an email list."

- **Visual on Screen (1:00 – 1:22):**  
  Click the blue button: **🚀 Run Transcript-to-Tasks Workflow**.  
  In under 1.5 seconds, the results animate on screen.  
  Show the clean green alert: *"Workflow Executed Successfully!"*  
  Show **Finalized Decisions**:  
  - *Club orientation will be held on 20th October.*  
  Show the rendered **Verified Action Items Checklist** table:  
  - Row 1: `Book seminar hall | Ravi | Friday | [Verified]`  
  - Row 2: `Design orientation poster | Meera | Monday | [Verified]`  
  - Row 3: `Email freshers list | Sana | After poster is ready | [Verified Contingent]`
- **Voiceover (Parth):**  
  > "In one click, the two-stage pipeline runs. It extracts the finalized decision, binds Ravi to booking the hall by Friday, Meera to the poster by Monday, and handles Sana's contingent deadline. Notice every single row is grounded with a verbatim transcript quote."

- **Visual on Screen (1:22 – 1:38):**  
  Switch the dropdown to **T08: Sports Meet Changed Decision (Edge Case)**.  
  Click run. Highlight the table showing that the initial Saturday proposal was discarded and Neha's cancelled task was reassigned to Sameer on Sunday morning.  
  Click the **Export to JSON / Markdown** button to show instant interoperability.
- **Voiceover (Parth):**  
  > "Even on complex edge cases where decisions change mid-meeting—like cancelling Saturday for Sunday—our verification auditor prunes the superseded proposal and captures the new owner accurately."

---

### Part 4: Progress and Next Steps for Milestone 3 (1:38 – 1:58 | Duration: ~20 seconds)
- **Visual on Screen (1:38 – 1:58):**  
  Show the project summary slide:  
  - 10 out of 12 benchmark tests passing  
  - Fully working Streamlit UI and Python orchestrator  
  - 4 Working Modules  
  - Milestone 3 Roadmap: Multilingual Hinglish temporal resolution, Jira/Slack automated webhook sync, and meeting classifier guardrail.  
  Display team credits: MinuteMasters, Bennett University.
- **Voiceover (Parth):**  
  > "For Milestone 2, our core extraction, verification, UI, and benchmark modules are all fully working. For Milestone 3, we will add an automatic guardrail classifier, resolve Hinglish temporal phrases like 'kal shaam', and build direct webhook sync to Jira and Slack. Thank you!"

---

## Technical Checklist for Recording Teammates
1. [ ] Set screen resolution to 1920x1080 (1080p).
2. [ ] Test microphone levels to ensure voice-over is crisp without echo.
3. [ ] Total video file runtime must be between **90 and 150 seconds** (target 118s).
4. [ ] Upload to Google Drive or YouTube as **Unlisted**; verify link sharing is set to **"Anyone with the link can view"** (test in Incognito mode!).
