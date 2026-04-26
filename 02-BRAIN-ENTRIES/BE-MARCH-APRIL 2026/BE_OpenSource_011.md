---
entry_id: [UNASSIGNED — assign when compiled with other entries]
date_logged: 2026-04-16
source_thread_date: 2026-04-05 through 2026-04-14
source_thread_title: "Open-Source AI Setup, LM Studio, Local Models,
                       Device Workflow"
entry_type: tool / ai-system / skill / meta
chronological_position: UNKNOWN — to be placed during compilation session
status: draft
supersedes: UNKNOWN — cannot confirm without seeing other entries
superseded_by: none
canonical_file: AI-WORKFLOW-RULES / BRAINOS-SYSTEM / BRAYDEN-IDENTITY
                / SKILLS-EDUCATION / KRAY-STUDIOS-CONTENT
                / [NEW: DEVICE-ECOSYSTEM]
context_available: none — isolated thread
tags: [open-source-ai, local-models, device-inventory, obsidian,
       lm-studio, ollama, laptop-setup, second-brain, tool-stack,
       naming-convention, adhd-workflow]
open_questions:
  - id: OQ-20260425-001
    question: "Create DEVICE-ECOSYSTEM.md — this thread is the primary seed"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260425-002
    question: "confirm Ollama install completed (download confirmed"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
---
# Brain Entry [UNASSIGNED] — Local open-source AI stack introduced;
  laptop partially set up; full device ecosystem planned

---

## 🔒 CONFIRMED FACTS

| Fact | Value | Where in Thread |
|------|-------|-----------------|
| Desktop CPU | AMD Ryzen 7 7700X | User stated directly |
| Desktop GPU | NVIDIA RTX 3060 12GB VRAM | User stated directly |
| Desktop RAM | 64GB | User stated directly |
| Desktop location | Home — Lawrence, KS | User stated directly |
| Desktop setup status (as of 4/11/2026) | Nothing installed yet | User stated directly |
| Laptop GPU | Intel Iris Xe (integrated, no dedicated GPU) | User stated directly |
| Laptop RAM | 8GB | User stated directly |
| Laptop OS | Windows | Inferred from download page shown (PowerShell install command, .exe files) |
| iPhone model | iPhone 15 | User stated directly |
| iPhone storage | 128GB | User stated directly |
| iPad model | 5th generation, main model (not mini or air) | User stated directly |
| iPad chip year | 2017 | User stated directly |
| iPad storage | 64GB | User stated directly |
| External drive 1 | 2TB | User stated directly |
| External drive 2 | 1TB | User stated directly |
| LM Studio version installed | 0.4.9-1 x64 | Screenshot — file dated 4/5/2026 1:44 AM |
| LM Studio install date | 4/5/2026 1:44 AM | Screenshot filename + timestamp |
| Ollama installer downloaded | 4/5/2026 1:40 AM (~1.8GB) | Screenshot timestamp |
| LocalSend version downloaded | 1.17.0 windows-x86-64 | Screenshot filename |
| LocalSend download date | 4/5/2026 2:37 AM | Screenshot timestamp |
| Obsidian version downloaded | 1.12.7 | Screenshot filename |
| Obsidian download date | 4/5/2026 2:22 AM | Screenshot timestamp |
| Syncthing downloaded | 4/5/2026 2:38 AM | Screenshot timestamp |
| Pinokio downloaded | 4/5/2026 2:41 AM (~121MB) | Screenshot timestamp |
| Spacedesk downloaded | 4/5/2026 11:36–11:37 PM | Screenshot timestamp |
| Spacedesk status | Installed and confirmed working with iPad | User stated directly |
| Syncthing status | Installed, running | Desktop screenshot shows icon |
| LM Studio status | Installed, Gemma 3 1b tested and running | User confirmed + screenshot |
| Obsidian status | Installed, no real vault created | User stated directly |
| LocalSend laptop status | Downloaded, not configured | User stated directly |
| "Test Vault" in Obsidian | Throwaway — not real content | User stated directly |
| Gemma 3 1b speed on laptop | 18.66 tok/sec | Screenshot stat bar |
| Gemma 3 1b response length (test) | 116 tokens | Screenshot stat bar |
| Gemma 3 1b response time (test) | 2.44 seconds | Screenshot stat bar |
| Gemma 3 1b stop reason | EOS Token Found (normal) | Screenshot stat bar |
| Gemma 3 1b image support | None — text only | Screenshot error: "Model does not support image input" |
| iPhone setup status | Nothing done — starting from scratch | User stated directly |
| iPad setup status | Spacedesk only — all else pending | User stated directly |
| Desktop setup status | Fully pending | User stated directly |
| Hugging Face account | Does not exist yet | User stated directly |
| Vault name decision | "Test Vault" discarded; new vault to be created after Google Drive + Space org is complete | User stated directly |
| Naming convention rule | Brand placeholder names not to be cemented in files/folders yet | User stated directly |
| GLWC name status | Essentially decided — can be referenced directly | User stated directly |
| "Kray Studios" name status | Provisional — do not cement in files/folders | User stated directly |
| "Ctrl+You" name status | Provisional — do not cement in files/folders | User stated directly |
| Current primary thinking tool | Perplexity (this) — user's main thinking interface | User stated directly |
| Current notes tools | Google Docs, phone Notes app, laptop Notes app | User stated directly |
| Model examined but not downloaded | TeichAI/gemma-4-31B-it-Claude-Opus-Distill-GGUF | User linked to Hugging Face page |
| Gemma 4 31B distill size (Q4_K_M) | 18.7GB | Hugging Face page read in thread |
| Gemma 4 31B distill license | Apache 2.0 | Hugging Face page read in thread |
| Gemma 4 31B distill base | Google Gemma 4 architecture, fine-tuned on Claude Opus 4.6 reasoning outputs | Hugging Face page read in thread |
| Gemma 4 31B modalities | Text, image, audio (30s max), video (60s as frames) | Hugging Face page / model card in thread |
| Thinking mode trigger | Add `<|think|>` to system prompt | Model card quoted in thread |
| Gemma 4 31B recommended settings | temperature=1.0, top_p=0.95, top_k=64 | Model card quoted in thread |
| Local models — internet access | None by default | Stated in thread |
| Local models — token cost | Zero — no usage cost, no monthly cap | Stated in thread |
| Local model context window limit | Exists per model (varies 8k–128k+) but resets per chat, no charge | Stated in thread |
| LM Link feature | Laptop connects to desktop LM Studio wirelessly, uses desktop GPU as if local | LM Studio page read in thread |
| LM Link security | End-to-end encrypted via Tailscale mesh VPN | LM Studio page read in thread |
| LM Link status | Preview — rolling out in batches | LM Studio page read in thread |
| User's honest system assessment | Hopes this is the hardest part; concerned about clunky execution and unforeseen errors from past Perplexity systems | User stated directly |

---

## 🕐 TIMELINE MARKERS

- **4/5/2026 ~1:40 AM** — Ollama installer downloaded on laptop
- **4/5/2026 ~1:44 AM** — LM Studio 0.4.9 downloaded on laptop
- **4/5/2026 ~2:11 AM** — "Thinking Mode.png" saved (screenshot of LM Studio concept)
- **4/5/2026 ~2:22 AM** — Obsidian 1.12.7 downloaded
- **4/5/2026 ~2:34 AM** — "Test Vault" folder created (throwaway)
- **4/5/2026 ~2:37 AM** — LocalSend downloaded
- **4/5/2026 ~2:38 AM** — Syncthing downloaded
- **4/5/2026 ~2:41 AM** — Pinokio downloaded
- **4/5/2026 ~11:36–11:37 PM** — Spacedesk drivers downloaded (32-bit + 64-bit)
- **4/7/2026 ~10:35 PM** — Syncthing folder modified (suggests it was actively used)
- **4/11/2026** — User in Topeka, KS; reviewed thread and answered follow-up questions
- **4/14/2026** — User in Lawrence, KS; thread finalized

---

## 📋 UPDATES TO CANONICAL FILES

- **BRAYDEN-IDENTITY:** Add full device inventory with confirmed specs
  (desktop, laptop, iPhone 15, iPad 5th gen 2017, both external drives).
  Add current location of desktop (Lawrence, KS home).

- **AI-WORKFLOW-RULES:** Add full local tool stack table. Add naming
  convention rule (no brand name cementing). Add local AI concepts
  glossary (inference, quantization, context window, tokens locally,
  VRAM offloading). Add LM Link connectivity method. Add internet
  access limitation note for local models. Add document output method
  (LibreOffice). Add Gemma 4 31B as target desktop model with pull
  command and settings.

- **BRAINOS-SYSTEM:** Add vault rebuild protocol (8-step sequence,
  triggered after all brain entries + Google Drive org complete).
  Add daily workflow pipeline (Capture → Process → Create → Publish).
  Add ADHD-specific workflow rules (single entry point, Daily note,
  PocketPal as zero-friction capture). Add forward rules for adding
  entries without confusion, modifying canonical files, adding new tools.

- **SKILLS-EDUCATION:** Add open-source AI vocabulary section.
  Add local model concepts. Add confirmed tools learned this thread.

- **KRAY-STUDIOS-CONTENT:** Add full creative pipeline. Add image
  generation stack (ComfyUI + Flux). Add video generation stack
  (Wan2GP). Add audio stack (Faster Whisper, MusicGen).

- **[NEW: DEVICE-ECOSYSTEM.md]:** Create new canonical file.
  Contains: confirmed hardware specs per device, per-device role
  definitions, per-device setup checklists with completion status,
  cross-device connectivity map, Syncthing/LocalSend/Möbius Sync
  configuration notes, Spacedesk setup, LM Link pairing instructions.

---

## ⚠️ CONTRADICTIONS

- Cannot fully assess — thread is partially isolated. Flag for review
  during compilation.

- **Naming convention:** This thread establishes that "Kray Studios"
  and "Ctrl+You" should NOT be cemented in files. If prior entries
  used these names as primary identifiers in canonical files, those
  references need to be reviewed and optionally replaced with
  functional descriptors. **Flag for Brayden to audit canonical files
  after all entries are compiled.**

- **Obsidian vault:** If any prior entry described a vault as
  "created" or "set up," this thread directly contradicts that —
  user confirmed no real vault exists yet. Test Vault is throwaway.
  **Resolution: this thread's state is the confirmed current reality.**

- **iPad model:** Thread initially unclear; user confirmed 5th gen
  2017 main model (not mini, not air). If prior entries named a
  different model, this thread's confirmation supersedes.

- **Device setup status:** If any prior entry described iPhone, iPad,
  or desktop as "set up" or "in progress," this thread resets all
  three to either fully pending (desktop, iPhone) or minimal
  (iPad = Spacedesk only).

---

## 🧠 INSIGHTS & PATTERNS

- User works late at night on technical setup tasks (all laptop
  installs between 1:40 AM – 2:41 AM, then resumed 11:36 PM same day).
  System design should account for late-night energy and interrupted
  sessions — tasks need to be completable in short bursts.

- User explicitly named concern about "systems built out in Perplexity
  that have unforeseen errors and clunky execution" — the brain system
  itself must be designed to be resilient, manually editable, and not
  dependent on any single thread's context being perfect.

- User's thinking primarily happens through Perplexity conversations,
  not structured notes. Obsidian will need a near-zero-friction
  entry point to become habitual, otherwise it won't get used.

- User is self-aware about ADHD impact on system maintenance. Any
  workflow that requires more than one decision to start will likely
  be abandoned. Design for one-tap, one-folder, one-action entry
  points everywhere.

- User downloaded all tools in one late-night session rather than
  spacing them out — suggests high-energy bursts followed by gaps.
  Setup tasks should be designed to be "pick up where you left off"
  without needing to re-read context.

- User is deliberately withholding brand name commitments until
  projects are more developed — this is a sign of healthy restraint,
  not indecision. Do not pressure naming in the brain system.

- User is approaching this as a long-term investment: "I hope this
  is the hardest, most time consuming part." Framing the entry
  process as "worth it" suggests motivation is present but needs
  visible progress markers to stay engaged.

---

## 🔧 TOOLS / RESOURCES REFERENCED

| Tool / Resource | Status | Notes |
|----------------|--------|-------|
| Ollama | Downloaded on laptop | Install confirmation unverified |
| LM Studio 0.4.9 | Installed, tested | Gemma 3 1b running at 18.66 tok/sec |
| Obsidian 1.12.7 | Installed | No real vault yet — pending Drive org |
| LocalSend 1.17.0 | Downloaded, not configured | Laptop only |
| Syncthing | Installed, running | Laptop — folder modified 4/7 |
| Pinokio | Downloaded | Not yet used |
| Spacedesk | Installed + working | iPad second monitor for laptop confirmed |
| Gemma 3 1b | Running