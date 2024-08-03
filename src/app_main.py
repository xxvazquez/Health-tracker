from flask import Flask, render_template, redirect, url_for, request 
from datetime import datetime
from src.config import Config
from src.models import db, Food, Intake

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.route('/')
    def index():
        intakes = Intake.query.order_by(Intake.date.desc()).limit(5).all()  # Get the most recent 5 intakes
        return render_template('index.html', intakes=intakes)

    @app.route('/add', methods=['GET', 'POST'])
    def add_intake():
        foods = Food.query.all()  # Retrieve all food items from the database
        if request.method == 'POST':
            selected_foods = request.form.getlist('food')  # Get selected food items
            quantity = request.form.get('quantity')  # Get the quantity from the form

            for food_id in selected_foods:
                intake = Intake(date=datetime.today().date(), food_id=food_id, quantity=quantity)
                db.session.add(intake)

            db.session.commit()
            return redirect(url_for('index'))

        return render_template('add_intake.html', foods=foods)

    @app.route('/report')
    def report():
        intakes = Intake.query.all()
        return render_template('report.html', intakes=intakes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)