from django.shortcuts import render
from .models import Customer
from django.http import HttpResponseRedirect
from django.contrib import messages

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
    if request.method == 'POST':
        first = request.POST['InputFirst']
        last = request.POST['InputLast']
        phone = request.POST['InputPhone']
        address = request.POST['InputAddress']

        obj = Customer(pk=id, first=first, last=last, phone=phone, address=address)
        obj.save()
        messages.success(request,'Updated')
        return HttpResponseRedirect('/')

    object = Customer.objects.get(pk=id)
    return render(request, 'update.html',context={'object':object})


def delete(request, id):
    obj = Customer.objects.get(pk=id)
    obj.delete()
    messages.success(request, 'Deleted')
    return HttpResponseRedirect('/')