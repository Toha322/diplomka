from django.shortcuts import render

from django.shortcuts import render

def profile_page(request):
    return render(request,'profiles/profile.html')