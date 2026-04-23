\# BRAINOS-SYSTEM.md  
Last updated: April 10, 2026 | Meta-file \- describes the whole system

\#\# What This System Is

BrainOS is Brayden Boots' personal knowledge operating system.  
Goal: A growing, evolving second brain that makes connections across all projects, retains important information long-term, and gets smarter over time without manual overhead.

This system was built on April 10, 2026 from all Perplexity thread history across all Spaces.

\#\# The Core Problem This Solves

\- Perplexity AI has NO memory between threads \- each thread starts blank  
\- Multiple project Spaces were siloed \- no cross-domain synthesis possible  
\- Brain\_Entry files were accumulating but not connected to a working system  
\- Old threads contained outdated information surfacing as if current

\#\# The Solution Architecture

\#\#\# Two-Tier File System

Tier 1 \- Canonical Files (8 files, Google Drive, synced to Perplexity Space)  
These are living documents. Updated in place. Never replaced. Always current.  
\- BRAYDEN-IDENTITY.md  
\- FINANCIAL-SNAPSHOT.md  
\- CTRL-YOU-STATUS.md  
\- KRAY-STUDIOS-CONTENT.md  
\- GOODLIFE-UNION.md  
\- SKILLS-EDUCATION.md  
\- AI-WORKFLOW-RULES.md  
\- BRAINOS-SYSTEM.md (this file)

Tier 2 \- Archive (Obsidian, never in Perplexity Space)  
Event logs, brain entries, old versions, raw exports.  
Unlimited files. Searchable. Graphable. Never touches the 50-file limit.

\#\#\# The Flow

Conversation happens in Perplexity  
  \--\> /mdsummary generates a Brain\_Entry (Tier 2 archive)  
  \--\> Canonical File Targets section tells you what to update  
  \--\> You update the Tier 1 Google Drive file directly  
  \--\> Google Drive auto-syncs to Perplexity Space  
  \--\> Next session has current context without any file management overhead

\#\# Google Drive Structure

Folder: /BrainOS-Canonical/  
Contents: All 8 Tier 1 files above  
Connect this folder to your Perplexity Master Brain Space via Google Drive connector

Folder: /BrainOS-Archive/  
Contents: Brain\_Entry\_001 through Brain\_Entry\_00X, raw exports  
This folder does NOT connect to Perplexity

\#\# Perplexity Master Brain Space Setup

1\. Create one Space called "Master Brain" or "BrainOS"  
2\. Connect Google Drive /BrainOS-Canonical/ folder  
3\. Copy BRAYDEN-IDENTITY.md content into the Space system prompt (always-on context)  
4\. Collapse all separate project Spaces into this one (except where active project work warrants isolation)  
5\. Always use the most capable model for synthesis queries

\#\# Obsidian Vault Setup (when ready)

Folder structure:  
\- /Canonical/ \- mirror of Google Drive Tier 1 files (linked, not duplicated)  
\- /Archive/ \- all Brain\_Entry files  
\- /Notes/ \- freeform notes, ideas, fleeting captures  
\- /Projects/ \- one file per active project (links to canonical files)

Key Obsidian plugins to install:  
\- Obsidian Copilot (Perplexity API integration)  
\- Obsidian Web Clipper (capture from browser)  
\- Dataview (query your vault like a database)

\#\# The /mdsummary Shortcut (upgraded)

Recommended prompt structure:  
\- \#\# Thread Summary  
\- \#\# Key Information Extracted  
\- \#\# Decisions Made  
\- \#\# Cross-Domain Connections (MANDATORY)  
\- \#\# Canonical File Targets (which Tier 1 files to update)  
\- \#\# Permanent Rules Extracted (for AI-WORKFLOW-RULES.md)  
\- \#\# Priority-Flagged Open Questions  
\- \#\# Tags

\#\# Version History

v1.0 \- April 10, 2026: Initial build from full thread history scan across all Spaces  
Created by: Perplexity/Comet in single session  
Based on: Totally hands off. space, Union space, The Van The Debt space, general library threads

\#\# What Comes Next

1\. Move all 8 files into /BrainOS-Canonical/ folder in Google Drive  
2\. Create Master Brain Space in Perplexity  
3\. Connect Google Drive folder to that Space  
4\. Copy BRAYDEN-IDENTITY content into Space system prompt  
5\. Start using Master Brain Space for all future queries  
6\. Set up Obsidian vault (low priority until Perplexity system is working)  
7\. Run /mdsummary on remaining threads not yet captured  
8\. Update Canonical files with anything surfaced from those threads  
