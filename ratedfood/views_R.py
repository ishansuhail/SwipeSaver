from django.shortcuts import render
from .models import ratedFoodItem

from django.http import HttpResponse
from django.template import loader
from PIL import Image, ImageDraw, ImageFont
import io


# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def commons(request):
    return render(request, 'commons.html')

def contact(request):
	
	form = ContactFormForm
	return render(request, 'contact.html', {'form':form})

def about(request):
	return render(request, 'contact.html')


def ratedfood(request):
    displayALL = ratedFoodItem.objects.all()
    return render(request, 'ratedfood.html', {'displayALL': displayALL})

def ratedfood_high(request):
	displayALL = ratedFoodItem.objects.all()
	return render(request, 'ratedfood_high.html', {'displayALL': displayALL})

def ratedfood_low(request):
	displayALL = ratedFoodItem.objects.all()
	return render(request, 'ratedfood_low.html', {'displayALL': displayALL})

def ratedfood_vegan(request):
	displayALL = ratedFoodItem.objects.all()
	return render(request, 'ratedfood_vegan.html', {'displayALL': displayALL})

def display_FOOD(request):
	display_FOOD = ratedFoodItem.objects.all()
	return render(request, 'display_FOOD.html', {'display_FOOD': display_FOOD})

def ratedfood_commons(request):
	displayALL = ratedFoodItem.objects.all()
	return render(request, 'ratedfood_commons.html', {'displayALL': displayALL})


def simple_image(request):
	return render(request, 'salad.jpg')
def generate_image(request):

	base_image = Image.open('salad_oCO7XyP.jpg')

	# Resize the image to thumbnail dimensions
	thumbnail_size = (1280, 720)  # Example dimensions, adjust as needed
	base_image.thumbnail(thumbnail_size)

	# Create a drawing object
	draw = ImageDraw.Draw(base_image)

	# Load a font for the text overlay (you'll need to provide the path to your font)
	font = ImageFont.truetype('static/Rubber-Duck.ttf', 36)

	# Define the text and position
	text = "temp"
	text_position = (20, 20)  # Example position, adjust as needed

	# Add the text overlay to the image
	draw.text(text_position, text, fill=(255, 255, 255), font=font)

	# Round the corners of the image
	radius = 50  # Adjust the radius as needed
	mask = Image.new('L', base_image.size, 0)
	draw_mask = ImageDraw.Draw(mask)
	draw_mask.rectangle((0, 0, base_image.width, base_image.height), fill=255)
	draw_mask.ellipse((0, 0, 2 * radius, 2 * radius), fill=0)
	draw_mask.ellipse((0, base_image.height - 2 * radius, 2 * radius, base_image.height), fill=0)
	draw_mask.ellipse((base_image.width - 2 * radius, 0, base_image.width, 2 * radius), fill=0)
	draw_mask.ellipse((base_image.width - 2 * radius, base_image.height - 2 * radius, base_image.width, base_image.height), fill=0)
	base_image.putalpha(mask)

	# Save the final image to a buffer
	image_buffer = io.BytesIO()
	base_image.save(image_buffer, format='PNG')  # Use PNG format to preserve transparency

	# Return the image as an HTTP response
	response = HttpResponse(image_buffer.getvalue(), content_type='image/png')
	return response