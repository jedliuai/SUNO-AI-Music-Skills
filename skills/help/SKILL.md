---
name: help
description: Shows available skills, common workflows, and quick reference for the plugin. Use when the user asks for help, what skills are available, or how to do something.
---

## bitwize-music Plugin Help

Display this help information to the user in a clear, organized format.

---

### Getting Started

**New to the plugin?**
- ``tutorial` skill` - Interactive guided album creation
- ``configure` skill` - Set up configuration file
- ``about` skill` - About bitwize and this plugin

**Resume existing work:**
- ``resume` skill <album-name>` - Find an album and see status/next steps

---

### Skills by Category

**Album & Track Creation**
- ``album-ideas` skill` - Track and manage album ideas
- ``promote-idea` skill` - Convert a Pending idea into a full album (one-shot)
- ``new-album` skill` - Create new album with directory structure
- ``album-conceptualizer` skill` - Album concepts and tracklist architecture
- ``lyric-writer` skill` - Write/review lyrics, fix prosody
- ``suno-engineer` skill` - Technical Suno prompting and genre selection

**Research & Sources**
- ``researcher` skill` - Main research coordinator, fact-checking
- ``document-hunter` skill` - Automated document search/download
- ``researchers-legal` skill` - Court documents, indictments
- ``researchers-gov` skill` - DOJ/FBI/SEC releases
- ``researchers-tech` skill` - Project histories, changelogs
- ``researchers-journalism` skill` - Investigative articles
- ``researchers-security` skill` - Malware analysis, CVEs
- ``researchers-financial` skill` - SEC filings, market data
- ``researchers-historical` skill` - Archives, timelines
- ``researchers-biographical` skill` - Personal backgrounds
- ``researchers-primary-source` skill` - Tweets, blogs, forums
- ``researchers-verifier` skill` - Quality control, citation validation

**Quality Control**
- ``lyric-reviewer` skill` - Pre-generation QC gate (14-point checklist)
- ``pronunciation-specialist` skill` - Scan for pronunciation risks
- ``explicit-checker` skill` - Verify explicit content flags
- ``plagiarism-checker` skill` - Check lyrics for phrases matching existing songs
- ``voice-checker` skill` - Detect AI-written patterns in lyrics and prose
- ``pre-generation-check` skill` - Final pre-generation checkpoint (6 gates)
- ``validate-album` skill` - Validate album structure and paths

**Production & Release**
- ``album-art-director` skill` - Visual concepts and AI art prompts
- ``mastering-engineer` skill` - Audio mastering guidance
- ``promo-director` skill` - Generate promo videos for social media
- ``cloud-uploader` skill` - Upload promo videos to Cloudflare R2 or AWS S3
- ``sheet-music-publisher` skill` - Convert audio to sheet music
- ``release-director` skill` - Release coordination and distribution

**File Management**
- ``import-track` skill` - Move track .md files to album location
- ``import-audio` skill` - Move audio files to album location
- ``import-art` skill` - Place album art in correct locations
- ``clipboard` skill` - Copy track lyrics/prompts to clipboard

**Workflow & Status**
- ``session-start` skill` - Run session startup procedure
- ``next-step` skill` - Get recommended next action
- ``album-dashboard` skill` - Visual album progress dashboard

**System & Maintenance**
- ``configure` skill` - Edit plugin configuration
- ``test` skill` - Run automated tests
- ``skill-model-updater` skill` - Update model references in skills
- ``help` skill` - Show this help (you are here!)
- ``about` skill` - About bitwize and the plugin

---

### Common Workflows

**Creating a New Album:**
1. ``new-album` skill <name> <genre>` - Create structure (or ``promote-idea` skill "<idea title>"` if the idea lives in `IDEAS.md`)
2. Answer the 7 planning phases (concept, sonic direction, etc.)
3. Write lyrics for each track
4. Run ``lyric-reviewer` skill` before generation
5. Generate in Suno, log results
6. Master audio with ``mastering-engineer` skill`
7. [Optional] Generate promo videos with ``promo-director` skill`
8. [Optional] Upload to cloud with ``cloud-uploader` skill`
9. Release with ``release-director` skill`

**True-Story Albums (with research):**
1. Use researcher skills to gather sources
2. All sources must be verified by human before production
3. Update track status from `❌ Pending` to `✅ Verified (DATE)`
4. Then proceed with lyric writing and generation

**Resume Existing Work:**
1. ``resume` skill <album-name>` - Get detailed status
2. Follow the recommended next steps

---

### Quick Tips

- **Config file:** `~/.bitwize-music/config.yaml` (always read this for paths)
- **Pronunciation:** Use phonetic spelling for tricky words (see pronunciation guide)
- **Explicit content:** Use flag for: fuck, shit, bitch, cunt, cock, dick, pussy, etc.
- **Mastering target:** -14 LUFS, -1.0 dBTP for streaming platforms
- **Promo videos:** Generate after mastering, 15s vertical (9:16) for social media
- **Track status flow:** Not Started → In Progress → Generated → Final
- **Album status flow:** Concept → In Progress → Complete → Released

---

### Key Documentation

- **CLAUDE.md** - Main workflow instructions
- **README.md** - Project overview
- `this skill package root/reference/suno/` - Suno V5 guides, pronunciation, tips
- `this skill package root/reference/workflows/` - Detailed workflow procedures
- `this skill package root/reference/mastering/` - Audio mastering documentation
- `this skill package root/templates/` - Templates for new content
- `this skill package root/skills/[skill-name]/SKILL.md` - Individual skill documentation

---

### Getting Help

- Use this skill anytime: ``help` skill`
- For tutorial: ``tutorial` skill`
- For status: ``resume` skill <album-name>`
- Ask Codex: "What should I do next?" for guidance
