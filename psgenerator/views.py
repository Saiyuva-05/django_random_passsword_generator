from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'home.html')

def passw(request):
    gpassword=''
    characters=list('abcdefgijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*)_+~'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    length=int(request.GET.get('length'))
    for i in range(length):
        gpassword+=random.choice(characters)
    return render(request,'pass.html',{'password':gpassword})
