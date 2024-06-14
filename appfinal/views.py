from django.shortcuts import render

def mainView(request):
    return render(request, 'mainView.html')