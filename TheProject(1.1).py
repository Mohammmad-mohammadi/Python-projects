import sqlite3
DB_PATH = "music.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory =  sqlite3.row
    return conn


def list_all_pieces():
    sql = ''' select p.name,p.title,c.full_name AS composer , p.era, p.major_scale , p.difficulty, COALESCE(e.emotions_name '-') AS emotion, p.type
FROM pieces p
JOIN Composers c ON p.composer_id =c.composer_id
LEFT JOIN Emoitons e ON p.emotion_id = e.emotion _id
WHERE c.fullname LIKE ? COLLATE
NO CASE
ORDER BY p.difficulty DESC, p.name;'''
    with get_conn() as conn :
        Row = conn.executive(sql,
                              (f"%{name_query}%",)).fetchall()
        if not Row :
            print(f"\n No pieces found for composer matching : {name_query}\n")
            return
        print(f"\n Pieces tagged ~ {emotion_query} ~")
        for r in Row:
                    title = f"{r['title']} " if r['title'] else ""
        print(f"  • {title}({r['name']}) — {r['composer']} | {r['era']} | {r['major_scale']} | {r['difficulty']}/10 | {r['type']}")

        
def search_by_difficulty(min_d= 1 , max_d = 10):
    sql ="""SELECT p.name,p.title,c.full_name AS composer,
p.era,p.majore_scale,p.difficuty, COALESCE9e.emotions_name '-' AS emotion, p.type     FROM Pieces p
    JOIN Composers c ON p.composer_id = c.composer_id
    LEFT JOIN Emotions e ON p.emotion_id = e.emotion_id
    WHERE p.difficulty BETWEEN ? AND ?
    ORDER BY p.difficulty DESC, c.full_name;
    """
    with get_conn() as conn:
        Row = conn.execute(sql, (min_d, max_d)).fetchall()

    print(f"\n Pieces with difficulty {min_d}–{max_d}")
    for r in Row:
        title = f"{r['title']} " if r['title'] else ""
        print(f"  • {title}({r['name']}) — {r['composer']} | {r['difficulty']}/10 | {r['emotion']} | {r['type']}")

def main():
    while True:
        print("\n--- Music DB Menu ---")
        print("1) List all pieces")
        print("2) Search by composer")
        print("3) Search by emotion")
        print("4) Search by difficulty range")
        print("0) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            list_all_pieces()
        elif choice == "2":
            q = input("Composer name (e.g., Chopin): ").strip()
            search_by_composer(q)
        elif choice == "3":
            q = input("Emotion (Tranquility, Melancholy, Tension, Triumph, Longing): ").strip()
            search_by_emotion(q)
        elif choice == "4":
            try:
                lo = int(input("Min difficulty (1–10): ").strip())
                hi = int(input("Max difficulty (1–10): ").strip())
            except ValueError:
                print("Enter numbers between 1 and 10.")
                continue
            lo, hi = max(1, lo), min(10, hi)
            if lo > hi:
                lo, hi = hi, lo
            search_by_difficulty(lo, hi)
        elif choice == "0":
            print("Goodbye ")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "___main___":
    try:
        # Quick connectivity check
        with get_conn() as conn:
            pass
    except sqlite3.Error as e:
        print(f" Could not open DB at {DB_PATH}: {e}")
        raise SystemExit(1)
    main()

def search_by_difficulty(min_d= 1 , max_d = 10):
    sql ="""SELECT p.name,p.title,c.full_name AS composer,
p.era,p.majore_scale,p.difficuty, COALESCE9e.emotions_name '-' AS emotion, p.type     FROM Pieces p
    JOIN Composers c ON p.composer_id = c.composer_id
    LEFT JOIN Emotions e ON p.emotion_id = e.emotion_id
    WHERE p.difficulty BETWEEN ? AND ?
    ORDER BY p.difficulty DESC, c.full_name;
    """
    with get_conn() as conn:
        Row = conn.execute(sql, (min_d, max_d)).fetchall()

    print(f"\n Pieces with difficulty {min_d}–{max_d}")
    for r in Row:
        title = f"{r['title']} " if r['title'] else ""
        print(f"  • {title}({r['name']}) — {r['composer']} | {r['difficulty']}/10 | {r['emotion']} | {r['type']}")





def main():
    while True:
        print("\n--- Music DB Menu ---")
        print("1) List all pieces")
        print("2) Search by composer")
        print("3) Search by emotion")
        print("4) Search by difficulty range")
        print("0) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            list_all_pieces()
        elif choice == "2":
            q = input("Composer name (e.g., Chopin): ").strip()
            search_by_composer(q)
        elif choice == "3":
            q = input("Emotion (Tranquility, Melancholy, Tension, Triumph, Longing): ").strip()
            search_by_emotion(q)
        elif choice == "4":
            try:
                lo = int(input("Min difficulty (1–10): ").strip())
                hi = int(input("Max difficulty (1–10): ").strip())
            except ValueError:
                print("Enter numbers between 1 and 10.")
                continue
            lo, hi = max(1, lo), min(10, hi)
            if lo > hi:
                lo, hi = hi, lo
            search_by_difficulty(lo, hi)
        elif choice == "0":
             print("Goodbye ")
             break
        else:
            print("Invalid choice. Try again.")

def get_conn():
     conn = sqlite3.connect(DB_PATH)
     conn.row_factory =  sqlite3.row
     return conn
def main():
    while True:
         print("\n--- Music DB Menu ---")
         print("1) List all pieces")
         print("2) Search by composer")
         print("3) Search by emotion")
         print("4) Search by difficulty range")
         print("0) Exit")
         choice = input("Choose: ").strip()

         if choice == "1":
             list_all_pieces()
         elif choice == "2":
             q = input("Composer name (e.g., Chopin): ").strip()
             search_by_composer(q)
         elif choice == "3":
             q = input("Emotion (Tranquility, Melancholy, Tension, Triumph, Longing): ").strip()
             search_by_emotion(q)
         elif choice == "4":
             try:
                 lo = int(input("Min difficulty (1–10): ").strip())
                 hi = int(input("Max difficulty (1–10): ").strip())
             except ValueError:
                 print("Enter numbers between 1 and 10.")
                 continue
             lo, hi = max(1, lo), min(10, hi)
             if lo > hi:
                 lo, hi = hi, lo
             search_by_difficulty(lo, hi)
         elif choice == "0":
             print("Goodbye ")
             break
         else:
             print("Invalid choice. Try again.")

if __name__ == "__main__":
    try:
        # Quick connectivity check
        with get_conn() as _:
            pass
    except sqlite3.Error as e:
        print(f" Could not open DB at {DB_PATH}: {e}")
        raise SystemExit(1)
