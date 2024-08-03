from src.app_main import create_app
from src.models import db

app = create_app()
app.app_context().push()
db.create_all()
