from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_meal_info(meal_items):
    html_parts = []  # Use a list to collect parts
    prev_station = ""
    
    for item in meal_items:
        if str(item.station) != "None":
            if item.station != prev_station:
                html_parts.append(f'''
                    <p class="station-style">{item.station}</p>         
                ''')
                prev_station = item.station

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
    
    return mark_safe(''.join(html_parts))