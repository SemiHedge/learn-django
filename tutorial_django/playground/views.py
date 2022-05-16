from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate():
    x = 2
    y = 3
    return x * y

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Semi'})