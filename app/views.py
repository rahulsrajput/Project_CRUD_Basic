from django.shortcuts import render
from .models import Customer
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        first = request.POST['InputFirst']
        last = request.POST['InputLast']
        phone = request.POST['InputPhone']
        address = request.POST['InputAddress']
        # print(f'{first},{last},{phone},{address}')

        obj = Customer(first=first, last=last, phone=phone, address=address)
        obj.save()
        return HttpResponseRedirect('/')

    customers_objs = Customer.objects.all()
    return render(request,'home.html',context={'customers_objs':customers_objs})


def update(request, id):
    pass


def delete(request, id):
    pass