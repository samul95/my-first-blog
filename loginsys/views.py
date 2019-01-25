from django.shortcuts import render
from django.shortcuts import redirect

def login(request):
    return render(request, 'loginsys/login.html')


def logout(request):
    return redirect('post_list')

def addnewauth(request):
    return render(request, 'loginsys/addnewauth.html')