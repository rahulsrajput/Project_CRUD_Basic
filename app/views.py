from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def update(request, id):
    pass


def delete(request, id):
    pass