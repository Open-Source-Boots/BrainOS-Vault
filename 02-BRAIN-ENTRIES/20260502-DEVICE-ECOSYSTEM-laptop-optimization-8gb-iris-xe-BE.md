---
title: Laptop Optimization for Local LLMs (8GB Iris Xe, Win10)
filename: 20260502-DEVICE-ECOSYSTEM-laptop-optimization-8gb-iris-xe-BE.md
date: 2026-05-02
domain: DEVICE-ECOSYSTEM
slug: laptop-optimization-8gb-iris-xe
status: ACTIVE
compilation_status: CURRENT
supersedes: ""
superseded_by: ""
canonical_file: DEVICE-ECOSYSTEM.md
tags:
  - brainos
  - device-ecosystem
  - laptop
  - performance
  - local-llm
  - windows10
  - optimization
open_questions:
  - id: OQ-20260502-001
    question: "Should DEVICE-ECOSYSTEM.md be updated to reflect that the laptop runs Windows 10 Pro 22H2 instead of Windows 11, and what exact OS build string should be recorded?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-002
    question: "What final, confirmed LM Studio advanced settings (context length, KV quantization, GPU offload, threads) are Brayden actually using on the laptop after this optimization session?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-003
    question: "Which specific local LLM model (name, size, quantization) runs reliably on the optimized laptop without crashes, and what tokens-per-second does it achieve on typical BrainOS workloads?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-004
    question: "Does the optimized laptop reach a stable idle memory usage below 40 percent after reboot, and what are the exact Task Manager Memory stats that should be recorded as canonical?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-005
    question: "Should BrainOS standardize the virtual memory settings on the laptop at 4–16 GB or at the classic 1.5x–3x RAM formula, and which choice is adopted as canonical for future reinstalls?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-006
    question: "Should Intelligent Standby List Cleaner (ISLC) be added to DEVICE-ECOSYSTEM.md as a required tool for the laptop, and if so, what exact threshold settings should be documented?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-007
    question: "Which vendor utilities and telemetry packages (Intel DSA, Lenovo Vantage, etc.) are now considered permanently uninstalled or disabled on all BrainOS devices to reduce RAM pressure?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-008
    question: "Does Brayden want a dedicated Windows user profile for LLM sessions with only BrainOS and LM Studio installed, and if so what should that account be named and how locked down should it be?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260502-009
    question: "What is the long-term OS plan for the laptop (stay on Windows 10, upgrade to Windows 11, or dual-boot with Linux Mint) in light of Windows 10 end-of-support and local LLM performance needs?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-010
    question: "Should Comet and Claude desktop apps be removed entirely on the laptop in favor of browser-only access to reduce background RAM footprint, or are there workflow reasons to keep them installed?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-011
    question: "How much VRAM and system RAM headroom does the future desktop workstation actually provide in practice once BrainOS is installed, and what class of local models should be standard there?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
---

## KEY FACTS

- The canonical “laptop” in DEVICE-ECOSYSTEM is now confirmed as an 11th Gen Intel Core i5‑1135G7 with 8 GB RAM, Intel Iris Xe integrated graphics, and a 477 GB NVMe SSD, running Windows 10 Pro 22H2 build 19045.6466 rather than Windows 11 as previously assumed.[file:19][conversation_history:1]  
- Idle memory usage before optimization hovered around 54–70 percent with Task Manager showing roughly 5.0 GB “In use” and only about 2.7 GB “Available,” which severely constrained local LLM loading on an 8 GB system.[conversation_history:1][web:85]  
- The running-processes list revealed that the Comet desktop app alone spawned 18 processes totaling roughly 1.6–1.7 GB of working set RAM, making it the single largest non-system consumer on the laptop.[conversation_history:1]  
- Intel Driver & Support Assistant services (DSAService, DSAUpdateService, ESRV_SVC_QUEENCREEK, esifsvc, telemetry) and Lenovo Vantage services (LenovoVantageService, ImControllerService, LITSSVC, multiple Vantage add‑ins) were consuming several hundred megabytes of RAM and running constantly in the background.[conversation_history:1]  
- Startup items included auto-launch for Steam, Discord, Riot Client, Epic Games Launcher, Claude desktop, Comet updater, Adobe updater, multiple Google Drive entries, and OneDrive setup/OneDrive.exe, all contributing to RAM and CPU usage without helping local LLM work.[conversation_history:1]  
- A PowerShell optimization script (brainos-laptop-optimize.ps1) was executed with elevated privileges, disabling or setting to manual many non-essential services, clearing startup Run entries for gaming launchers and cloud clients, hard-disabling OneDrive sync, and disabling transparency effects.[conversation_history:1]  
- Some protected services, namely GamingServices, GamingServicesNet, and DoSvc, resisted startup type changes with “Access is denied,” but these failures do not block the main optimization gains and can be tolerated.[web:102][web:108]  
- Virtual memory tuning was recommended for the laptop: placing the paging file on the NVMe SSD with a custom size of approximately 4–16 GB (or alternatively 1.5–3× RAM, e.g., 12–24 GB), ensuring sufficient swap space for LLM workloads without disabling paging entirely.[web:101][web:107]  
- Intelligent Standby List Cleaner (ISLC) was identified as an optional tool to manage standby memory, with safe 8 GB settings such as “Free memory is lower than 2048 MB,” “List size is at least 1024 MB,” and a custom standby list limit near 4096 MB.[web:99][web:100][web:97]  
- The canonical LM Studio laptop profile in DEVICE-ECOSYSTEM specifies CPU-only inference, context length 4096, zero GPU offload, one concurrent prediction, unified KV cache on, Q40 KV quantization, flash attention on, and “Keep model in memory” enabled, to keep total memory usage around 3.5 GB for a 7–9B Q4 model.[file:19]

## TIMELINE MARKERS

- 2022‑11‑14: Windows 10 Pro 22H2 originally installed on the laptop (per System info); this predates BrainOS but is relevant to OS support planning.[conversation_history:1]  
- 2026‑05‑02 (session start): Brayden notices Qwen 3.5 9B repeatedly failing to load, with LM Studio producing unknown error codes, and Task Manager showing unexpectedly high idle memory utilization.[file:19][conversation_history:1]  
- 2026‑05‑02: Running-processes, services, and startup lists are exported via PowerShell and analyzed, revealing Comet, Intel DSA, Lenovo Vantage, and gaming/launcher apps as major background consumers.[conversation_history:1]  
- 2026‑05‑02: brainos-laptop-optimize.ps1 is created and executed, attempting winget uninstalls for Intel DSA and Lenovo Vantage, disabling non-essential services, cleaning startup Run keys, and applying UX tweaks.[conversation_history:1]  
- 2026‑05‑02: Windows prompts for an execution policy change and the policy is set to RemoteSigned for the current user to allow the optimization script to run.[conversation_history:1]  
- 2026‑05‑02: Virtual memory settings dialog is opened, and new recommendations are given for a fixed paging file range on the C: NVMe drive to better support large local models.[web:101][web:107]  
- 2026‑05‑02: ISLC is discussed as a secondary optimization layer, but Brayden has not yet confirmed final ISLC configuration or adoption as canonical for the laptop.[web:99][web:100]

## UPDATES TO CANONICAL FILES

- **DEVICE-ECOSYSTEM.md** should be updated to correct the laptop OS from “Windows 11” to “Windows 10 Pro 22H2, OS build 19045.6466,” matching current System properties and clarifying support horizon for this node.[file:19][conversation_history:1]  
- The canonical LM Studio “Laptop – Advanced Settings” table already reflects the correct CPU-only, 4096-context, zero GPU layers, Q40 KV quantization configuration and should be confirmed as the standard baseline for all local LLM work on this machine; any deviations should be documented as experiments, not defaults.[file:19]  
- DEVICE-ECOSYSTEM.md should add explicit notes that Intel Driver & Support Assistant and Lenovo Vantage are considered non-essential, should remain uninstalled/disabled on the laptop, and are not part of the BrainOS stack on any device.[file:19][conversation_history:1]  
- The laptop section in DEVICE-ECOSYSTEM.md should emphasize that Comet and Claude desktop apps are substantial RAM consumers; for LLM sessions the recommended pattern is to close them and use browser access only, even if the applications remain installed for other tasks.[file:19][conversation_history:1]  
- DEVICE-ECOSYSTEM.md may need a short “Virtual Memory” row documenting the chosen paging file settings (initial and max size) as part of the laptop’s canonical configuration so future reinstalls can match today’s stable setup.[web:101][web:107]

## CONTRADICTIONS

- DEVICE-ECOSYSTEM currently implies that the laptop is running Windows 11, but System information confirms that it is actually running Windows 10 Pro 22H2 OS build 19045.6466; this is a direct contradiction that must be resolved in favor of the System info.[file:19][conversation_history:1]  
- The canonical laptop model section assumes that resource usage at the chosen LM Studio settings is around 3.55 GB and within an 8 GB envelope, but real-world measurements showed that additional bloat (Comet, Intel DSA, Lenovo Vantage, game launchers) pushed total usage high enough that Qwen 3.5 9B would not reliably load, indicating that the model settings alone were not sufficient without debloating the OS.[file:19][conversation_history:1]

## INSIGHTS & PATTERNS

- On an 8 GB Windows laptop, OS choice and background processes are as important as LM Studio settings: just one Electron desktop client (Comet) can consume as much memory as a 7–9B Q4_K_M model, effectively cutting available headroom in half.[conversation_history:1][web:88]  
- Vendor suites like Intel DSA and Lenovo Vantage, plus gaming launchers and cloud sync tools, can collectively consume well over a gigabyte of RAM while providing little or no value to BrainOS or local LLM workloads, making them high-leverage targets for removal.[conversation_history:1][web:88]  
- The access-denied errors for GamingServices and DoSvc show that not all services can be fully controlled via scripts on modern Windows, but selective trimming of what *can* be changed is still enough to materially improve memory headroom.[web:102][web:108]  
- Virtual memory is not optional for large local models on low-RAM machines; disabling or minimizing the pagefile is counterproductive when running 7–9B models, and a healthy SSD-based paging file acts as a safety net rather than a performance killer.[web:101][web:107]  
- ISLC and similar tools are secondary optimizations; the primary gains come from uninstalling and disabling large background consumers and correctly sizing the pagefile—only after those structural fixes is it worth fine-tuning standby memory behavior.[web:99][web:100]

## TOOLS & RESOURCES REFERENCED

- Windows Task Manager (Processes, Performance tabs) was used to inspect real-time CPU and RAM usage and to confirm the impact of individual processes like Comet and MsMpEng.[conversation_history:1]  
- PowerShell and built-in cmdlets (`Get-Process`, `Get-Service`, `Get-CimInstance Win32_StartupCommand`) generated machine-readable snapshots of running processes, services, and startup items for analysis.[conversation_history:1]  
- The `brainos-laptop-optimize.ps1` PowerShell script orchestrated service disabling, startup registry cleanup, OneDrive policy hardening, and minor UX tweaks, reducing manual configuration load.[conversation_history:1]  
- Microsoft and community documentation on paging file sizing and Windows 10 virtual memory behavior informed the recommended 4–16 GB or 12–24 GB custom size range for an 8 GB system.[web:101][web:107][web:110]  
- Guides and forum posts on Intelligent Standby List Cleaner provided safe baseline ISLC thresholds for 8 GB systems (2 GB free-memory trigger, 1 GB standby list minimum, ~4 GB custom limit) and clarified that stand‑by list management mainly helps with stutter and fragmentation rather than raw capacity.[web:96][web:99][web:100]

## CROSS-REFERENCES

- **BRAINOS-SYSTEM.md**: Should reference this entry as the origin of the first serious “device debloat” pass aimed at shifting the laptop from a general-purpose gaming/consumer profile to a BrainOS-first local LLM node.[file:21]  
- **ACTIVE-PROJECTS.md**: The CommonGrounds project relies on the laptop as the initial Whisper + Obsidian + LM Studio host; better LLM performance and stability directly support the CommonGrounds content and tooling roadmap.[file:13][file:17]  
- **BRAYDEN-IDENTITY.md**: Confirms that Brayden’s local-first, open-source bias and desire to avoid SaaS lock-in are part of the motivation for investing in a well-tuned local AI stack despite hardware constraints.[file:23]  
- **COMMONGROUNDS-PROJECT.md**: Describes Whisper-on-laptop as the Phase 1 gate for content creation; this optimization session is a prerequisite for stable transcription and local-model assisted scripting.[file:13]  
- **DEVICE-ECOSYSTEM.md**: Remains the canonical home for all device specs and should be updated with the corrected OS, service state, and any finalized ISLC and paging file settings that emerge from follow-up testing.[file:19]

## RAW HIGHLIGHTS

- Confirmed laptop specs: Intel Core i5‑1135G7 (4 cores/8 threads), 8 GB RAM, Intel Iris Xe integrated GPU, 477 GB NVMe SSD, Windows 10 Pro 22H2 OS build 19045.6466.[conversation_history:1]  
- Task Manager showed around 5.0 GB in use, 2.7 GB available, and 54–70 percent memory usage at idle before optimization, despite only a few visible apps being open.[conversation_history:1]  
- Comet desktop app alone ran 18 processes totaling ~1.6–1.7 GB working set, rivaling or exceeding the footprint of a 7–9B local model.[conversation_history:1]  
- Intel DSA and Lenovo Vantage services and add-ins consumed hundreds of megabytes and were judged non-essential for Brayden’s BrainOS use-case.  
- Startup included Google Drive FS multiple times, OneDrive setup and OneDrive.exe, Steam, Discord, Epic Games, Riot, Claude desktop, Comet updater, Adobe updater, and system tray items.  
- brainos-laptop-optimize.ps1: set execution policy, attempted winget uninstalls, disabled/Manual’d a long list of services, removed startup entries via Run key matching, and hardened OneDrive disablement.  
- Some services (GamingServices, GamingServicesNet, DoSvc, OneSyncSvc_77681) returned “Access is denied” or “parameter is incorrect” when PowerShell attempted to change startup types, but the script continued.  
- Virtual memory configuration dialog was opened for the C: NVMe SSD, and recommendations were given to set a sizeable fixed or semi-fixed paging file rather than relying on defaults or disabling it.  
- ISLC was introduced as a way to sweep standby memory when free memory falls below a threshold and the standby list grows, with conservative 8 GB settings sketched for later adoption.  
- Qwen 3.5 9B remains a stretch target on 8 GB; the realistic expectation is that 3–7B Q4_K_M models will feel substantially more stable, and heavier models may still require closing Comet and other Electron apps during LLM sessions.[file:19][web:86]