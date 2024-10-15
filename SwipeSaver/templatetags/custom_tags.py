from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_meal_info(meal_items):
    html_parts = []
    prev_station = ""
    
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