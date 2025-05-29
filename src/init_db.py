from app import app, db, User, News

def init_db():
    with app.app_context():
        db.drop_all()  # Optional: clears existing data
        db.create_all()
        print("✅ Tables created in database.db")

if __name__ == '__main__':
    init_db()