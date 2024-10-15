from django import template
from django.utils.safestring import mark_safe
from collections import defaultdict

register = template.Library()

@register.simple_tag
def render_meal_info(meal_items):
    # Group meal items by meal and station
    grouped_meals = defaultdict(lambda: defaultdict(list))
    for item in meal_items:
        if item.station:  # Ensure station is not None or empty
            grouped_meals[item.meal.upper()][item.station].append(item)
    
    html_parts = []

    # Iterate over meal types (BREAKFAST, LUNCH, DINNER)
    for meal in ["BREAKFAST", "LUNCH", "DINNER"]:
        if meal in grouped_meals:
            # Create top-level accordion for each meal
            html_parts.append(f'''
                <button class="accordion">{meal.capitalize()}</button>
                <div class="panel">
            ''')

            # Create station accordions within the meal accordion
            for station, items in grouped_meals[meal].items():
                if not station or station.lower() == "none":
                    continue  # Skip None or empty stations

                html_parts.append(f'''
                    <button class="accordion">{station}</button>
                    <div class="panel">
                ''')
                
                # Add each item for the station
                for item in items:
                    description = item.description.strip() if item.description else "No description available"
                    show_description = item.description and description.lower() != "no description available"
                    
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
                
                # Close the station panel
                html_parts.append('</div>')

            # Close the meal panel
            html_parts.append('</div>')

    return mark_safe(''.join(html_parts))
