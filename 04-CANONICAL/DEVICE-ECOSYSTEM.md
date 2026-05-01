---
title: Device Ecosystem
filename: DEVICE-ECOSYSTEM.md
updated: 2026-05-01
status: CANONICAL
domain: BRAINOS-SYSTEM
---

# 🖥️ Device Ecosystem — Brayden Boots

## Hardware Inventory

| Device                   | Specs                                                                          | Status                                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Desktop                  | AMD Ryzen 7 7700X, RTX 3060 12GB VRAM, 64GB RAM, Windows 11                    | Owned — nothing installed for BrainOS yet. When setup is done, this will be the 1st highest-priority device   |
| Laptop                   | Intel Core i5-1135G7 @ 2.40GHz, Intel Iris Xe integrated GPU, 8GB RAM, Windows | Hostname: DESKTOP-QS71AHN.<br>Once desktop is established, the laptop will be the 2nd highest-priority device |
| iPhone 15                | 128GB                                                                          | Obsidian node live via Möbius Sync; 3rd highest-priority device                                               |
| iPad Air (5th gen, 2017) | 64GB, A9 chip (assumed — not mini or air)                                      | Spacedesk working as second monitor; some apps installed; will always be the 4th highest-priority device      |
| External HDD 1           | 2TB                                                                            | Undetermined purpose at this time                                                                             |
| Bambu Lab P1S            | 3D printer, currently 0.4mm nozzle                                             | Located in bedroom on floor                                                                                   |
| 2015 Honda CRV           | Primary vehicle, owned by Brayden                                              | Payments to mom $350/mo, but owned. There is a lien on this vehicle for the OneMain loan                      |
| Toyota Sienna WAV        | Wheelchair-accessible van                                                      | Purchased ~March 25, 2026 — Allstate $253.95/mo on the 30th/31st of each month                                |

---

## Software Installed — Laptop (Primary)

| Software                 | Status                  | Notes                                                                                                 |
| ------------------------ | ----------------------- | ----------------------------------------------------------------------------------------------------- |
| Obsidian 1.12.7          | ✅ Installed             | Real vault live, past test stage                                                                      |
| LM Studio 0.4.9          | ✅ Installed             | See LM Studio section below for models and settings                                                   |
| Ollama                   | ✅ Installed             | Confirmed installed, not fully configured                                                             |
| n8n v2.17.6              | ✅ Installed             | Local REST API active — zero workflows built                                                          |
| Node.js                  | ✅ Installed             | Required for n8n                                                                                      |
| Git                      | ✅ Installed             | Auto-commit every 10 min, auto-pull on boot                                                           |
| Obsidian Git plugin      | ✅ Confirmed operational |                                                                                                       |
| Google Drive for Desktop | ✅ Active                | Replaced OGD Sync plugin — file moves now work                                                        |
| Syncthing                | ✅ Active                | Not fully configured on Desktop and iPad. iPhone and Laptop are already synced, working well together |
| LocalSend                | ⚠️ Installed            | Not configured                                                                                        |
| Spacedesk                | ✅ Working               | iPad as second monitor confirmed                                                                      |
| PocketPal                | ✅ iPhone                | Qwen 2.5 installed                                                                                    |
| Möbius Sync              | ✅ Active                | iPhone Obsidian sync confirmed                                                                        |
| LibreOffice              | ⚠️ Installed            | Installed only to laptop currently, no setup yet                                                      |
| ComfyUI                  | ❌ Not installed         | Planned for desktop                                                                                   |

---

## LM Studio — Laptop

### Installed Models (as of 2026-05-01)

| Model                | Quantization             | Use Case                                                      | Status      |
| -------------------- | ------------------------ | ------------------------------------------------------------- | ----------- |
| Gemma 4 E4B Instruct | Q4_K_M                   | General BrainOS sessions, reasoning, future multimodal        | ✅ Installed |
| Qwen 3.5 9B          | Q4_K_M                   | Structured output — mdfinancial, mdlegal, document extraction | ✅ Installed |

**Primary model for structured tasks:** Qwen 3.5 9B Q4_K_M
**Primary model for general sessions:** Gemma 4 E4B Instruct Q4_K_M

---

### LM Studio Advanced Settings — Laptop Canonical Config

These are the confirmed optimized settings for running local models on the laptop
(8GB RAM, Intel Iris Xe integrated GPU, no discrete VRAM).
Do not exceed these without confirming available memory first.

| Setting | Canonical Value | Notes |
|---|---|---|
| Context Length | 4,096 | Single biggest memory driver. 4k covers all BrainOS tasks. 8k max if needed for long docs. |
| GPU Offload Layers | 0 | Iris Xe is integrated — shares system RAM. Offloading does not free memory. Run fully on CPU. |
| CPU Thread Pool Size | 4 | Set to logical cores minus 1. Confirm in Task Manager → Performance → Logical processors. |
| Evaluation Batch Size | 128 | Larger = faster but more RAM. 128 is the 8GB sweet spot. |
| Max Concurrent Predictions | 1 | Solo use only. Each additional multiplies KV cache usage. |
| Unified KV Cache | On | Required for integrated GPU setup. |
| RoPE Frequency Base | Auto | Correct for Qwen 3.5 and Gemma 4. Do not override. |
| RoPE Frequency Scale | Auto | Correct for Qwen 3.5 and Gemma 4. Do not override. |
| Offload KV Cache to GPU | Off | Integrated GPU — no benefit, adds overhead. |
| Keep Model in Memory | On | Prevents reload penalty between sessions. |
| Try mmap() | On | Memory-mapped loading — more efficient on low-RAM systems. |
| Flash Attention | On | Reduces attention memory footprint. Critical on 8GB. Keep on. |
| K Cache Quantization | Q4_0 | Cuts KV cache memory by ~50-75%. Second biggest memory lever after context length. |
| V Cache Quantization | Q4_0 | Apply same as K cache. |
| Random Seed | Random | No change needed. |

**Estimated memory usage at these settings:** ~3.5–5GB (within 8GB ceiling with OS headroom)
**Previous misconfigured usage:** 16.80GB (context 262k, 13 GPU layers, no KV quantization — do not use)

---

## Desktop — Nothing Installed Yet

Desktop is owned and powered — no BrainOS software installed as of April 25, 2026.
Hostname: unknown (confirm when first accessed).
First install priority when ready: Ollama → LM Studio → Obsidian → Git → n8n (point to existing laptop workflows).

---

## VPS (Hostinger)
- Owned, active subscription (less than 1 year remaining)
- **Nothing deployed** — no OpenClaw, no n8n, no Ollama
- Brayden does not want to renew — looking for local/self-hosted replacements
- Do not build workflows that depend on this VPS

---

## API Keys & Credentials
- No API keys created as of April 17, 2026
- GitHub PAT: iPhone PAT expires **May 22, 2026** — renew before that date
- No paid AI subscriptions active beyond Perplexity
