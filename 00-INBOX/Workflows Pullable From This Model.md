Projects (Priority 1):

CommonGrounds — concept born April 25; pre-launch; the only gate is Whisper running locally on laptop

Electrician / Peaslee Tech — seat NOT secured; WIOA call to Phyllis Gingette (785-840-9675) is the unlock; Oct 27 cohort, $2,625 tuition

GLWC — PAUSED; Samantha conversation required first; Two-Hat principle always active

Projects (Priority 2): Ctrl+You (POD model, DSP niche, Printify → Shopify); YouTube BrayDonDon; Track A faceless channel (blocked on n8n + Ollama desktop) .

Workflows Pullable From This Model
Workflow A — Daily Re-Entry (under 5 min)
Open 01-DAILY — create today's daily note

Check ACTIVE-PROJECTS.md → Hard Deadlines table first, then Priority 1 next steps

Check FINANCIAL-SNAPSHOT.md for any cash alerts

Pick one next action — execute it, don't plan more

Workflow B — Financial Extraction (Stage 1, NOW)
Convert SoFi PDF statement to plain text

Open LM Studio 0.4.12 → load Qwen2.5-7B-Instruct Q4_K_M

Paste 07-TEMPLATE/compressed-mdfinancial.md as system prompt (≤500 tokens — Tier 1)

Paste statement plain text as user message (Tier 2 ≤2,500–3,000 tokens); chunk if larger

Copy structured output → paste into a Perplexity session

Perplexity updates FINANCIAL-SNAPSHOT.md and 05-INDEX/FINANCE-REGISTER.md

Commit: [FINANCE] update: SoFi [month] extraction complete

Workflow C — Brain Entry Compilation
End of AI thread → type /mdsummary

Review generated Brain Entry frontmatter (15 open questions, OQ IDs, correct canonical targets)

Verify filename follows YYYYMMDD-[DOMAIN]-[slug]-BE.md convention (BE at tail)

Push file to 02-BRAIN-ENTRIES/ via GitHub MCP or Obsidian Git

Run utils/rebuild_index.py locally to regenerate MASTER-INDEX.csv

Commit and push

Workflow D — Device Session (LLM work on laptop)
Before opening LM Studio: close Comet, Discord, all Electron apps

Optionally run ISLC (free memory threshold 2048 MB)

In LM Studio → Developer Mode → apply canonical settings: 4096 context, 0 GPU, 4 CPU threads, Flash Attention ON, KV Q4_0, mmap ON, mlock OFF

Load Qwen2.5-7B-Instruct Q4_K_M — one document per session

Workflow E — Project Unlock: CommonGrounds
The only gate is Whisper . One afternoon:

Install Whisper locally on laptop (post-optimization — RAM headroom should exist now)

Transcribe one real audio clip — confirm it works

Record first YouTube video: screen capture of the Whisper setup, honest commentary, no face required

After that: create 03-PROJECTS/COMMONGROUNDS-PROJECT.md stub

What's Incomplete / Still Needs To Move
These are the highest-priority open questions as of right now:

OQ-20260502-003 (DEVICE-ECOSYSTEM): What was idle RAM post-reboot after the optimizer script ran today? — this closes the debloat loop

OQ-20260502-005 (FINANCIAL-SNAPSHOT): Does the compressed-mdfinancial prompt produce clean structured output on the first live SoFi statement test? — Stage 1 has never actually run yet

Peaslee WIOA call — seat is not secured; Oct 27 starts in ~25 weeks

GitHub PAT on iPhone expires May 22 — 20 days from today

DEVICE-ECOSYSTEM.md still needs OS corrected from Windows 11 → Windows 10 Pro 22H2 build 19045.6466 — was flagged today but the canonical file may not yet reflect it