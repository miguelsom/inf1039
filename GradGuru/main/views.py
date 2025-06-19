from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'main/main_page.html')

def disciplinas(request):
    return render(request, 'main/disciplinas.html')

