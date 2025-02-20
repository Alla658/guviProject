from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import FavoriteCity
from .extensions import db
from .weather import get_weather_data

main = Blueprint('main', __name__)


# Home Route (After Login)
@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    weather = None  # Variable to store searched city's weather
    # If user submits a city in the form
    if request.method == 'POST':
        city_name = request.form.get('city')

        if city_name:
            weather = get_weather_data(city_name)
            if weather is None:
                flash("City not found. Please try again.", "danger")

    # Retrieve favorite cities & their weather
    favorite_cities = FavoriteCity.query.filter_by(user_id=current_user.id).all()
    favorite_weather_data = [get_weather_data(city.city_name) for city in favorite_cities]
    return render_template('index.html', weather=weather, favorite_cities=favorite_weather_data)


# Add Favorite City
@main.route('/add_favorite', methods=['POST'])
@login_required
def add_favorite():
    city_name = request.form.get('city_name')

    if not city_name:
        flash("City name is required!", "danger")
        return redirect(url_for('main.home'))

    # Check if city already exists in user's favorites
    existing_fav = FavoriteCity.query.filter_by(user_id=current_user.id, city_name=city_name).first()
    if existing_fav:
        flash(f"{city_name} is already in your favorites!", "warning")
        return redirect(url_for('main.home'))

    new_fav = FavoriteCity(user_id=current_user.id, city_name=city_name)
    db.session.add(new_fav)
    db.session.commit()

    flash(f"{city_name} added to favorites!", "success")
    return redirect(url_for('main.home'))


# Delete Favorite City
@main.route('/delete_favorite/<string:name>', methods=['POST'])
@login_required
def delete_favorite(name):
    favorite = FavoriteCity.query.filter_by(city_name=name, user_id=current_user.id).first_or_404()

    db.session.delete(favorite)
    db.session.commit()

    flash("City removed from favorites!", "success")
    return redirect(url_for('main.home'))
