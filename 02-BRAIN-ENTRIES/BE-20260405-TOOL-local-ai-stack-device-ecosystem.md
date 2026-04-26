---
date_logged: 2026-04-16
source_thread_date: 2026-04-05 through 2026-04-16
source_thread_title: "Open-Source AI Setup, LM Studio, Local Models,
                       Device Workflow"
entry_type: tool / ai-system / meta
chronological_position: UNKNOWN — to be placed during compilation session
status: draft
supersedes: UNKNOWN — cannot confirm without seeing other entries
superseded_by: none
canonical_file: AI-WORKFLOW-RULES / BRAINOS-SYSTEM / BRAYDEN-IDENTITY
                / SKILLS-EDUCATION / KRAY-STUDIOS-CONTENT
                / NEW: DEVICE-ECOSYSTEM
context_available: none — isolated thread. Memory search surfaced
  project arc and entry history but not full file contents.
tags: [open-source-ai, local-models, lm-studio, ollama, obsidian,
       device-inventory, laptop-setup, second-brain, naming-convention,
       adhd-workflow, tool-stack, kray-vault, brainos, full-circle,
       lm-link, gemma, flux, wan2gp, whisper, syncthing, localsend,
       spacedesk, pinokio, pocketpal, mobius-sync, hugging-face]
open_questions:
  - id: OQ-20260405-001
    question: "Create DEVICE-ECOSYSTEM.md canonical file — pull hardware inventory out of BRAYDEN-IDENTITY into it"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
---
# Brain Entry — Local open-source AI stack established on laptop;
  full device ecosystem designed; Obsidian introduced as brain storage;
  full-circle archival test completed

---

## CONFIRMED FACTS

### `tool` — Software installed on laptop

| Fact | Value | Source |
|------|-------|--------|
| LM Studio version | 0.4.9-1 x64 | Screenshot filename |
| LM Studio install date | 4/5/2026 1:44 AM | Screenshot timestamp |
| LM Studio status | Installed and tested | User confirmed + screenshot |
| Gemma 3 1b | Running, tested | Screenshot of active chat |
| Gemma 3 1b speed | 18.66 tok/sec | Screenshot stat bar |
| Gemma 3 1b response (test) | 116 tokens / 2.44s | Screenshot stat bar |
| Gemma 3 1b stop reason | EOS Token Found | Screenshot — confirmed normal |
| Gemma 3 1b image support | None — "Model does not support image input" | Screenshot error message |
| Ollama installer | Downloaded 4/5/2026 1:40 AM, ~1.8GB | Screenshot |
| Ollama install | Unconfirmed — installer downloaded only | User did not confirm run |
| Obsidian version | 1.12.7 | Screenshot filename |
| Obsidian download date | 4/5/2026 2:22 AM | Screenshot timestamp |
| Obsidian status | Installed, no real vault created | User stated directly |
| Test Vault | Exists, throwaway — not real content | User stated directly |
| LocalSend version | 1.17.0 windows-x86-64 | Screenshot filename |
| LocalSend download date | 4/5/2026 2:37 AM | Screenshot timestamp |
| LocalSend laptop status | Downloaded, not configured | User stated directly |
| Syncthing | Downloaded 4/5/2026 2:38 AM | Screenshot timestamp |
| Syncthing status | Installed, running | Desktop icon visible in screenshot |
| Syncthing folder last modified | 4/7/2026 10:35 PM | Screenshot timestamp |
| Pinokio | Downloaded 4/5/2026 2:41 AM, ~121MB | Screenshot |
| Pinokio status | Downloaded, not yet used | User implied |
| Spacedesk | Downloaded 4/5/2026 11:36–11:37 PM (32+64 bit) | Screenshot timestamps |
| Spacedesk status | Installed, confirmed working as iPad second monitor | User stated directly |

### `tool` — Model evaluated but not downloaded

| Fact | Value | Source |
|------|-------|--------|
| Model ID | TeichAI/gemma-4-31B-it-Claude-Opus-Distill-GGUF | User linked, page read |
| Architecture | Google Gemma 4 base | Hugging Face page |
| Fine-tune source | Claude Opus 4.6 high-reasoning outputs | Hugging Face page |
| License | Apache 2.0 | Hugging Face page |
| Q4_K_M size | 18.7 GB | Hugging Face page |
| Q3_K_M size | 15.3 GB | Hugging Face page |
| Q8_0 size | 32.6 GB | Hugging Face page |
| BF16 (full) size | 61.4 GB | Hugging Face page |
| Modalities | Text, image, audio (30s max), video (60s as frames) | Model card read in thread |
| Thinking mode trigger | `<\|think\|>` at start of system prompt | Model card read in thread |
| Recommended settings | temperature=1.0, top_p=0.95, top_k=64 | Model card read in thread |
| Desktop behavior | Overflows 12GB VRAM into 64GB RAM, ~3–8 tok/sec | Stated in thread |
| Download command | `ollama pull hf.co/TeichAI/gemma-4-31B-it-Claude-Opus-Distill-GGUF:Q4_K_M` | Stated in thread |

### `tool` — Local AI concepts confirmed in this thread

| Fact | Value | Source |
|------|-------|--------|
| Local model token cost | Zero — no usage cost, no monthly cap, no rate limit | Stated in thread |
| Local model internet access | None by default | Stated in thread |
| Context window | Exists per model, resets per chat, no charge | Stated in thread |
| EOS Token | Model finished naturally — normal and correct | Thread + screenshot |
| VRAM offloading | Model larger than VRAM spills into RAM — slower but functional | Stated in thread |
| OLLAMA_MODELS env var | Must be set before pulling to redirect to external drive | Stated in thread |
| Gemma 3 4b | Vision capable — upgrade from 1b for image input tasks | Stated in thread |
| Gemma 3n e2b/e4b | Designed for laptops, tablets, phones | Ollama library page read |
| LM Link | Laptop connects to desktop LM Studio wirelessly, uses desktop GPU | LM Studio page read |
| LM Link security | End-to-end encrypted, Tailscale mesh VPN | LM Studio page read |
| LM Link status | Preview — rolling out in batches | LM Studio page read |
| Open WebUI | ChatGPT-style interface over Ollama, browser-based | Stated in thread |
| Open WebUI access from laptop | `http://[desktop IP]:3000` | Stated in thread |

### `identity` — Hardware inventory (confirmed specs)

| Device | Spec | Value | Source |
|--------|------|-------|--------|
| Desktop | CPU | AMD Ryzen 7 7700X | User stated directly |
| Desktop | GPU | NVIDIA RTX 3060 12GB VRAM | User stated directly |
| Desktop | RAM | 64GB | User stated directly |
| Desktop | Location | Home — Lawrence, KS | User stated directly |
| Desktop | Setup status | Nothing installed as of 4/11/2026 | User stated directly |
| Laptop | GPU | Intel Iris Xe (integrated, no dedicated) | User confirmed |
| Laptop | RAM | 8GB | User stated directly |
| Laptop | OS | Windows | Confirmed via screenshots |
| iPhone | Model | iPhone 15 | User stated directly |
| iPhone | Storage | 128GB | User stated directly |
| iPhone | Setup status | Nothing done — starting from scratch | User stated directly |
| iPad | Generation | 5th gen, main model (not mini, not air) | User confirmed directly |
| iPad | Year | 2017 | User stated directly |
| iPad | Storage | 64GB | User stated directly |
| iPad | Chip | A9 (implied by 2017 5th gen model) | Inferred — FLAG for confirmation |
| iPad | Setup status | Spacedesk only — all else pending | User stated directly |
| External drive 1 | Size | 2TB — AI model storage | User stated directly |
| External drive 2 | Size | 1TB — footage/assets | User stated directly |

### `meta` — Naming convention rule

| Fact | Value | Source |
|------|-------|--------|
| Rule | Brand placeholder names NOT to be cemented in files, folders, or docs | User stated directly |
| Kray Studios | Provisional — do not use in file structure | User stated directly |
| Ctrl+You | Provisional — do not use in file structure | User stated directly |
| GLWC | Essentially decided — can be referenced directly | User stated directly |
| Functional alternatives | "Media Channel Project," "Online Business Project," "Union Project" | Stated in thread |

### `meta` — Current thinking/notes tools

| Fact | Value | Source |
|------|-------|--------|
| Primary thinking tool | Perplexity | User stated directly |
| Notes tools | Google Docs, Notes app (phone), Notes app (laptop) | User stated directly |
| Hugging Face account | Does not exist yet | User stated directly |

### `meta` — BrainOS full-circle confirmation

| Fact | Value | Source |
|------|-------|--------|
| This thread's significance | First thread to introduce Obsidian into the stack | User stated directly |
| Archival test | User uploaded all prior shortcut-generated threads to this space | User stated directly |
| Vault status | Does not exist — will be created fresh after Drive + Space org complete | User stated directly |
| Vault rebuild trigger | After all brain entries complete + Google Drive organized | User stated directly |

---

## TIMELINE MARKERS

- 4/5/2026 ~1:40 AM — Ollama installer downloaded on laptop
- 4/5/2026 ~1:44 AM — LM Studio 0.4.9 downloaded
- 4/5/2026 ~2:11 AM — "Thinking Mode.png" saved
- 4/5/2026 ~2:22 AM — Obsidian 1.12.7 downloaded
- 4/5/2026 ~2:34 AM — Test Vault folder created (throwaway)
- 4/5/2026 ~2:37 AM — LocalSend downloaded
- 4/5/2026 ~2:38 AM — Syncthing downloaded
- 4/5/2026 ~2:41 AM — Pinokio downloaded
- 4/5/2026 ~11:36–11:37 PM — Spacedesk drivers downloaded
- 4/7/2026 ~10:35 PM — Syncthing folder modified (active use)
- 4/11/2026 — User in Topeka, KS; interview questions answered
- 4/14/2026 — User in Lawrence, KS; thread continued
- 4/16/2026 2 AM CDT — Previous archival attempt begun (entry cut off)
- 4/16/2026 5 PM CDT — Full-circle archival test initiated; this entry

---

## UPDATES TO CANONICAL FILES

- **BRAYDEN-IDENTITY:** Add full confirmed hardware inventory table
  with all specs. Add desktop location. Add external drive assignments.
  Add current notes/thinking tools in use. Flag iPad A9 chip as
  inferred — confirm at compilation.

- **AI-WORKFLOW-RULES:** Add complete local tool stack. Add naming
  convention rule (no brand name cementing). Add local AI concepts
  glossary: inference, quantization (Q4/Q8), context window, tokens
  locally (zero cost), VRAM offloading, EOS token, parameters,
  diffusion model, checkpoint, LoRA. Add LM Link as laptop-to-desktop
  method. Add internet limitation note. Add document output via
  LibreOffice. Add Gemma 4 31B target model with full specs, pull
  command, settings, and behavior notes. Add image-before-text rule
  for multimodal prompting.

- **BRAINOS-SYSTEM:** Add vault rebuild protocol (8-step, fires after
  all entries done + Drive org complete). Add daily workflow pipeline
  (Capture → Process → Create → Publish). Add ADHD rules (single
  entry point, Daily note anchor, one-tap capture, if-it-feels-like-
  maintenance-cut-it). Add forward rules: how to add entries without
  confusion, how to modify canonical files, how to onboard new tools.

- **SKILLS-EDUCATION:** Add open-source AI vocabulary. Add confirmed
  tool knowledge from this thread. Add local model operation concepts.

- **KRAY-STUDIOS-CONTENT:** Add full creative pipeline. Add image
  stack (ComfyUI + Flux.1-schnell). Add video stack (Wan2GP, LTX).
  Add audio stack (Faster Whisper, MusicGen). Add Procreate →
  LocalSend → ComfyUI sketch-to-image pipeline.


- **NEW FILE — DEVICE-ECOSYSTEM.md:** Create this file. Contents:
  confirmed hardware specs per device, per-device role definitions,
  per-device setup checklists with current completion status,
  cross-device connectivity map (LocalSend / Syncthing / Möbius Sync /
  LM Link / Spacedesk), external drive assignments, Open WebUI
  remote access instructions, LM Link pairing steps.

---

## CONTRADICTIONS

- Cannot fully assess — thread is partially isolated from other entries.
  All items below flagged for compilation session review.

- **NAMING CONVENTION:** This thread establishes Kray Studios and
  Ctrl+You must not be cemented in file/folder names yet. If prior
  entries used these as primary identifiers in canonical file names
  or section headers, those references need audit.
  Prior state: UNKNOWN / This thread says: use functional descriptors
  until brand is launch-stable / Flag for Brayden to resolve.

- **VAULT STATUS:** This thread confirms no real vault exists. Test
  Vault is throwaway. If any prior entry described a vault as
  created, configured, or populated, this thread's state supersedes.
  Prior state: UNKNOWN / This thread says: no vault exists yet
  / Flag for Brayden to resolve.

- **iPAD MODEL:** Confirmed as 5th gen 2017 main model — not mini,
  not air. User confirmed directly when asked. If any prior entry
  named a different iPad model or generation, this supersedes.
  Prior state: UNKNOWN / This thread says: iPad 5th gen 2017 main
  / Flag for Brayden to resolve.

- **iPAD CHIP:** A9 chip noted as inferred from 2017 5th gen
  identification — NOT explicitly stated by user. Do not treat as
  confirmed fact. Flag for Brayden to verify.
  Prior state: UNKNOWN / This thread says: INFERRED ONLY
  / Flag for Brayden to confirm.

- **DEVICE SETUP STATUS:** If any prior entry described iPhone, iPad,
  or desktop as partially or fully configured, this thread resets:
  Desktop = fully pending. iPhone = zero. iPad = Spacedesk only.
  Prior state: UNKNOWN / This thread says: as stated above
  / Flag for Brayden to resolve.

- **OLLAMA INSTALL STATUS:** Installer was downloaded (confirmed via
  screenshot). Whether it was actually run and installed is not
  confirmed in this thread. Do not treat as installed.
  Prior state: UNKNOWN / This thread says: downloaded only, install
  unconfirmed / Flag for Brayden to verify current state.

---

## INSIGHTS & PATTERNS

- All five core laptop installs happened between 1:40 AM and 2:41 AM
  in a single uninterrupted burst. System design must support
  pick-up-anywhere resumption — no sequential dependency chains
  that require re-reading context to continue.

- Spacedesk was downloaded at 11:36 PM the same night — second
  burst after a gap. High-energy late-night work pattern is
  consistent. Tasks left mid-completion get returned to same night
  if motivation holds.

- User explicitly flagged past Perplexity systems failing due to
  unforeseen errors and clunky execution. The brain must be manually
  auditable and not collapse if one component is missing or wrong.

- User skips configuration steps that don't produce immediate visible
  output. LocalSend downloaded but not configured. Vault not created.
  Every setup task needs an immediate payoff moment or it stalls.

- User tested LM Studio the same session it was installed — curiosity
  and fast experimentation are strong. Tool onboarding is most
  effective when there is something to try right away.

- Naming convention rule was not pre-planned — it emerged organically
  from a question about brand names in this thread. Log as a standing
  rule. Do not pressure naming decisions in the brain system.

- User is withholding brand name commitments deliberately. This is
  healthy restraint. The brain system should use functional
  descriptors and let naming decisions come from the user unprompted.

- ADHD-relevant: user framed this entire project as "I hope this is
  the hardest part." Visible progress markers are important for
  sustained engagement. The compilation session should produce a
  clear artifact that demonstrates the system working — not just
  more files to manage.

- User's primary thinking surface is Perplexity, not a notes app.
  Obsidian will only become habitual if the entry point is
  frictionless. Daily note + one-tap is the minimum viable habit.

- This thread is the full-circle origin point: it introduced Obsidian,
  which became the storage layer for all of BrainOS. The project
  succeeded in building itself out of this conversation.

---

## TOOLS & RESOURCES REFERENCED

- Ollama | needs setup — install unconfirmed | Downloaded on laptop
  4/5/2026 1:40 AM. Must set OLLAMA_MODELS env var before first pull.
- LM Studio 0.4.9 | active | Installed, Gemma 3 1b running and tested
- Gemma 3 1b | active | 18.66 tok/sec on laptop CPU, text only
- Gemma 3 4b | needs setup | Vision capable, not yet downloaded
- Gemma 3n e2b | mentioned | Designed for phones/tablets — iPhone +
  iPad PocketPal model
- Gemma 4 31B Claude distill | mentioned — not downloaded | Target
  desktop deep-reasoning model. 18.7GB Q4_K_M. Apache 2.0.
- Obsidian 1.12.7 | needs setup | Installed, no vault created yet
- LocalSend 1.17.0 | needs setup | Downloaded, not configured
- Syncthing | active | Installed and running on laptop
- Pinokio | needs setup | Downloaded, not yet used
- Spacedesk | active | Installed, iPad second monitor confirmed working
- ComfyUI | mentioned | Install via Pinokio on desktop — pending
- Flux.1-schnell | mentioned | Best free image model, no watermarks.
  Download from Hugging Face to external drive.
- Wan2GP | mentioned | Best free video generator. Install via Pinokio.
- LTX Video | mentioned | Lighter/faster video alternative.
- Faster Whisper | mentioned | Voice transcription via Pinokio.
- MusicGen / AudioCraft | mentioned | Free local music + SFX.
- Open WebUI | mentioned | ChatGPT-style browser interface over Ollama.
  Deploy via Docker on desktop.
- Docker Desktop | mentioned | Required for Open WebUI deploy.
- LM Link | mentioned | Laptop borrows desktop GPU wirelessly.
  Preview status as of thread date.
- PocketPal AI | mentioned | Offline AI on iPhone 15 and iPad.
  Gemma 3n E2B recommended for both devices.
- Möbius Sync | mentioned | Syncthing client for iOS. Syncs KrayVault
  to iPhone and iPad silently.
- LibreOffice | mentioned — not installed | Free .docx and PDF output
  from model responses. Install on laptop and desktop.
- Hugging Face | needs setup | Account does not exist yet. Required
  for model downloads including Gemma 4 31B distill.
- n8n | mentioned — future | Automation pipeline. Not set up.
  Phase 2 desktop task.
- Smart Connections (Obsidian plugin) | mentioned — future | Enables
  RAG over Obsidian vault using local Ollama endpoint. Install after
  vault is created and desktop Ollama is running.

---

## OPEN QUESTIONS

- Has Ollama actually been installed (run) on the laptop, or just
  downloaded? User did not confirm execution.
- Is the iPad A9 chip correct? Inferred from 2017 5th gen — not
  stated explicitly. Affects PocketPal model size recommendations.
- PocketPal E2B confirmed for iPad — but will it actually run at
  acceptable speed on a 2017 chip? Needs real-world test.
- LM Link is in Preview status. Has access been granted? Is it
  usable now or still on waitlist?
- Hugging Face account: when will this be created? Gates Gemma 4 31B
  download and direct model browsing.
- LibreOffice: not yet installed on laptop. Simple 5-minute install —
  when is this getting done?
- LocalSend: downloaded but not configured. What is blocking this?
  It is a 2-minute task.
- Has the desktop been set up at all since April 11, 2026? User was
  in Topeka on that date and at home in Lawrence on April 14 and 16 —
  possible that desktop work has begun. Not confirmed in this thread.
- When does the vault rebuild session happen? User said after all
  brain entries are complete and Google Drive is organized. What is
  the current count of entries and how many threads remain?
- What is the current number of brain entries completed? Memory
  suggests at least 10, possibly more. Exact count not confirmed
  in this thread.

---

## CROSS-REFERENCES

Cross-references to be added during compilation session.

- Feeds into: AI-WORKFLOW-RULES, BRAINOS-SYSTEM, BRAYDEN-IDENTITY,
  SKILLS-EDUCATION, KRAY-STUDIOS-CONTENT, NEW: DEVICE-ECOSYSTEM
- Possible links to: any prior entry covering Obsidian introduction,
  device specs, or tool stack — confirm at compilation
- Note: This thread is the origin point of Obsidian in the stack.
  Any entry that references Obsidian as a tool traces back here.

---

## RAW HIGHLIGHTS

> "I don't want to hardlock myself with the placeholder names like
> Kray Studios or Ctrl+You" — user establishing naming convention
> rule, April 11, 2026

> "I hope this is the hardest, most time consuming part, going back
> and manually talking with this process, going through each thread,
> reading through the files you output to make sure they're accurate.
> I think this will be worth it in the end, I think it will work
> better with my ADHD, my temperament, my interests" — user on
> the investment framing of the whole project

> "This is a full-circle test, this is the thread that first gave
> me this idea" — user confirming this thread as the origin point
> of the BrainOS second brain project

> "I've been burned by systems built out in perplexity that have
> unforeseen errors and clunky execution" — standing warning; the
> system must be manually auditable and resilient

> "Let's just say nothing's been done, we'll start from the
> beginning for those systems" — on iPhone and iPad setup, April 11


STEP 3 — POST-ENTRY REPORT
1. Canonical files to update:
AI-WORKFLOW-RULES, BRAINOS-SYSTEM, BRAYDEN-IDENTITY, SKILLS-EDUCATION, KRAY-STUDIOS-CONTENT, and the new DEVICE-ECOSYSTEM.md file.

2. New file needed:
Yes — DEVICE-ECOSYSTEM.md. This thread generated enough per-device hardware specs, role definitions, setup checklists, and cross-device connectivity logic that fragmenting it across BRAYDEN-IDENTITY and BRAINOS-SYSTEM would lose coherence. It warrants its own canonical file. Contents: hardware inventory, device roles, completion-status checklists, sync configuration (Syncthing/LocalSend/Möbius Sync), Spacedesk notes, LM Link pairing, external drive assignments, Open WebUI remote access.

3. Potential conflicts to flag:

Any prior entry that says vault is created — this thread says no vault exists

Any prior entry with a different iPad model — this thread confirms 5th gen 2017 main

Any prior entry that lists Ollama as installed — this thread says downloaded only, install unconfirmed

Any prior entry using "Kray Studios" or "Ctrl+You" as structural identifiers — naming convention rule established here says not to cement those

iPad A9 chip is inferred, not confirmed — if any prior entry used a specific chip spec, compare carefully

4. Cross-reference tag:
BE-20260405-TOOL-local-ai-stack-device-ecosystem.md — Local AI stack built on laptop; full device ecosystem designed; Obsidian introduced; BrainOS origin thread
---


⚙️ This entry was generated in an isolated thread. Entry ID,
supersedes field, chronological position, and cross-references are
unconfirmed until the full compilation session. During that session:
assign IDs in date order, resolve contradictions, deduplicate facts
across entries, and push confirmed updates to canonical files.