from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_meal_info(meal_items, user_ratings):
    html_parts = []
    prev_station = ""
    
    for item in meal_items:
        if str(item.station) != "None":
            if item.station != prev_station:

                # Close the previous accordion if there was one
                if prev_station:
                     # Get the user's rating for this station and meal, if any
                    user_rating_queryset = user_ratings.filter(station=item.station, meal=item.meal)

                    # Check if the queryset has any ratings
                    if user_rating_queryset.exists():
                        user_rating = user_rating_queryset.first().rating  # Get the first rating
                    else:
                        user_rating = 0  # Default to 0 if no rating

                    # Append the rating information
                    html_parts.append(f'''
                        <div class="rating-section" data-station={item.station} data-dining-hall={item.dining_hall} data-meal={item.meal}>
                            <span class="meal-title">Rate Station: </span>
                            <div class="star-rating">
                                <button class="star {'selected' if user_rating == 5 else ''}" data-value="5">★</button>
                                <button class="star {'selected' if user_rating == 4 else ''}" data-value="4">★</button>
                                <button class="star {'selected' if user_rating == 3 else ''}" data-value="3">★</button>
                                <button class="star {'selected' if user_rating == 2 else ''}" data-value="2">★</button>
                                <button class="star {'selected' if user_rating == 1 else ''}" data-value="1">★</button>
                            </div>
                        </div>
                        ''')

                    # Attach star ratings for previous station
                    html_parts.append('</div>')  # Close previous panel div
                
                # Add new accordion button and panel
                html_parts.append(f'''
                    <button class="accordion">{item.station}</button>
                    <div class="panel">
                ''')
                prev_station = item.station

            # Safely check if the description is meaningful
            description = item.description.strip() if item.description else "No description available"
            show_description = item.description and description.lower() != "no description available"
            
            # Add the meal item, only show the button and description if `show_description` is True
            html_parts.append(f'''
            <div class="meal-item">
                <div class="meal-header">
                    <p class="meal-name">{item.name}</p>
                    {'<button onclick="toggleDescription(this);" class="toggle-button">+</button>' if show_description else ''}
                </div>
                {f'<div style="display: none;"><p class="meal-description">{description}</p></div>' if show_description else ''}
            </div>
            ''')

            # Add a red dotted line after each item
            html_parts.append('<hr class="dashed-line">')

    # Close the last panel if there are items
    if prev_station:
        html_parts.append('</div>')
    
    return mark_safe(''.join(html_parts))