from django.shortcuts import render
from .models import Customer
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.core.paginator import Paginator
import csv

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

    customers_objs = Customer.objects.all().order_by('id')
    paginator = Paginator(customers_objs,5)
    # print(paginator)

    page_number = request.GET.get('page')
    print(page_number)

    page_obj = paginator.get_page(page_number)
    print(page_obj)

    return render(request,'home.html',context={'page_obj':page_obj})


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


def csv_(request):
    try:
        if request.method == "POST":
            file = request.FILES['UploadCSV'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                Customer.objects.create(
                first = row['first'],
                last = row['last'],
                phone = row['phone'],
                address = row['address']
                )
            messages.success(request, 'Imported')
            return HttpResponseRedirect('/')
        
        return render(request, 'csv.html')
    
    except Exception:
        messages.error(request, 'Invalid document')
        return HttpResponseRedirect('/')