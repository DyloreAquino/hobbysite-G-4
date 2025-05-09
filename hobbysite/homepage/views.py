from django.shortcuts import render

def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)

# Create your views here.
