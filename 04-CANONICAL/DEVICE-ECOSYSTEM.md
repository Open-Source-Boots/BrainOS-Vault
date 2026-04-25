---
title: Device Ecosystem
filename: DEVICE-ECOSYSTEM.md
updated: 2026-04-25
status: CANONICAL
domain: BRAINOS-SYSTEM
---

# 🖥️ Device Ecosystem — Brayden Boots

## Hardware Inventory

| Device | Specs | Status |
|---|---|---|
| Desktop | AMD Ryzen 7 7700X, RTX 3060 12GB VRAM, 64GB RAM, Windows 11 | Owned — nothing installed for BrainOS yet |
| Laptop | Intel Iris Xe integrated, 8GB RAM, Windows | Primary BrainOS device |
| iPhone 15 | 128GB | Obsidian node live via Möbius Sync |
| iPad 5th gen (2017) | 64GB, A9 chip (assumed — not mini or air) | Spacedesk working as second monitor; some apps installed |
| External HDD 1 | 2TB | AI model storage (designated) |
| External HDD 2 | 1TB | Footage / assets |
| Bambu Lab P1S | 3D printer, currently 0.4mm nozzle | Located in bedroom on floor |
| 2015 Honda CRV | Primary vehicle, owned by Brayden | Payments to mom $350/mo |
| Toyota Sienna WAV | Wheelchair-accessible van | Purchased ~March 25, 2026 — Allstate $253.95/mo |

## Software Installed — Laptop (Primary)

| Software                 | Status                  | Notes                                          |
| ------------------------ | ----------------------- | ---------------------------------------------- |
| Obsidian 1.12.7          | ✅ Installed             | Real vault live, past test stage               |
| LM Studio 0.4.9          | ✅ Installed             | Gemma 3 1b tested at 18.66 tok/sec             |
| Ollama                   | ✅ Installed             | Confirmed installed, not fully configured      |
| n8n v2.17.6              | ✅ Installed             | Local REST API active — zero workflows built   |
| Node.js                  | ✅ Installed             | Required for n8n                               |
| Git                      | ✅ Installed             | Auto-commit every 10 min, auto-pull on boot    |
| Obsidian Git plugin      | ✅ Confirmed operational |                                                |
| Google Drive for Desktop | ✅ Active                | Replaced OGD Sync plugin — file moves now work |
| Syncthing                | ✅ Downloaded            | Not fully configured                           |
| LocalSend                | ⚠️ Installed            | Not configured                                 |
| Spacedesk                | ✅ Working               | iPad as second monitor confirmed               |
| PocketPal                | ✅ iPhone                | Qwen 2.5 installed                             |
| Möbius Sync              | ✅ Active                | iPhone Obsidian sync confirmed                 |
| LibreOffice              | ⚠️ Installed            | Any device                                     |
| ComfyUI                  | ❌ Not installed         | Planned for desktop                            |

## Desktop — Nothing Installed Yet
Desktop is owned and powered — no BrainOS software installed as of April 25, 2026.
First install priority when ready: Ollama → LM Studio → Obsidian → Git → n8n (point to existing laptop workflows).

## VPS (Hostinger)
- Owned, active subscription (less than 1 year remaining)
- **Nothing deployed** — no OpenClaw, no n8n, no Ollama
- Brayden does not want to renew — looking for local/self-hosted replacements
- Do not build workflows that depend on this VPS

## API Keys & Credentials
- No API keys created as of April 17, 2026
- GitHub PAT: iPhone PAT expires May 22, 2026 — renew before that date
- No paid AI subscriptions active beyond Perplexity