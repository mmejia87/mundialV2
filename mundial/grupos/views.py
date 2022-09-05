from django.http import HttpResponse
from django.shortcuts import render

from grupos.models import Grupos


# Create your views here.
def grupos(request):

    groupA= Grupos.objects.filter(grupo='A')
    groupB= Grupos.objects.filter(grupo='B')
    groupC= Grupos.objects.filter(grupo='C')
    groupD= Grupos.objects.filter(grupo='D')
    groupE= Grupos.objects.filter(grupo='E')
    groupF= Grupos.objects.filter(grupo='F')
    groupG= Grupos.objects.filter(grupo='G')
    groupH= Grupos.objects.filter(grupo='H')

    return render(request,'plantilla_grupo.html',{'groupA':groupA,'groupB':groupB,'groupC':groupC,'groupD':groupD,
                        'groupE':groupE,'groupF':groupF,'groupG':groupG,'groupH':groupH})