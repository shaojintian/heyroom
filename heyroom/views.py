
from django.shortcuts import render_to_response

def show_index(request):
    return render_to_response('heyroom/index.html')

