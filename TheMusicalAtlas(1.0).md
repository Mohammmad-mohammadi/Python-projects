🎼 Music Atlas — First Release

👤 About Me

Hi, I’m a student and a builder who loves music, technology, and the idea of organizing complex things into something simple. This is my first attempt at bundling classical music data into an accessible format, so that anyone (including myself) can search, filter, and explore without needing a complicated setup.

📖 About the Project

This project is called Music Atlas. Its goal is simple:
to bring together a database of musical works and make them easy to browse, search, and filter.

There are two different browsers included:

1. TheProject.py — Flask-based web interface (runs locally, but requires keeping a server open).


2. TheProject(offline).py — Offline terminal browser (runs fully offline, no server, no internet).



Because running Flask all the time on my phone isn’t practical, I built the offline version as the main tool. That’s the one most people should use.


---

⚡ Offline Browser

The offline browser (TheProject(offline).py) is the recommended way to explore.
It connects to the included music_ultimate_full.db SQLite database.

Features

🎹 Filter by composer, nationality, key signature, difficulty, and type

🔎 Multi-filter form (s) or single filters (c, n, t, k, etc.)

📑 Sort results by difficulty or composer

📄 Export filtered results to CSV

📱 Designed to work both on desktop and mobile (e.g. Pydroid on Android)


Quick Commands

s — open multi-filter search

c — filter composer

d — filter by minimum difficulty

n — filter by nationality

k — filter by key signature

t — filter by type

o — sort

p — change page size

> — next page

< — previous page

x — export current results to CSV

r — reset filters

h — help

q — quit



---

🗂 Database

The SQLite database included is music_ultimate_full.db, with two main tables:

Composers — full name, nationality, and other metadata

Pieces — title, difficulty, type, key signature, and composer link



---

🛠 Known Bugs & Limitations (v1)

This is the first version — expect rough edges:

Some pieces are missing type and key signature information.

Not all metadata is fully standardized (e.g. “French” vs “France”).

Filtering sometimes gives unexpected results due to inconsistent data.

Column widths in the offline table can look cramped on small screens.

Export CSV may contain empty fields for incomplete data.


These issues will be fixed and improved in future versions. This is just the beginning.


---

💬 Personal Note

This project is both a technical exercise and a personal passion project. It’s not perfect — in fact, it’s full of bugs — but it represents a first step. I’m learning, improving, and planning to release a much better version in the future.

If you’re reading this, thank you for taking an interest in my work.

— End of Version 1
-- Mohammad Mohammadi 2025/8/19
