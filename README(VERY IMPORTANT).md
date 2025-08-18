For nominating committees / reviewers — a concise story about me, why I’m applying, and a clear explanation of my flagship project so you can verify, run, and evaluate it quickly.




---

Who I am (short story)

I’m 15, from Iran, and I’m a student who thinks of the world in patterns — in notes, numbers and small signals. I grew up reading history, practising piano, and solving math problems; those three habits shaped how I learn and how I build. At school I achieved top grades (20/20 GPA in 9th grade), I attend a rigorous Sampad program, and I’m steadily combining two things that feel most like me: music and data.

I compose and perform piano pieces (I work with demanding repertoire and original compositions). At the same time I teach myself programming and data work — I’m advanced in Python, actively building projects that are both technical and human-centered. My projects are not showpieces: they’re tools I’ve made to help other learners and to document knowledge in a rigorous, verifiable way.

Why this matters: I want to study quantitative fields because they reward exactness, pattern recognition, and disciplined creativity — the same skills I practice at the piano and at the keyboard. The flagship project bundled here is the clearest expression of that blend: a verifiable, searchable database of canonical musical works that I designed, implemented and packaged so others can use it immediately.


---

What the flagship project demonstrates (one-sentence)

A self-directed, full-stack data project that combines structured data design, reproducible methods, and a small web UI — showing technical skill (Python + SQL), quantitative thinking (data design and metrics), domain knowledge (music history/curation), and the ability to produce verifiable work for reviewers.


---

Flagship Project — Overview

Name: Music Ultimate — composer & repertoire database (packaged offline)
Why built: to create a verifiable, browsable corpus of canonical repertoire useful for pedagogy, curriculum design, and quantitative analysis of repertoire. The project is intentionally reproducible and verifiable: the database is compiled from canonical references (Wikipedia-style sources noted in the Sources table), and the code is purely local — no external calls are required to run or verify.


---

What’s included in the package

music_ultimate_full.db — ready-to-use SQLite database (Composers, Pieces, Emotions, Sources).

music_browser.py — a read-only Flask application to browse/filter/export the database.

README.txt — quick-run notes (this file is the expanded README).

music_ultimate_sources.csv (optional) — composer → source mapping (for manual validation).



---

Database design (schema summary)

Tables and key columns:

Composers (composer_id, full_name, era, nationality, main_instrument, wiki_url)

Pieces (piece_id, name, title, composer_id, era, major_scale, difficulty, emotion_id, type, wiki_url)

Emotions (emotion_id, emotion_name) — seeded with curated emotional labels (e.g., Tranquility, Longing)

Sources (id, composer_name, composer_wiki_url, work_title, work_wiki_url) — maps claims to public pages for verification


Design goals:

Intelligible foreign-key model (Pieces → Composers, Pieces → Emotions) so reviewers can query relationships quickly.

Source traceability so every piece entry can be checked against public references.

Fields that reflect musical and analytical qualities: major_scale, difficulty, emotion_id, type (etude, sonata, concerto, etc.).



---

How the flagship project works — technical flow

1. Offline data (db file)
The packaged SQLite DB contains the curated data. That means no scraping or network activity is required to review the content. The Sources table points to public pages so reviewers can confirm entries easily.


2. Local app (browsing + filter + export)
music_browser.py reads the database and launches a small Flask web UI to:

Filter by composer, emotion, minimum difficulty, type, major scale, or free-text in the title.

Sort results by difficulty or composer name.

Export the current filtered view as CSV for downloading and sharing.



3. Reproducibility / provenance

Every record includes a link in Sources to at least the composer’s public page (and, where available, the work’s page).

The schema and CSV exports allow any reviewer to re-run analysis, import into other tools, or extend the dataset.



4. Why this shows readiness for quantitative work

Data design: normalised tables, referential integrity, explicit provenance.

Analytical thinking: ability to design fields (difficulty, emotion) and justify measurement choices — the next step is to compute item statistics (e.g., distribution of difficulty across eras) or reliability metrics (like test KR-20 on item banks).

Software: building a usable UI and export shows practical engineering discipline (packaging, documentation, reproducibility).





---

How to run and verify (reviewer-friendly)

Prerequisites

Python 3.9+ (recommended)

pip install flask (for the browser app)


Quick run

# unzip the package and cd into it
python -m venv venv         # optional but recommended
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install flask
python music_browser.py --db music_ultimate_full.db --host 127.0.0.1 --port 5000
# open http://127.0.0.1:5000 in your browser

Useful sample SQL queries (for reviewers who prefer the DB directly)

Count pieces by emotion:


SELECT e.emotion_name, COUNT(*) FROM Pieces p
JOIN Emotions e ON p.emotion_id = e.emotion_id
GROUP BY e.emotion_name ORDER BY COUNT(*) DESC;

Top challenging “Longing” pieces:


SELECT p.title, c.full_name, p.difficulty FROM Pieces p
JOIN Composers c ON p.composer_id=c.composer_id
JOIN Emotions e ON p.emotion_id=e.emotion_id
WHERE e.emotion_name='Longing' AND p.difficulty > 6 ORDER BY p.difficulty DESC;

Show sources for a composer:


SELECT * FROM Sources WHERE composer_name LIKE '%Chopin%';


---

How the flagship project was curated (transparency)

The dataset was assembled from canonical composer pages and published “selected works” lists (Wikipedia-style public references). Every piece entry includes a Sources trace so reviewers can verify claims.

The project is intentionally curated (not exhaustive) — I selected the most canonical, pedagogically relevant works to showcase repertoire across eras and to keep the dataset focused for evaluation.

Emotion mapping and difficulty are curator judgements (documented in the DB). These are meant to be transparent, editable, and reproducible: reviewers can reassign labels or run their own mapping logic.



---

Impact, evidence & how this helps my application

This project is designed to demonstrate:

Quantitative aptitude: schema design, data normalization, and the ability to reason about metrics and distributions.

Programming and engineering: a complete, runnable project (Python + SQLite + Flask) with exports and documentation.

Domain knowledge & creativity: deep, verifiable engagement with music (repertoire selection, analysis of scale/key and emotional mapping).

Initiative & reproducibility: I packaged the entire workspace so a reviewer can inspect, run, and validate every claim without special permissions.


For a scholarship committee, this project shows I can:

Identify a problem, set measurable goals, and deliver a robust technical solution.

Work across fields (arts + data), showing the interdisciplinary thinking prized by modern quantitative programs.



---

How the flagship project could be evaluated (suggested rubric)

Data integrity (30%) — Are the composer/work entries correct and traceable? (Check Sources entries)

Design & queryability (25%) — Is the schema sensible and easy to query? (Run sample SQL queries)

Functionality (25%) — Does the app allow filtering and export as described? (Run the Flask app and export CSV)

Creativity & depth (20%) — Are the pieces chosen well? Is emotion/difficulty mapping thoughtful and consistent?



---

Next steps (what I plan to add)

An interactive scale visualiser (draw a scale and show cadences) integrated with the piece view.

Automatic per-work verification fallback (local tool to look up missing work pages; offline by default, online if a reviewer permits).

Statistical reports (difficulty histograms, era vs. emotion heatmaps) to show quantitative analysis outcomes.



---

Closing note (personal)

This project is more than a technical exercise. It is the intersection of what I love (music) and how I think (structured, analytical, reproducible). I packaged it so a reviewer can verify everything in minutes, run queries themselves, and see the rigor in the choices I made. If you review my work and want a live walkthrough, I can present the data, show the code, and explain the modeling decisions — and I’ll add any requested clarifications directly into the DB or README so the evidence is immediately available.
