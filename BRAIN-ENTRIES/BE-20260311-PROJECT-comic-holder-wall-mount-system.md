---
date_logged: 2026-04-16
source_thread_date: 2026-03-11 (confirmed from system timestamps; thread extended to 2026-04-16 for final query)
source_thread_title: "Comic book holder 3D print wall mount system — Bambu Lab P1S garage setup"
entry_type: project / skill / tool
chronological_position: UNKNOWN — to be placed during Obsidian compilation session
status: draft
supersedes: UNKNOWN — cannot confirm without seeing other entries
superseded_by: none
canonical_file: NEW FILE NEEDED — see Step 3 notes; closest existing: BRAYDEN-IDENTITY, SKILLS-EDUCATION
context_available: BRAYDEN-IDENTITY.md visible in Space files; no prior 3D printing entries found
tags: [3d-printing, bambu-lab, comic-books, garage-organization, frenchfinity, wall-mount, maker, modular-storage, P1S]
---

# Brain Entry — 3D Printed Comic Book Wall Mount System Design and Bambu Studio Workflow

---

## CONFIRMED FACTS
Only facts explicitly stated in this thread. Nothing inferred.

- Brayden owns a **Bambu Lab P1S** printer | confirmed | Bambu Studio screenshots show "Bambu Lab P1S" in printer selector
- Brayden owns a **Bambu Lab X1C** profile | also referenced | slicer profile visible "0.20mm Standard @BBL X1C"
- Brayden has an **AMS (multi-filament system)** | confirmed | 4 filament slots visible in all Bambu Studio screenshots
- Filaments loaded at time of session: Generic PLA (slot 1), PLA Basic (slot 2), PLA Matte (slot 3), PETG HF (slot 4) | confirmed | screenshot file:68
- Filaments loaded in second session: PETG HF (slot 1), PLA Wood (slot 2), PLA Basic (slot 3), PLA Matte (slot 4) | confirmed | screenshot file:69
- Brayden's garage is described as a **standard 2-car garage** | stated by Brayden | garage photo shared (file:33)
- Garage has very little wall space; floor is cluttered with boxes, chairs, shelving units | confirmed | photo file:33
- Existing shelving units (metal, multi-shelf) visible on back wall | confirmed | file:33
- **Model 1**: Vertical comic book holder — MakerWorld link https://makerworld.com/models/787123 | stated by Brayden
- Model 1 print stats: **~4.7 hours, 236g** | stated by Brayden
- Model 1 stated capacity: **~20 standard comic books** | stated by Brayden
- Model 1 confirmed dimensions in Bambu Studio: **62 x 206 x 204 mm** | object info box file:69
- Model 1 volume: **514,337 mm³** | object info box file:69
- Model 1 STL filename: **Comic Book Holder – v2.5.2.stl** | confirmed | file:69, file:71
- **Model 2**: Modular Comic Book Stand — MakerWorld link https://makerworld.com/models/1363563 | stated by Brayden
- Model 2 print stats: **~7 hours, 273g** | stated by Brayden
- Model 2 stated capacity: **~30 comic books** | stated by Brayden; from MakerWorld listing description
- Model 2 is **horizontal orientation** | confirmed by Brayden and 3D preview screenshot file:34
- Model 2 designed with modular divider/holder on 4mm peg increments | confirmed | MakerWorld listing text visible in file:35
- Model 2 creator: **XTP3** on MakerWorld | confirmed | file:35
- Model 2 has 122 downloads, 65 makes, 52 likes, 151 bookmarks | confirmed | file:35
- Standard comic book weight: **~2.2 oz / 62g each** | sourced from web
- 20 comics total load: **~2.75 lbs / 1,240g** | calculated in thread
- **Frenchfinity wall anchor** STL filename in Bambu Studio: **frenchfinity-wall-anchor-v1-w70.00.stl** | confirmed | file:68
- Wall anchor dimensions: **38.2668 x 20 x 70 mm** | object info box file:68
- Wall anchor volume: **36,974.7 mm³** | object info box file:68
- **Frenchfinity custom base adapter** STL filename: **frenchfinity-custom-b…adapter-v1-w30.00.stl** (truncated) | confirmed | file:70
- Base adapter dimensions: **29 x 8.26 x 21.76 mm** | object info box file:70
- Base adapter volume: **4,001.42 mm³** | object info box file:70
- At merge step (file:71), the adapter was successfully added as a **nested Part under the holder** in Bambu Studio
- Objects panel showed both parts nested under parent: "Comic Book Holder – v2.5.2.stl" with frenchfinity adapter as sub-part | confirmed | file:71
- Combined object volume after merge: **518,338 mm³** | object info box file:71
- Combined object dimensions: **213.234 x 62 x 204 mm** | file:71
- Slicer settings at time of merge step: **Layer height 0.20mm, 15% infill, 3 wall loops** | file:71
- Brayden asked about **0.8mm nozzle** time savings | confirmed | thread query
- Realistic time savings with 0.8mm nozzle on P1S: **10–30% per community consensus** | sourced from web
- Brayden wants to put **comic book cover art on the side panels** of holders using SVG emboss | confirmed | final thread query
- Bambu Studio supports native **SVG emboss/deboss** on model surfaces | confirmed via web sources
- Recommended tools for JPEG → SVG conversion: **Vector Magic** (online) and **Inkscape** (free, local) | confirmed via web sources
- Frenchfinity project website: **frenchfinity.xyz** | confirmed via web
- Frenchfinity wall anchor on Printables: https://www.printables.com/model/1101675-frenchfinity-french-cleat-wall-anchor | confirmed via web
- Frenchfinity custom base plate on Printables: https://www.printables.com/model/1101708-frenchfinity-french-cleat-custom-base-plate-adapte | confirmed via web
- Brayden's occupation: **Elite Direct Support Professional** at **Goodlife Innovations** | user profile metadata
- Brayden is located in **Lawrence, Kansas, US** | user profile metadata

---

## TIMELINE MARKERS

- **2026-03-11 ~11:21 AM CDT** — Thread opened; first comic holder model shared (Model 1, vertical)
- **2026-03-11 ~11:26 AM CDT** — Question about editing model in Bambu Studio
- **2026-03-11 ~11:34 AM CDT** — Second model shared (Model 2, modular horizontal); garage photo shared
- **2026-03-11 ~11:38 AM CDT** — Question about finding Frenchfinity rail system on MakerWorld
- **2026-03-11 ~11:47 AM CDT** — Request for direct Frenchfinity base link
- **2026-03-11 ~11:57 AM CDT** — Full download + install walkthrough requested
- **2026-03-11 ~12:03 PM CDT** — Wall anchor loaded in Bambu Studio; screenshot shared (file:68)
- **2026-03-11 ~12:09 PM CDT** — Comic holder + base adapter both loaded; merge step begins (file:69)
- **2026-03-11 ~12:15 PM CDT** — Trouble moving base adapter; Bambu Studio snapping issue reported
- **2026-03-11 ~12:19 PM CDT** — Both objects on plate but not yet merged (file:70)
- **2026-03-11 ~12:21 PM CDT** — Gizmo snapping to plate issue; "Add Part" workaround given
- **2026-03-11 ~12:27 PM CDT** — Merge confirmed successful as nested Part (file:71)
- **2026-03-11 ~1:30 PM CDT** — 0.8mm nozzle question
- **2026-04-16 ~4:28 PM CDT** — SVG texture question; thread archived today

---

## UPDATES TO CANONICAL FILES

- **BRAYDEN-IDENTITY**: Add confirmed ownership of Bambu Lab P1S with AMS. Add that Brayden does 3D printing as a hobby/maker activity. Add garage as a personal space Brayden is actively organizing/building out.
- **NEW FILE — MAKER-3DPRINT-LOG**: This thread warrants a dedicated canonical file (see Step 3). Should contain: printer hardware, filament inventory, active projects, Bambu Studio skill level, garage storage system build log.
- **SKILLS-EDUCATION**: Add Bambu Studio as an active tool Brayden is learning. Add skills confirmed in this thread: mesh boolean, negative parts, SVG emboss, part assembly, nozzle swapping, slicer settings optimization.

---

## CONTRADICTIONS

Cannot assess — thread is isolated. Flag for review during compilation.
- No prior 3D printing entries found in Space files to cross-check against. If any other thread mentions Brayden's printer model differently, flag at compilation.

---

## INSIGHTS & PATTERNS

- Brayden benefits from step-by-step instructions broken into individual clicks — abstract descriptions caused confusion (gizmo snapping issue persisted until exact workaround was given)
- Brayden is actively building out his garage as a functional maker/creative space, not just storage
- Brayden thinks in systems — immediately escalated from "one holder" to "how do I hold 600+ comics modularly"
- ADHD-relevant: Brayden engaged persistently across a multi-hour session on a single project without dropping it — strong hyperfocus indicator on maker/build topics
- Comic book collecting is a confirmed personal interest/hobby for Brayden
- Brayden has AMS and is interested in multi-color prints (cover art on holders) — aesthetic presentation matters to him even on functional prints
- Brayden ran into a common Bambu Studio beginner friction point (auto-drop to plate locking Z movement) — worth documenting as a known obstacle for future sessions

---

## TOOLS & RESOURCES REFERENCED

- **Bambu Lab P1S** | active | Primary printer; AMS equipped
- **Bambu Studio** | active | Slicer; Brayden is actively learning it
- **MakerWorld** | active | Source for STL models; used to find comic holder and Frenchfinity files
- **Frenchfinity** (frenchfinity.xyz) | active | French cleat wall system; wall anchor and base adapter downloaded and loaded
- **Printables.com** | active | Source for Frenchfinity STL files
- **Inkscape** | mentioned | Free JPEG→SVG tool for cover art textures
- **Vector Magic** (vectormagic.com) | mentioned | Online JPEG→SVG tracer
- **Tinkercad / Fusion 360** | mentioned | Referenced as CAD alternatives but not confirmed as used by Brayden
- **Bambu Studio Mesh Boolean** | skill confirmed | Used (or attempted) during merge step
- **Bambu Studio Add Part** | skill confirmed | Successfully used to nest adapter under holder

---

## OPEN QUESTIONS

- Did Brayden actually print the first test holder? Result not captured in this thread.
- Was the 0.8mm nozzle installed and tested? No result captured.
- Was the SVG cover art workflow attempted? Thread ended at the instructions step.
- How many total holders does Brayden plan to print for the full garage system?
- Was the Frenchfinity wall anchor physically mounted to a stud? Not confirmed.
- Which comic book series or characters does Brayden want to display? Not captured.
- Did the Mesh Boolean Union succeed or did Brayden stay with the nested Part approach? Screenshot file:71 shows nested Part but no Boolean result confirmed.
- What filament color(s) does Brayden plan to use for the holders?

---

## CROSS-REFERENCES

Cross-references to be added during compilation session.
- Feeds into: BRAYDEN-IDENTITY (maker hobby confirmed), SKILLS-EDUCATION (Bambu Studio skill), NEW FILE — MAKER-3DPRINT-LOG
- Possible links to: any garage/home organization threads, any maker/craft threads in other entries

---

## RAW HIGHLIGHTS

> "I want to make comic book holders to hang up in my garage" — Brayden, opening query

> "If my garage is a standard 2 car garage, with very little wall space, how can I make a system that allows me to hold the most amount of comic books while taking up the least amount of space? Can it be modular, expandable" — Brayden, second model query

> "Ok I'm at the merging step, to ensure that this doesn't exceed load bearing, droop, fall, etc, what should I do to this model for it to work with the wall anchor I just printed?" — Brayden, file:69 query

> "No position option in bottom right corner, gizmo snaps it back to the plate" — Brayden, confirming Bambu Studio Z-lock friction

> "I'm thinking about putting comic book cover art on the side of the vertical comic book holders" — Brayden, final creative intent

---

## ⚙️ COMPILATION NOTE

This entry was generated in an isolated thread. Entry ID, supersedes field, chronological position, and cross-references are unconfirmed until the full compilation session. During that session: assign IDs in date order, resolve contradictions, deduplicate facts across entries, and push confirmed updates to canonical files.
