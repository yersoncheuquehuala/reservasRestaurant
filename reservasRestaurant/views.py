from django.shortcuts import render

def home_page_view(request):
    # Django automatically looks inside your app's 'templates' folder
    return render(request, 'home.html')