from django.shortcuts import render
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from openai import OpenAI


openai.api_key = settings.OPENAI_API_KEY

client = OpenAI(
    # This is the default and can be omitted
    api_key=openai.api_key
)



@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(f"this is the data", data)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": data.get("message")}]
        )
        
        print(response.choices[0].message.content)
        
        
        return JsonResponse({"message": response.choices[0].message.content}, status= 200)

    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def chatbot(request):
    return render(request, 'chatbot.html')