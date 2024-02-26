from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        first = request.POST['InputFirst']
        last = request.POST['InputLast']
        phone = request.POST['InputPhone']
        address = request.POST['InputAddress']
        
        # print(f'{first},{last},{phone},{address}')

        
    return render(request,'home.html')


def update(request, id):
    pass


def delete(request, id):
    pass