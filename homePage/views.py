from django.shortcuts import render

# Create your views here.

def welcome_page(request):

	return render(request, 'welcome_page.html')

def experience(request):

	return render(request, 'experience.html')

