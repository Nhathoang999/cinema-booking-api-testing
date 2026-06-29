import sqlite3
import os
import sys

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'cinema.db')

def verify_booking_created(target_username="qa_automation_user"):
    """Verifies that the automated test user has a booking."""
    if not os.path.exists(DB_PATH):
        print(f"[-] Database {DB_PATH} not found.")
        sys.exit(1)
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, email FROM users WHERE username = ?", (target_username,))
        user_row = cursor.fetchone()
        
        if not user_row:
            print(f"[-] Verify DB Failed: User with username '{target_username}' not found in DB.")
            sys.exit(1)
            
        user_id = user_row[0]
        email = user_row[1]
        
        cursor.execute("SELECT movie_id FROM bookings WHERE user_id = ? AND status != 'CANCELLED'", (user_id,))
        bookings = cursor.fetchall()
        
        if not bookings:
            print(f"[-] Verify DB Failed: No active bookings found for user '{email}'")
            sys.exit(1)
            
        print(f"[+] Verify DB Passed: Found {len(bookings)} active bookings for test user '{email}'.")
    except Exception as e:
        print(f"[-] Booking Verification FAILED: {e}")
        sys.exit(1)
    finally:
        conn.close()

if __name__ == "__main__":
    print("Running Database State Verification...")
    verify_booking_created()
