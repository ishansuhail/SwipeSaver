from django import template
from django.utils.safestring import mark_safe
from collections import defaultdict

register = template.Library()

# Used to dynamically generate the station HTML
@register.simple_tag
def render_meal_info(meal_items, user_ratings, is_authenticated):
    # Group meal items by meal and station
    grouped_meals = defaultdict(lambda: defaultdict(list))
    for item in meal_items:
        if item.station:  # Ensure station is not None or empty
            grouped_meals[item.meal.upper()][item.station].append(item)
    
    
    
    html_parts = []

    # Iterate over meal types (BREAKFAST, LUNCH, DINNER)
    for meal in ["BREAKFAST", "BRUNCH", "LUNCH", "DINNER"]:
        if meal in grouped_meals:
            # Create top-level accordion for each meal
            html_parts.append(f'''
                <button class="accordion">
                    <span class="accordion-text">View Menu</span>
                </button>
                <div class="panel">
            ''')

            # Create station accordions within the meal accordion
            for station, items in grouped_meals[meal].items():
                
                if not station or station.lower() == "none":
                    continue  # Skip None or empty stations

                html_parts.append(f'''             
                     <button class="accordion">
                        <div class="accordion-title">
                            <span class="station-name">{station}</span>
                            <div class="rating-display">
                                <span class="rating-icon">★</span>
                                <span class="rating-score" id="rating-{station}-{meal}"> Unrated </span>
                            </div>
                        </div>
                    </button>
                    <div class="panel">
                ''')
                
                # Add each item for the station
                for item in items:
                    description = item.description.strip() if item.description else "No description available"
                    show_description = item.description and description.lower() != "no description available"
                    
                    allergens = item.allergens if len(item.allergens) > 0 else "No allergens"
                    calories = item.calories.strip()
                    
                    
                    
                    html_parts.append(f'''
                    <div class="meal-item">
                        <div class="meal-header">
                            <p class="meal-name">{item.name} </p>
                            {'<button onclick="toggleDescription(this);" class="toggle-button">+</button>' if show_description else ''}
                            <div style = "color: black; display: flex; flex-direction: row; gap: 10px; margin-left: 10px;">
                                {''.join(f'<div>{allergen["name"]}</div>' if isinstance(allergen, dict) and "name" in allergen else f'<div></div>' for allergen in allergens)}
                            </div>
                            <button onclick=addCalories({calories}) class="calorie-button">{calories}cal</button>
                            
                        </div>
                        
                        {f'<div style="display: none;"><p class="meal-description">{description}</p></div>' if show_description else ''}
                        
                    </div>
                    ''')
                    
                    # Add a red dotted line after each item
                    html_parts.append('<hr class="dashed-line">')
                
                if (is_authenticated):
                    # Get the user's rating for this station and meal, if any
                    user_rating_queryset = user_ratings.filter(station=item.station, meal=item.meal)

                    # Check if the queryset has any ratings
                    if user_rating_queryset.exists():
                        user_rating = user_rating_queryset.first().rating  # Get the first rating
                    else:
                        user_rating = 0  # Default to 0 if no rating

                    # Append the rating information
                    html_parts.append(f'''
                        <div class="rating-section" 
                            data-station="{item.station}" 
                            data-dining-hall="{item.dining_hall}" 
                            data-meal="{item.meal}">
                            <span class="rate-message-style">Rate Station: </span>
                            <div class="star-rating">
                                <button class="star {'selected' if user_rating == 5 else ''}" data-value="5">★</button>
                                <button class="star {'selected' if user_rating == 4 else ''}" data-value="4">★</button>
                                <button class="star {'selected' if user_rating == 3 else ''}" data-value="3">★</button>
                                <button class="star {'selected' if user_rating == 2 else ''}" data-value="2">★</button>
                                <button class="star {'selected' if user_rating == 1 else ''}" data-value="1">★</button>
                            </div>
                        </div>
                        ''')
                
                # Close the station panel
                html_parts.append('</div>')

            # Close the meal panel
            html_parts.append('</div>')
            html_parts.append('</button>')

    return mark_safe(''.join(html_parts))

# Used to properly capitalize dining hall names for HTML
@register.filter
def capitalize_dining_hall_name(value):
    if value:
        return ' '.join(word.capitalize() for word in value.split('-'))
    return value