from django.shortcuts import render
from django.http import HttpResponse


from equipos.models import Equipos


# Create your views here.
def equipos(request):
    team= Equipos.objects.count()
    teamE= Equipos.objects.filter(continente='Europeo')
    teamA= Equipos.objects.filter(continente='Asia')
    teamS= Equipos.objects.filter(continente='Sudamerica')
    teamC= Equipos.objects.filter(continente='Centro,Norteamerica')
    teamAf= Equipos.objects.filter(continente='Africa')
    return render(request,'plantilla.html',{'team':team,'teamE':teamE,'teamA':teamA,'teamS':teamS,
                                            'teamC':teamC,'teamAf':teamAf})
def busqueda_equipos(request):
    return render(request,"busqueda.html")




