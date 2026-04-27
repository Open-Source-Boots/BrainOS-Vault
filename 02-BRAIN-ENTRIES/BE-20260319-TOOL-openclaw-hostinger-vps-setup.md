---
filename: BE-20260319-TOOL-openclaw-hostinger-vps-setup.md
thread_date: 2026-03-19
domain: BRAINOS-SYSTEM
status: SUPERSEDED
priority: 3
compilation_status: pending
supersedes: none
superseded_by: none
canonical_file: BRAINOS-SYSTEM.md
generated_by_skill: manual
tags: []
notes: Hostinger VPS is a real owned asset — confirm it's not sitting idle
open_questions:
  - id: OQ-20260319-001
    question: "Confirm if OpenClaw ever deployed"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260319-002
    question: "confirm if VPS is being used for n8n or other tools"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
---
date_logged: 2026-04-16
source_thread_date: 2026-03-19
source_thread_title: "trying to deploy open claw on my hostinger vps, do I have any of these credentials?"
entry_type: tool / project
chronological_position: UNKNOWN — to be placed during Obsidian compilation session
status: draft
supersedes: UNKNOWN — cannot confirm without seeing other entries
superseded_by: none
canonical_file: AI-WORKFLOW-RULES (primary); SELF-HOSTED-INFRA (proposed new file)
context_available: image.jpg (screenshot of OpenClaw deploy form on Zeabur/Hostinger interface) — attached in thread; no other files or prior entries visible
tags: [openclaw, vps, hostinger, self-hosting, AI-tools, free-tier, api-keys, docker, ollama, model-providers]
Brain Entry — Brayden explored deploying OpenClaw on Hostinger VPS; assessed credentials and free model options
CONFIRMED FACTS
Only facts explicitly stated in this thread. Nothing inferred.

OpenClaw is a personal AI assistant that runs on your own devices and supports multi-channel messaging | Confirmed | User's screenshot and Perplexity response

OpenClaw was formerly called Moltbot/Clawbot | Confirmed | Screenshot label in attached image

OpenClaw integrates with WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Microsoft Teams, and other channels | Confirmed | Screenshot description visible in image

The OpenClaw deploy form requires: Gateway Token, Anthropic API Key, OpenAI API Key, Gemini API Key, X API Key, WhatsApp number, Telegram bot token | Confirmed | User's attached screenshot

Brayden has a Hostinger VPS | Confirmed | User's explicit statement in thread

The Gateway Token is NOT provided by Hostinger — it is set by OpenClaw itself and must be manually configured in openclaw.json under "auth": {"mode": "token", "token": "..."} or via a Docker environment variable OPENCLAW_GATEWAY_TOKEN | Confirmed | Perplexity response citing OpenClaw docs and Hostinger docs

Anthropic, OpenAI, and Gemini API keys are NOT included through a Perplexity subscription | Confirmed | Perplexity response

Those API keys are created separately at each provider's dashboard (console.anthropic.com, platform.openai.com, aistudio.google.com/api-keys) | Confirmed | Screenshot field labels + Perplexity response

Brayden does NOT appear to have any of these API keys on record as of this thread | Confirmed | Memory search returned no stored credentials

X API Key is for Grok AI models (from console.x.ai) | Confirmed | Screenshot field label

WhatsApp number format expected: +1234567890 (with country code) | Confirmed | Screenshot placeholder text

Telegram bot token is obtained by talking to @BotFather in Telegram | Confirmed | Perplexity response

OpenClaw is available as a Docker template deployable on Zeabur (template ID VTZ4FX confirmed in search) | Confirmed | Web search result

OpenClaw supports an ollama provider — runs local models on your VPS with no API key and zero per-token cost | Confirmed | Perplexity response citing OpenClaw docs (fossies.org mirror)

OpenClaw supports Qwen OAuth device-code login — provides access to coder/vision models with a daily free quota, no API key needed | Confirmed | Perplexity response citing OpenClaw docs

Free-tier options also available via OpenRouter (":free" models) and Groq | Confirmed | Perplexity response citing multiple sources

Flagship API models (OpenAI, Anthropic, Gemini) cost low-to-mid single-digit dollars per million input tokens | Confirmed | Perplexity response citing pricing sources

OpenClaw's provider system allows routing different channels to different models/providers | Confirmed | Perplexity response citing OpenClaw docs

Hostinger VPS credentials Brayden has (or can access from hPanel): VPS IP address, root username/password or SSH key, possibly a control panel login URL | Confirmed | Perplexity response

TIMELINE MARKERS
2026-03-19 — Brayden first explored deploying OpenClaw on Hostinger VPS (this thread)

2026-03-19 — Brayden did not yet have any AI provider API keys as of this date (no memory record found)

Thread ended without Brayden confirming which install method he would use (Docker template, plain Docker, or bare binary); Perplexity asked but user did not respond within this thread

UPDATES TO CANONICAL FILES
AI-WORKFLOW-RULES: Add OpenClaw as a tracked AI tool. Log that Brayden is exploring self-hosting it on Hostinger VPS. Note: no paid API keys exist as of 2026-03-19. Preferred free-tier strategy identified: Qwen OAuth or Ollama (local), with OpenRouter ":free" models as secondary option.

SELF-HOSTED-INFRA (proposed new file): Create this file. First entry: Hostinger VPS — active. OpenClaw deployment — in progress as of 2026-03-19, install method unconfirmed. Gateway Token — not yet set. All AI provider API keys — not yet created. Ollama — not yet installed.

CONTRADICTIONS
Cannot assess — thread is isolated. Flag for review during compilation.

Note: Memory search run during this thread returned no record of any Hostinger VPS, OpenClaw, or AI API keys. This is consistent with this being a first-mention thread. No contradiction found, but verify against any infra-adjacent entries (n8n, Docker, automation entries) during compilation.

INSIGHTS & PATTERNS
Brayden has a pattern of exploring self-hosted AI tools that reduce ongoing SaaS costs — OpenClaw follows the same logic as n8n.

Brayden is budget-conscious about API costs; the free-first approach was confirmed as the direction without hesitation.

Brayden does not yet have any paid AI API accounts — this is a potential gap if any tool or workflow later assumes he does.

The thread ended at a decision point (which install method) — this is a common drop-off pattern; worth flagging as an open loop.

OpenClaw's multi-channel nature aligns with Brayden's existing multi-platform communication needs (WhatsApp, Telegram mentioned in earlier automation work).

TOOLS & RESOURCES REFERENCED
OpenClaw | active (exploring deployment) | Formerly Moltbot/Clawbot; personal AI assistant with multi-channel messaging

Hostinger VPS | active | Brayden owns one; login credentials exist in hPanel

Zeabur | mentioned | Hosts an OpenClaw Docker template (VTZ4FX); may not be relevant if deploying directly on Hostinger

Ollama | mentioned — needs setup | Would run local models on the VPS; free, no API key required

Qwen OAuth (OpenClaw provider) | mentioned — needs setup | Free daily quota; device-code auth; no API key

OpenRouter (":free" models) | mentioned | Free API keys available for low-cost model routing in OpenClaw

Groq | mentioned | Free-tier inference; can be wired into OpenClaw

@BotFather (Telegram) | mentioned | Required to generate Telegram bot token if Telegram channel is configured

WhatsApp Cloud API | mentioned | Required if WhatsApp channel is configured in OpenClaw

OpenAI / Anthropic / Gemini / X.ai | mentioned — not yet set up | All require separate paid/trial accounts; no keys exist as of 2026-03-19

console.anthropic.com | source | Where Anthropic API keys are generated

platform.openai.com | source | Where OpenAI API keys are generated

aistudio.google.com/api-keys | source | Where Gemini API keys are generated

console.x.ai | source | Where X/Grok API keys are generated

OPEN QUESTIONS
Which install method will Brayden use for OpenClaw on Hostinger VPS? (Docker marketplace template, plain Docker + GitHub clone, or bare binary — never answered in this thread)

Will Brayden start with Ollama (local) or a free cloud provider (Qwen/OpenRouter)?

Does Brayden's Hostinger VPS have enough RAM/CPU to run Ollama models locally at useful speed?

Will Brayden ever create a paid API key for any provider, and if so, which one and when?

Has Brayden actually logged into his Hostinger hPanel and confirmed VPS is running/accessible?

Which messaging channel does Brayden actually want to use OpenClaw with — WhatsApp, Telegram, or another?

CROSS-REFERENCES
Cross-references to be added during compilation session.

Feeds into: AI-WORKFLOW-RULES, SELF-HOSTED-INFRA (proposed)

Possible links to: n8n automation entries (shared pattern of self-hosted free tools), KRAY-STUDIOS-CONTENT or CTRL-YOU-STATUS (if OpenClaw is later used to automate messaging for those projects), any entry mentioning Hostinger or VPS

RAW HIGHLIGHTS
"trying to deploy open claw on my hostinger vps, do I have any of these credentials?" — User's opening question; establishes this as a first-touch exploration thread

"Through perplexity, do I have anthropic, openai, or gemini api keys? Do these cost money to work within openclaw? What's the most free and most effective way to use open claw?" — User's second question; confirms no prior API key setup and explicit free-first priority

"You do not get Anthropic, OpenAI, or Gemini API keys through Perplexity; those are separate accounts and keys you create directly with each provider" — Perplexity response; key clarification worth preserving

"On a plain Hostinger VPS you only start with server access (IP, root username/password or SSH key); you do not automatically have any of the OpenClaw API keys, bot tokens, or gateway token shown in that form." — Perplexity response; defines what Hostinger actually gives you