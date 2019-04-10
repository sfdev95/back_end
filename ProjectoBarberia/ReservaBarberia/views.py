from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from ReservaBarberia.forms import ReservaForm
def home (request):
    context = {'foo': 'bar'}
    return render(request,'base.html',context)
    
def ejemplo(request):
    context = {'foo': 'bar'}
    titulo = 'Django vive en codigo'
    nombre = 'Pasando variables en Django'
    lista =[2,3,5,65,78,98,234,567,876]
    return render(request,'ejemplo.html',{'title':titulo,'nombre':nombre,'lista':lista},context)
    

def index (request):
    return render (request,'reservas/index.html')


def reserva_view (request):
    if request.method == "POST":
        form =ReservaForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'reservas/index.html',{'form':form})

        else:
            form = ReservaForm()
            return render(request,'reservas/reserva_form.html',{'form':form})


# Create your views here.
