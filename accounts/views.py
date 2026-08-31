from django.shortcuts import render

# Create your views here.
def login_views(request):
    return render(request,'account/login.html')
# def logout_views(request):
    return render(request,'account/logout.html')
def signup_views(request):
    return render(request,'account/signup.html')
