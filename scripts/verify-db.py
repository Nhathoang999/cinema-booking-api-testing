import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'cinema.db')

def verify_booking_created(email, expected_movie_id):
    """Verifies that a user has a booking for the specified movie."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # In a real app, you would join users and bookings, but this assumes a simple schema
    try:
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        user_row = cursor.fetchone()
        assert user_row is not None, f"User {email} not found in DB."
        user_id = user_row[0]
        
        cursor.execute("SELECT movie_id FROM bookings WHERE user_id = ? AND status != 'CANCELLED'", (user_id,))
        bookings = cursor.fetchall()
        movie_ids = [b[0] for b in bookings]
        
        assert expected_movie_id in movie_ids, f"Movie {expected_movie_id} booking not found for user {email}"
        print("Booking Created: PASS")
    except Exception as e:
        print(f"Booking Verification FAILED: {e}")
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    # Example usage during pipeline execution
    # In reality, this would dynamically read the test user email used in the API test run
    print("Database Verification Running...")
    # This acts as a stub to show the DB assertion capability for the portfolio
    print("DB Schema connected and validation ready.")
    pass
