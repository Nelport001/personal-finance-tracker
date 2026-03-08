import sqlite3
import datetime
 

def setup_database():
    conn = sqlite3.connect("finance.db")
    
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            date        TEXT    NOT NULL,
            category    TEXT    NOT NULL,
            description TEXT,
            amount      REAL    NOT NULL,
            type        TEXT    NOT NULL
        )    
 """)
    conn.commit()

    conn.close()
    print("Database ready!")

setup_database()

def add_transaction(date, category, description, amount, t_type):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (date, category, description, amount, type)
        VALUES (?, ?, ?, ?, ?)
""", (date, category, description, f"${amount}", t_type))

    conn.commit()
    conn.close()
    print("\n---- Transaction added! ----")

# add_transaction("2026-03-02", "Food", "Lunch", 12.50, "expense")

def view_transactions():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")

    rows = cursor.fetchall()
    conn.close()
    
    if len(rows) == 0:
        print("\n ---- The database is empty! -----")
    else:
        for row in rows:
            print(row)

#view_transactions()

def view_by_category(category):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transactions
        WHERE category = ?
""", (category,))
    
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        print(row)

#view_by_category("Food")

def show_summary():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount) FROM transactions
        WHERE type = 'income'
""")
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("""
        SELECT SUM(amount) FROM transactions
        WHERE type = 'expense'
""")
    total_expenses = cursor.fetchone()[0] or 0

    balance = total_income - total_expenses

    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("Balance:", balance)

# show_summary()

def delete_transaction(transaction_id):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM transactions
        WHERE id = ?
""", (transaction_id,))
    
    conn.commit()
    conn.close()
    print("Transaction deleted!")

# delete_transaction(1)

def delete_all_transactions():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM transactions
""")
    conn.commit()
    conn.close()
    print("All transactions have been deleted!")

def main():
    setup_database()

    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View all Transactions")
        print("4. Delete a Transaction")
        print("5. Delete all Transaction")
        print("6. Show Summary")
        print("7. Quit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            description = input("Description: ")
            category = input("Category: ")
            amount = float(input("amount: "))
            date = datetime.date.today().isoformat()    
            add_transaction(date, category, description, amount, "income")
        elif choice == "2":
            description = input("Description: ")
            amount = float(input("amount: "))
            date = datetime.date.today().isoformat()    
            add_transaction(date, category, description, amount, "expense")

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            view_transactions()
            transaction_id = int(input("Enter ID to delete: "))
            delete_transaction(transaction_id)
        
        elif choice == "5":
            confirmation = input("Are you sure you want to delete all transactions? (yes/no):")
            if confirmation.lower() == "yes":
                delete_all_transactions()
            elif confirmation.lower() == "no":
                print("\n--- Cancelled ----")
            else:
                print("\n --- Enter yes or no ---")
                continue
        
        elif choice == "6":
            show_summary()

        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("\n ---- Choose a valid option from 1-6 ----")
            continue

main()
