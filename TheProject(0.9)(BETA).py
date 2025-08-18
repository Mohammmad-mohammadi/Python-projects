Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import sqlite3
conn = sqlite3.connect("TheProject.db")
cursor = conn.cursor()
SyntaxError: multiple statements found while compiling a single statement
[DEBUG ON]
conn = sqlite3.connect("TheProject.db")
cursor = conn.cursor()
SyntaxError: multiple statements found while compiling a single statement
[DEBUG ON]

[DEBUG ON]

[DEBUG OFF]




import sqlite3
  conn = sqlite3.connect("TheProject.db")
  cursor = conn.cursor()
  
SyntaxError: multiple statements found while compiling a single statement
import sqlite3


conn = sqlite3.connect("music.db")   
cursor = conn.cursor()

def list_all_pieces():
    query = """
    SELECT p.name, p.title, c.full_name, p.era, p.difficulty, e.name, p.type
    FROM Pieces p
    JOIN Composers c ON p.composer_id = c.id
    JOIN Emotions e ON p.emotion_id = e.id;
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n🎼 All Pieces in Database:")
    for row in rows:
        name, title, composer, era, difficulty, emotion, type_ = row
        print(f"🎶 {title} ({name})")
        print(f"   Composer: {composer} | Era: {era} | Difficulty: {difficulty}/10 | Emotion: {emotion} | Type: {type_}\n")

def search_by_composer(composer_name):
    query = """
    SELECT p.name, p.title, c.full_name, p.era, p.difficulty, e.name, p.type
    FROM Pieces p
    JOIN Composers c ON p.composer_id = c.id
    JOIN Emotions e ON p.emotion_id = e.id
    WHERE c.full_name LIKE ?;
    """
    cursor.execute(query, ('%' + composer_name + '%',))
    rows = cursor.fetchall()

    if not rows:
        print(f"\n No pieces found for composer: {composer_name}\n")
    else:
        print(f"\nPieces by {composer_name}:")
        for row in rows:
            name, title, composer, era, difficulty, emotion, type_ = row
            print(f"{title} ({name}) | Era: {era} | Difficulty: {difficulty}/10 | Emotion: {emotion} | Type: {type_}")

def main():
    while True:
        print("\n--- Music Database Menu ---")
        print("1. List all pieces")
        print("2. Search by composer")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_all_pieces()
        elif choice == "2":
            composer = input("Enter composer name: ")
            search_by_composer(composer)
        elif choice == "0":
            print("Goodbye !")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
    conn.close()
    
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
python 
import sqlite3


conn = sqlite3.connect("music.db")
cursor = conn.cursor()

def list_all_pieces():
    query = """
    SELECT p.name, p.title, c.full_name, p.era, p.difficulty, e.name, p.type
    FROM Pieces p
    JOIN Composers c ON p.composer_id = c.id
    JOIN Emotions e ON p.emotion_id = e.id;
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n All Pieces in Database:")
    for row in rows:
        name, title, composer, era, difficulty, emotion, type_ = row
        print(f" {title} ({name})")
        print(f"   Composer: {composer} | Era: {era} | Difficulty: {difficulty}/10 | Emotion: {emotion} | Type: {type_}\n")

def search_by_composer(composer_name):
    query = """
    SELECT p.name, p.title, c.full_name, p.era, p.difficulty, e.name, p.type
    FROM Pieces p
...     JOIN Composers c ON p.composer_id = c.id
...     JOIN Emotions e ON p.emotion_id = e.id
...     WHERE c.full_name LIKE ?;
...     """
...     cursor.execute(query, ('%' + composer_name + '%',))
...     rows = cursor.fetchall()
... 
...     if not rows:
...         print(f"\n No pieces found for composer: {composer_name}\n")
...     else:
...         print(f"\nPieces by {composer_name}:")
...         for row in rows:
...             name, title, composer, era, difficulty, emotion, type_ = row
...             print(f"{title} ({name}) | Era: {era} | Difficulty: {difficulty}/10 | Emotion: {emotion} | Type: {type_}")
... 
... def main():
...     while True:
...         print("\n--- Music Database Menu ---")
...         print("1. List all pieces")
...         print("2. Search by composer")
...         print("0. Exit")
... 
...         choice = input("Choose an option: ")
... 
...         if choice == "1":
...             list_all_pieces()
...         elif choice == "2":
...             composer = input("Enter composer name: ")
...             search_by_composer(composer)
...         elif choice == "0":
...             print("Goodbye !")
...             break
...         else:
...             print("Invalid choice, try again.")
... 
... if __name__ == "__main__":
...     main()
...     conn.close()
...     
SyntaxError: multiple statements found while compiling a single statement
