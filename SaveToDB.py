def save_to_database(numbers):
    # For now, just print numbers
    print(f"Saving to database: {numbers}")

    # Here you can add real database logic
    # Example with SQLite:
    # import sqlite3
    # conn = sqlite3.connect('yourdb.db')
    # c = conn.cursor()
    # c.execute('CREATE TABLE IF NOT EXISTS numbers (num TEXT)')
    # for num in numbers:
    #     c.execute('INSERT INTO numbers (num) VALUES (?)', (num,))
    # conn.commit()
    # conn.close()
