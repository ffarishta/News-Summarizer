from app import db, User, app  # Replace with your actual filename (e.g. from app import db, User, app)

with app.app_context():
    db.create_all()