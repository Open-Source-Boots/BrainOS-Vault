date_logged: 2026-04-16
source_thread_date: 2026-03-10
source_thread_title: "Explain exactly how to use and what to avoid for each piece that came with my Bambu Labs P1S."
entry_type: TOOL
chronological_position: UNKNOWN — to be placed during Obsidian compilation session
status: draft
supersedes: UNKNOWN — cannot confirm without seeing other entries
superseded_by: none
canonical_file: NEW FILE — HARDWARE-AND-TOOLS
context_available: none — isolated thread
tags: [bambu-lab, p1s, 3d-printer, maintenance, lubrication, hotend, extruder, hardware, tools]
```

***

# Brain Entry — Bambu Lab P1S Maintenance Kit: Full Usage Guide and Axis Lubrication Rules

## CONFIRMED FACTS

- **Printer owned:** Bambu Lab P1S | confirmed | user photo + query
- **Maintenance kit included in box** with the following confirmed items:
  - Bambu Lab Thermal Paste (silver foil packet, thermal conductivity: 2W/m·K) | confirmed | user photo
  - Bambu Lab Lubricant Grease (white tube, 3g) | confirmed | user photo
  - "For Extruder" bag — contains small replacement screws | confirmed | user photo
  - "For Hot End" bag — contains nozzle, silicone sock, thermistor clip, hardware | confirmed | user photo
  - Cleaning/nozzle needle (thin metal pin) | confirmed | user photo
  - Allen/hex L-key | confirmed | user photo
  - "For Scraper" bag — contains replacement silicone/rubber nozzle wiper blade | confirmed | user photo
  - Black rectangular foam/pad (likely purge chute gasket or toolhead pad) | confirmed | user photo

***

### Thermal Paste Rules
- Apply into groove on nozzle where ceramic heater sits | confirmed | AI response citing Bambu wiki
- Apply a small dab inside the thermistor hole before inserting thermistor | confirmed | AI response
- Use foil packet itself as spreader | confirmed | AI response
- To remove old hotend: apply a few drops of IPA to old thermal paste, wait 5 minutes to soften before pulling | confirmed | AI response citing Bambu wiki
- **Avoid:** applying too little (causes poor heat transfer and temperature errors); letting it cure before seating components | confirmed | AI response

***

### Lubricant Grease (3g tube) Rules
- ✅ **Correct uses:** Z-axis lead screws, extruder gear teeth | confirmed | AI response citing Bambu P1 maintenance wiki
- ❌ **Do NOT use on:** X-axis carbon rods, Y-axis linear rods, idler pulleys | confirmed | AI response citing Bambu P1 maintenance wiki
- Z-axis application: apply with bed at home position, lower bed, apply again to newly exposed sections, run bed up/down to spread | confirmed | AI response
- Extruder gears: tiny amount on gear contact points only; wipe off excess to prevent filament path contamination | confirmed | AI response

***

### X-Axis (Carbon Rods) Rules
- Requires **zero lubrication** | confirmed | Bambu P1 wiki via AI response
- Clean with dry or IPA-dampened lint-free cloth only | confirmed | Bambu P1 wiki
- **Explicit Bambu warning:** "Do not use grease on the carbon rods, as it will cause abnormal resistance and difficulty in cleaning." | confirmed | direct quote from Bambu wiki

***

### Y-Axis (Linear Rods) Rules
- Uses 8mm steel linear rods with LMU8 bearings | confirmed | AI response citing Bambu wiki
- Requires **lightweight oil**, NOT grease | confirmed | Bambu P1 wiki via AI response
- Recommended product: **Super Lube 52004 Synthetic Lightweight Oil** | confirmed | Bambu P1 wiki
- Clean with IPA first, then immediately apply thin oil coat | confirmed | Bambu wiki
- **Critical warning:** If you clean with IPA and skip the oil step, the rods will rust | confirmed | Bambu wiki
- Move bed back and forth manually after oiling to work oil into bearings | confirmed | Bambu wiki

***

### Nozzle Wiper / Scraper Blade Rules
- Slides off and on the mount, no tools needed | confirmed | AI response
- Replace when torn, deformed, or heavily gunked | confirmed | AI response
- **Do NOT clean with IPA** — IPA degrades silicone/rubber over time, causing cracking and brittleness | confirmed | AI response

***

### IPA (Isopropyl Alcohol) — Where Safe vs. Unsafe on P1S
- ✅ Safe on: carbon/linear rods (before re-oiling), build plate, hotend exterior (removing old thermal paste) | confirmed | AI response
- ❌ Not safe on: silicone wiper blade, rubber components | confirmed | AI response

***

### Nozzle / Hotend Rules
- Always heat nozzle to ~200°C before removing — never remove cold | confirmed | AI response
- Use Allen key from kit to secure hotend mounting screws | confirmed | Bambu wiki
- Replace silicone sock when cracked, burned, or heavily built up | confirmed | AI response

***

### Cleaning Needle Rules
- Insert into nozzle tip only when nozzle is at print temperature | confirmed | AI response
- Never insert into cold nozzle — will bend needle or damage bore | confirmed | AI response
- For stubborn clogs, do a cold pull instead of forcing needle | confirmed | AI response

***

## TIMELINE MARKERS

- 2026-03-10 — User photographed and queried Bambu P1S maintenance kit contents (Thread Message 1)
- 2026-03-10 — User asked follow-up about using grease on X/Y axis, referencing Bambu Lab P2S maintenance wiki (Thread Message 2)
- 2026-04-16 — Thread archived into BrainOS

***

## UPDATES TO CANONICAL FILES

- **NEW FILE — HARDWARE-AND-TOOLS:** Create this file. Add Bambu Lab P1S as confirmed owned hardware. Log all maintenance kit items with their use/avoid rules. Log axis lubrication matrix (see confirmed facts). Add Super Lube 52004 as a needed consumable to acquire.
- **BRAYDEN-IDENTITY:** Minor optional note — Brayden owns a Bambu Lab P1S 3D printer as of March 2026. Only add if identity file tracks owned equipment.
- **SKILLS-EDUCATION:** Optional — basic 3D printer maintenance knowledge is now documented. Could be logged as a practical hardware skill.

***

## CONTRADICTIONS

Cannot assess — thread is isolated. Flag for review during compilation.

- No prior references to a 3D printer were visible in this thread. If another thread elsewhere establishes different lubrication rules or a different printer model, flag for Brayden to resolve.

***

## INSIGHTS & PATTERNS

- Brayden is hands-on with hardware and performs his own printer maintenance — aligns with self-sufficiency pattern seen elsewhere in BrainOS
- Brayden referenced a P2S wiki page for his P1S printer — worth flagging that P1S and P2S wiki pages differ; always verify the correct model page
- The grease-vs-oil distinction is a common mistake; Bambu explicitly warns against it — encode this as a standing rule in HARDWARE-AND-TOOLS so it is never misapplied
- "AI writes structure, Brayden fills numbers" applies here too — maintenance frequency intervals were not confirmed in this thread and should not be assumed

***

## TOOLS & RESOURCES REFERENCED

- Bambu Lab P1S | active — owned hardware | 3D printer, subject of entire thread
- Bambu Lab Lubricant Grease 3g | active — in kit | Z-axis lead screws and extruder gears only
- Bambu Lab Thermal Paste | active — in kit | hotend ceramic heater and thermistor application
- Super Lube 52004 Synthetic Lightweight Oil | mentioned — needs to be purchased | Y-axis linear rods and idler pulleys
- Bambu Lab P1 Maintenance Wiki (wiki.bambulab.com/en/p1/maintenance/p1p-maintenance) | active source | confirmed as primary reference for P1S maintenance
- Bambu Lab P2S Maintenance Wiki (wiki.bambulab.com/en/p2s/maintenance/period-maintenance) | mentioned — use with caution | User referenced this; may differ from P1S specs, verify before applying

***

## OPEN QUESTIONS

- What is the correct maintenance interval for each task on the P1S (Z-axis grease, extruder cleaning, wiper replacement)? Not stated in this thread.
- Has Brayden acquired Super Lube 52004 for the Y-axis rods? Not confirmed.
- What filament types does Brayden primarily print? Not stated — relevant to nozzle wear and maintenance frequency.
- What is the black rectangular foam pad specifically? Identified tentatively as a purge chute gasket but not confirmed by Bambu documentation in this thread.
- Does Brayden have an AMS unit with this P1S? Not mentioned — would add additional maintenance items.

***

## CROSS-REFERENCES

Cross-references to be added during compilation session.
- Feeds into: NEW FILE — HARDWARE-AND-TOOLS, optionally BRAYDEN-IDENTITY, optionally SKILLS-EDUCATION
- Possible links to: foam sculpting / fabrication thread (BEUNASSIGNED_20260416_SKILL_foam-sculpting-finishing-reference.md) — both involve physical/maker tools; may be worth grouping in a MAKER-SKILLS section

***

## RAW HIGHLIGHTS

> "Do not use grease on the carbon rods, as it will cause abnormal resistance and difficulty in cleaning." — Bambu Lab official wiki, quoted in AI response

> "If you clean with IPA and skip the oil step, the rods will rust." — AI response citing Bambu P1 maintenance wiki

> "Can I clean this black part in the printer with iso alcohol?" — Brayden, Thread Message 1 (referring to silicone wiper blade)

> "Do not use the grease tube on your X or Y axis linear rods. The grease is specifically for the Z-axis lead screws and extruder gears only." — AI response, Thread Message 2

***

## STEP 3 — Post-Entry Report

**1. Canonical files to update:**
- **NEW FILE — HARDWARE-AND-TOOLS** is the primary target. This thread alone justifies creating it.
- **BRAYDEN-IDENTITY** — optional one-liner noting P1S ownership.

**2. New file warranted?**
Yes. `HARDWARE-AND-TOOLS.md` — would cover: owned physical equipment, maintenance schedules, product-specific rules (lubrication matrices, cleaning restrictions), consumables to stock, and repair/replacement logs. No existing canonical file covers this domain.

**3. Potential conflicts to flag:**
- The user referenced the **P2S** maintenance wiki for a **P1S** printer. If any other thread or canonical file records maintenance procedures sourced from the P2S wiki, those rules should be cross-checked against the P1S wiki before being encoded as standing rules.
- No financial data in this thread to conflict with FINANCIAL-SNAPSHOT.

**4. One-line cross-reference tag:**
`BE-20260310-TOOL-p1s-maintenance-kit-rules` — Bambu Lab P1S maintenance kit usage guide, axis lubrication matrix, and IPA safety rules.

***

## STEP 4 — File Name

```
BE-20260310-TOOL-p1s-maintenance-kit-rules.md
```