from django.shortcuts import render

def welcome_page_view(request):
    # Django automatically looks inside your app's 'templates' folder
    return render(request, 'welcome.html')

def home_page_view(request):
    # Django automatically looks inside your app's 'templates' folder
    return render(request, 'home.html')