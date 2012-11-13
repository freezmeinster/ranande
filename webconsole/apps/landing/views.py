from django.shortcuts import render_to_response

def login(request):
    return render_to_response('unicorn/html/login.html')