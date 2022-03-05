from django.shortcuts import render

# Create your views here.


def HomeViews (request):
    return render(request, 'index.html')