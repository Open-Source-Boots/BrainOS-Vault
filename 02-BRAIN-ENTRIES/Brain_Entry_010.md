---
filename: Brain_Entry_010.md
thread_date: 2026-04-11
domain: BRAINOS-SYSTEM
status: canonical — source of truth for device inventory, open-source AI stack, and Obsidian setup sequence
priority: 1
compilation_status: pending
supersedes: nothing — this is new infrastructure detail not in prior entries
superseded_by: none
canonical_file: AI-WORKFLOW-RULES, BRAINOS-SYSTEM, SKILLS-EDUCATION, BRAYDEN-IDENTITY (device specs)
generated_by_skill: manual
tags: ['open-source', 'local-ai', 'lm-studio', 'ollama', 'obsidian', 'devices', 'infrastructure', 'second-brain', 'tools']
open_questions:
  - id: OQ-20260425-001
    question: "Create DEVICE-ECOSYSTEM.md — this entry + BE_OpenSource_011 are co-equal seed sources"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260425-002
    question: "complete laptop remaining tasks in order (Ollama confirm → LocalSend → LibreOffice → HuggingFace → KrayVault → Smart Connections → Syncthing)"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
entry_id: 8
date_logged: 2026-04-05 to 2026-04-11
source_thread_date: 2026-04-05 to 2026-04-11
source_thread_title: Open-Source AI Setup, LM Studio, Local Models, Device Workflow
entry_type: tool, ai-system, meta
notes: Overlaps significantly with BE_OpenSource_011.md — both cover April 5-11 device setup; during vault build treat Brain_Entry_010 as canonical and BE_OpenSource_011 as supplementary or merge them
---
# Brain Entry 010 — Open-Source AI Stack, Device Ecosystem & Second Brain Infrastructure

> **Thread significance:** This is the moment the second brain gained a physical infrastructure layer — not just notes and documents, but a network of devices running free, local, private AI tools. Core philosophy: owning your tools changes your relationship to the work. Renting AI (ChatGPT, Midjourney, Runway) means creative capacity is always someone else's decision. Running models locally means the only limit is hardware you already own.

---

## 🔒 CONFIRMED FACTS — DEVICE INVENTORY

### Desktop (Home — Lawrence, KS)
| Spec | Value |
|------|-------|
| CPU | AMD Ryzen 7 7700X |
| GPU | NVIDIA RTX 3060 — 12GB VRAM |
| RAM | 64GB |
| Role | Primary AI compute engine — large models, image/video generation, automation pipelines |
| Status | **Nothing installed yet as of April 11, 2026 — full setup pending** |

### Laptop (Current primary device)
| Spec | Value |
|------|-------|
| GPU | Intel Iris Xe integrated — no dedicated GPU |
| RAM | 8GB |
| OS | Windows |
| Role | Daily driver, command center, writing/planning, light local AI, remote access to desktop via LM Link |
| Status | **Partially set up — see setup section below** |

### iPhone 15
| Spec | Value |
|------|-------|
| Storage | 128GB |
| Role | Capture device (video, voice, photos), offline AI via PocketPal, note input to Obsidian, file transfer via LocalSend |
| Status | **Setup not started — starting from scratch** |

### iPad (5th Generation, 2017)
| Spec | Value |
|------|-------|
| Storage | 64GB |
| Chip | A9 — 3GB RAM |
| Role | Second monitor (Spacedesk), Obsidian writing surface, storyboard/sketch input, Procreate/ComfyUI pipeline |
| Status | Spacedesk installed and working — all other setup pending |
| Note | A9 chip limits PocketPal to small models (E2B tier) — heavier tasks route to iPhone 15 or desktop |

### External Storage
| Drive | Purpose |
|-------|---------|
| 2TB external HDD | AI model storage — Ollama models, ComfyUI checkpoints |
| 1TB external HDD | Raw footage archive, project assets |

---

## 🔒 CONFIRMED FACTS — LAPTOP SETUP (as of April 5–11, 2026)

| Tool | Version | Install Date/Time | Status |
|------|---------|-------------------|--------|
| LM Studio | 0.4.9-1 x64 | April 5, 2026 — 1:44 AM | ✅ Installed — Gemma 3 1b running, tested |
| Obsidian | 1.12.7 | April 5, 2026 — 2:22 AM | ✅ Installed — no real vault created yet |
| Syncthing (Windows) | — | April 5, 2026 — 2:38 AM | ✅ Installed, running (confirmed via desktop icon) |
| Spacedesk | Win10 32/64-bit | April 5, 2026 — 11:36 AM | ✅ Installed, tested, works with iPad |
| Ollama | Setup 1.8GB | April 5, 2026 — 1:40 AM | ⚠️ Downloaded — install status unconfirmed |
| LocalSend | 1.17.0 | April 5, 2026 — 2:37 AM | ⚠️ Downloaded — not configured |
| Pinokio | 121MB | April 5, 2026 — 2:41 AM | ⚠️ Downloaded — not installed |

### LM Studio — Confirmed Working on Laptop
- Model running: `google/gemma-3-1b` — text only
- Speed: **18.66 tok/sec on CPU only** — functional for daily use
- Tested with basic chat (Goodness Check session) — passed
- Limitation confirmed: Gemma 3 1b is text-only; image upload returns "Model does not support image input" — expected and normal
- Solution identified: **Gemma 3 4b has vision capability** — download in LM Studio when needed for image input tasks

### LM Studio Stats — Plain Language Reference
| Stat | Meaning |
|------|---------|
| tok/sec | Generation speed — 18 on laptop CPU is usable; desktop GPU will hit 40–80 |
| Token count | Length of response — 116 tokens ≈ 85 words |
| Stop reason: EOS Token Found | Model finished naturally — normal and good |
| Context window | 8k–32k tokens depending on model — won't be hit in normal creative/planning sessions |

---

## 📋 CORE INSIGHT — WHY THIS MATTERS

**The subscription problem being solved:**
Every major AI creative tool (ChatGPT Plus, Midjourney, Runway, Claude Pro) charges $20–$200/month. Combined, a full creative AI stack could cost $100–$300/month with no ownership. Local open-source AI eliminates this entirely after the one-time cost of hardware already owned.

**Key concepts — plain language reference:**
| Term | Meaning |
|------|---------|
| Model | The AI's brain — downloaded once (~20GB file), runs forever, no internet required |
| Inference | When the model actually thinks — your hardware pays the cost in electricity, not a monthly bill |
| Parameters (1B, 7B, 31B) | Model size — bigger = smarter but needs more RAM/VRAM; laptop runs 1B–4B, desktop runs up to 31B |
| Quantization (Q4, Q8) | Compression — Q4 = smaller/faster, slight quality loss; Q8 = larger/slower, near-full quality; **use Q4_K_M as default** |
| Context window | How much the model remembers within one conversation — local models have this limit too, but there is no token cost |
| VRAM vs RAM offloading | If a model is bigger than GPU VRAM, it spills into system RAM — still works, just slower; desktop (12GB VRAM + 64GB RAM) can run 18–20GB models this way |

**Key distinction — tokens locally:**
> On paid APIs: tokens = money. On local models: tokens = electricity only. No monthly cap, no usage limits, no rate limiting. The only ceiling is context window length per conversation, which resets each new chat.

---

## 📋 UPDATES TO CANONICAL FILES
- **AI-WORKFLOW-RULES:** Add open-source philosophy, token cost distinction, fabrication-prevention context (local models don't hallucinate differently — same rules apply), internet connectivity note
- **BRAINOS-SYSTEM:** Full device inventory, installed tool table, KrayVault folder structure, setup sequence — canonical here
- **SKILLS-EDUCATION:** Local AI literacy (model types, quantization, context windows) is a skill being actively built — log progress here
- **BRAYDEN-IDENTITY:** Device inventory — Desktop (RTX 3060, 64GB RAM), Laptop (8GB, Iris Xe), iPhone 15, iPad 5th Gen — canonical here

---

## ⚠️ CONTRADICTIONS
- **Notion:** Referenced in earlier threads as an active tool. **Deleted (Entry 008).** Not in the stack. Do not include in any future tool lists.
- **Internet access:** Local models have NO internet access by default — they only know their training data. To give a local model live information: use Open WebUI's web search toggle, or research in Perplexity then paste findings into the local model for deeper reasoning.

---

## 🧠 INSIGHTS & PATTERNS
- **Owning your tools changes your relationship to the work.** Renting AI means creative capacity is always someone else's decision. This is a philosophical anchor worth revisiting whenever a paid tool looks tempting.
- **The open-source stack directly serves every other project track** — YouTube editing, GLWC content, CtrlYou automation (n8n), BrainOS itself. It's not a separate project. It's the infrastructure layer under all of them.
- **Starting from scratch on iPhone and iPad** — this is an opportunity to build the capture → sync → vault workflow correctly the first time rather than retrofitting it.
- **Procreate Dreams** (Entry 008 flag) connects here — ComfyUI on desktop can generate assets that feed into Procreate Dreams animations on iPad. The pipeline exists in hardware already owned.

---

## 🔧 OPEN-SOURCE AI MODEL STACK — FULL REFERENCE

### Text / Reasoning Models
| Model | Role | Where It Runs |
|-------|------|--------------|
| Gemma 3 1b | Fast laptop daily driver — text only | Laptop |
| Gemma 3 4b | Laptop vision model — slower but sees images | Laptop |
| Llama 3.3 8b | Desktop daily reasoning model | Desktop |
| DeepSeek R1 14b | Desktop deep thinking, systems analysis | Desktop |
| Qwen 2.5 Coder 7b | Desktop coding, automation, scripting | Desktop |
| Gemma 4 31B (Claude Distill) | Desktop slow/deep reasoning — Claude-like quality | Desktop only |

### Gemma 4 31B Claude Distill — Key Facts
| Detail | Value |
|--------|-------|
| Model ID | `TeichAI/gemma-4-31B-it-Claude-Opus-Distill-GGUF` |
| What it is | Gemma 4 architecture fine-tuned on Claude Opus 4.6 high-reasoning outputs |
| Download command | `ollama pull hf.co/TeichAI/gemma-4-31B-it-Claude-Opus-Distill-GGUF:Q4_K_M` |
| Size | 18.7GB Q4_K_M — store on 2TB external drive |
| Desktop behavior | Overflows 12GB VRAM into 64GB RAM — runs at 3–8 tok/sec, usable for deep sessions |
| Capabilities | Text, image, audio, video (30s max as frames) |
| License | Apache 2.0 — fully open, commercial use allowed |
| Thinking mode | Add `think` to system prompt to see full internal reasoning chain |
| Best settings | temperature=1.0, top_p=0.95, top_k=64 |

### Image Generation
| Tool | Role | Where |
|------|------|-------|
| Flux.1-schnell | Best free image model, no watermarks | Desktop via ComfyUI |
| Pinokio | One-click installer for all AI apps | Desktop |

### Video Generation
| Tool | Role | Where |
|------|------|-------|
| LTX Video | Lighter/faster video model | Desktop |

### Audio / Transcription
| Tool | Role | Where |
|------|------|-------|
| MusicGen (AudioCraft) | Free local music + SFX generation | Desktop |

### File Sync / Device Network
| Tool | Role | Platforms |
|------|------|----------|
| LocalSend | Instant WiFi file transfer, no cloud | Win, iPhone, iPad |
| Syncthing | Continuous background folder sync | Win laptop ↔ Win desktop |
| Spacedesk | iPad as wireless second monitor for Windows | Laptop + iPad |

### Document Output (Free)
| Tool | Output | Where |
|------|--------|-------|
| LibreOffice | .docx, .odt, PDF | Laptop + Desktop |
| Browser Print | Save any page/text as PDF | Any device |

---

## 🔧 OBSIDIAN — KRAY VAULT SETUP (do not use Test Vault)

**Vault name:** `KrayVault`

**Folder structure:**
KrayVault/
├── Brain/ ← raw thoughts, voice memo transcripts
├── Scripts/ ← video/content scripts
├── Projects/ ← project-specific notes
├── Research/ ← articles, summaries
├── Prompts/ ← prompts that work — save these
└── Daily/ ← one note per day, stream of consciousness


**Plugin to install:** Smart Connections (Community Plugins → Browse → search "Smart Connections")

**Sync:** Configure Syncthing to sync KrayVault folder between laptop and desktop

---

## 🔧 PROJECT NAMING CONVENTION — SYSTEM RULE (confirmed April 11, 2026)

> **Decision logged:** Brand placeholder names are NOT to be cemented into second brain files, folder structures, or canonical documents at this stage.

| What it is | Use this in brain files | Eventual brand name (provisional) |
|------------|------------------------|----------------------------------|
| YouTube/media content channels | Media Channel Project or Creative Channel | Unnamed — do not cement |
| Online business / digital products | Online Business Project | CtrlYou (provisional) |
| Labor organizing / worker community | GLWC — Goodlife Workers Committee | Name essentially decided — use GLWC throughout |
| Local AI tools, content, workflow | Open-Source AI Project | Part of Media Channel |

> **Why this matters:** Folder names, Obsidian vault tags, Syncthing share names, and canonical file titles should use functional descriptors until the brand is formally launched and stable. This prevents a rename cascade across 50+ files later.
> **Exception:** GLWC (Goodlife Workers Committee) name is essentially decided — reference directly throughout brain files.

---

## 🔧 SETUP CHECKLISTS — PENDING (do in order)

### Laptop — Remaining Tasks
- [ ] Confirm Ollama installed — open PowerShell, run `ollama run gemma3:1b`
- [ ] Set `OLLAMA_MODELS` environment variable → point to 2TB external drive path (before pulling any models on desktop)
- [ ] Configure LocalSend — open app, confirm device name, leave running in system tray
- [ ] Install LibreOffice → libreoffice.org
- [ ] Create Hugging Face account → huggingface.co (required for model downloads including Gemma 4 31B)
- [ ] Create KrayVault in Obsidian (not Test Vault) — use folder structure above
- [ ] Install Smart Connections plugin in Obsidian
- [ ] Configure Syncthing — get laptop Device ID (Actions → Show ID) at `http://127.0.0.1:8384`
- [ ] Download Gemma 3 4b in LM Studio (vision/image input capability — 3GB)
- [ ] After desktop is set up: install LM Link on laptop, enter desktop's code → laptop uses desktop GPU wirelessly

### Desktop — Full Setup (all pending, do in this order)
**Phase 1 — Core AI stack:**
- [ ] Set `OLLAMA_MODELS` environment variable → point to 2TB external drive
- [ ] Install Ollama → ollama.com
- [ ] Pull models:
  - `ollama pull llama3.3:8b`
  - `ollama pull deepseek-r