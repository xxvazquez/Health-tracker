import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app_main import create_app
from models import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created")
