from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import utils
import io

# Create your views here.

def home(request):
    return render(request, 'home.html')


@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        action = request.POST.get('action')

        if not image_file or not action:
            return JsonResponse({'error': 'Missing data'}, status=400)

        input_bytes = image_file.read()

        try:
            if action == 'remove':
                output_bytes = utils.remove_bg(input_bytes)
            elif action == 'enhance':
                output_bytes = utils.enhance_image(input_bytes)
            else:
                return JsonResponse({'error': 'Invalid action'}, status=400)

            return HttpResponse(output_bytes, content_type='image/png')

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid method'}, status=405)
