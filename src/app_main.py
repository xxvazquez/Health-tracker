from flask import Flask, render_template, redirect, url_for
from src.forms import IntakeForm
from datetime import datetime
from src.config import Config
from src.models import db, Food, Intake

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/add', methods=['GET', 'POST'])
    def add_intake():
        form = IntakeForm()
        if form.validate_on_submit():
            intake = Intake(date=datetime.today().date(), food_id=form.food.data, quantity=form.quantity.data)
            db.session.add(intake)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('add_intake.html', form=form)

    @app.route('/report')
    def report():
        intakes = Intake.query.all()
        return render_template('report.html', intakes=intakes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
