import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_message = response['choices'][0]['message']['content']

        return JsonResponse({"message": bot_message})

    return JsonResponse({"error": "Invalid request"}, status=400)
