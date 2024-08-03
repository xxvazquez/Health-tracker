# populate_db.py
from src.app_main import create_app
from src.models import db, Food

app = create_app()
app.app_context().push()

def populate_food_data():
    foods = [
        # Dairy
        ('Hard cheese (parmesan)', 'Dairy'),
        ('Kefir', 'Dairy'),
        ('Semi-soft or soft cheese (feta)', 'Dairy'),
        ('Yogurt', 'Dairy'),
        # Dairy alt
        ('Almond milk', 'Dairy alt'),
        ('Coconut milk', 'Dairy alt'),
        ('Coconut yogurt', 'Dairy alt'),
        # Fat
        ('Coconut oil (cold)', 'Fat'),
        ('Ghee or butter', 'Fat'),
        ('Olej z czarnuszki', 'Fat'),
        ('Olej z rotkinita', 'Fat'),
        ('Olej z wiesiołka', 'Fat'),
        ('Olive oil', 'Fat'),
        # Fruit
        ('Apple', 'Fruit'),
        ('Banana', 'Fruit'),
        ('Blueberries', 'Fruit'),
        ('Kiwi', 'Fruit'),
        ('Lemon', 'Fruit'),
        ('Lime', 'Fruit'),
        ('Mango', 'Fruit'),
        ('Melon', 'Fruit'),
        ('Nectarine', 'Fruit'),
        ('Orange', 'Fruit'),
        ('Peach', 'Fruit'),
        ('Raspberries', 'Fruit'),
        ('Strawberries', 'Fruit'),
        ('Watermelon', 'Fruit'),
        # Grains
        ('Amaranth, extruded', 'Grains'),
        ('Barley', 'Grains'),
        ('Buckwheat', 'Grains'),
        ('Gluten', 'Grains'),
        ('Millet', 'Grains'),
        ('Millet flakes', 'Grains'),
        ('Oats', 'Grains'),
        ('Popcorn', 'Grains'),
        ('Quinoa', 'Grains'),
        ('Quinoa flakes', 'Grains'),
        ('Rice', 'Grains'),
        ('Teff flakes', 'Grains'),
        # Greens
        ('Basil', 'Greens'),
        ('Coriander', 'Greens'),
        ('Dill', 'Greens'),
        ('Lamb\'s lettuce (roszponka)', 'Greens'),
        ('Parsley', 'Greens'),
        ('Romaine lettuce', 'Greens'),
        ('Spinach', 'Greens'),
        # Liquid
        ('Apple cider vinegar', 'Liquid'),
        ('Broth', 'Liquid'),
        # Nuts
        ('Almond butter', 'Nuts'),
        ('Brazil', 'Nuts'),
        ('Cacao 100%', 'Nuts'),
        ('Cashew butter', 'Nuts'),
        ('Cashews', 'Nuts'),
        ('Chocolate >85% Lindt (~10g)', 'Nuts'),
        ('Macadamia', 'Nuts'),
        ('Peanut butter', 'Nuts'),
        ('Peanut powder', 'Nuts'),
        ('Pistachio', 'Nuts'),
        ('Walnuts', 'Nuts'),
        # Protein
        ('Anchovies', 'Protein'),
        ('Beef, lamb or veal', 'Protein'),
        ('Chickpeas', 'Protein'),
        ('Eggs', 'Protein'),
        ('Liver (chicken or turkey)', 'Protein'),
        ('Oily fish', 'Protein'),
        ('Pea powder', 'Protein'),
        ('Red lentils', 'Protein'),
        ('Shellfish', 'Protein'),
        ('Tofu', 'Protein'),
        ('Tuna', 'Protein'),
        ('Turkey or chicken', 'Protein'),
        ('White fish', 'Protein'),
        # Sauce
        ('Tomato sauce', 'Sauce'),
        # Seeds
        ('Cardamon', 'Seeds'),
        ('Chia', 'Seeds'),
        ('Flaxseeds', 'Seeds'),
        ('Mustard', 'Seeds'),
        ('Pumpkin', 'Seeds'),
        ('Sunflower', 'Seeds'),
        ('Tahini', 'Seeds'),
        # Spices
        ('Basil', 'Spices'),
        ('Bay leaves', 'Spices'),
        ('Black pepper', 'Spices'),
        ('Cinnamon', 'Spices'),
        ('Cloves', 'Spices'),
        ('Coriander', 'Spices'),
        ('Cumin', 'Spices'),
        ('Garam masala', 'Spices'),
        ('Garlic powder', 'Spices'),
        ('Ginger', 'Spices'),
        ('Marjoram', 'Spices'),
        ('Nutmeg', 'Spices'),
        ('Onion powder', 'Spices'),
        ('Oregano', 'Spices'),
        ('Other spices', 'Spices'),
        ('Rosemary', 'Spices'),
        ('Star anise', 'Spices'),
        ('Thyme', 'Spices'),
        ('Turmeric', 'Spices'),
        # Sweet
        ('Dates', 'Sweet'),
        ('Honey', 'Sweet'),
        # Veggies
        ('Avocado', 'Veggies'),
        ('Broccoli', 'Veggies'),
        ('Carrot', 'Veggies'),
        ('Cauliflower', 'Veggies'),
        ('Celery', 'Veggies'),
        ('Eggplant', 'Veggies'),
        ('Fennel', 'Veggies'),
        ('Garlic', 'Veggies'),
        ('Ginger', 'Veggies'),
        ('Leek', 'Veggies'),
        ('Mushrooms', 'Veggies'),
        ('Onion', 'Veggies'),
        ('Potato', 'Veggies'),
        ('Tomato', 'Veggies'),
        ('Zucchini', 'Veggies'),
    ]

    # Add each food item to the database
    for name, category in foods:
        food = Food(name=name, category=category)
        db.session.add(food)

    db.session.commit()
    print("Food data added to the database.")

if __name__ == '__main__':
    populate_food_data()
