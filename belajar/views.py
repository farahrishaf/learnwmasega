from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse(request.user.username)

def belajar(request):
    users = User.objects.filter(username__icontains='a')
    return render(request, 'belajar.html', {'users' : users})