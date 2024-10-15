from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_meal_info(meal_items):
    html_parts = []
    prev_station = ""
    meal_count = 0
    
    for item in meal_items:
        if str(item.station) != "None":
            if item.station != prev_station:
                # Close the previous accordion if there was one
                if prev_station:
                    html_parts.append('</div>')  # Close previous panel div
                
                # Add new accordion button and panel
                html_parts.append(f'''
                    <button class="accordion">{item.station}</button>
                    <div class="panel">
                ''')
                prev_station = item.station
                meal_count = 0  # Reset meal count for the new station

            description = item.description if item.description != "" else "No description available"
            html_parts.append(f'''
            <div class="meal-item">
                <div class="meal-header">
                    <p class="meal-name">{item.name}</p>
                    <button onclick="toggleDescription(this);" class="toggle-button">+</button>
                </div>
                <div style="display: none;">
                    <p class="meal-description">{description}</p>
                </div>
            </div>
            ''')
            
            # Add red dotted line after each item except the last one
            meal_count += 1
            if meal_count < len(meal_items):
                html_parts.append('<hr class="dashed-line">')
    
    # Close the last panel if there are items
    if prev_station:
        html_parts.append('</div>')
    
    return mark_safe(''.join(html_parts))