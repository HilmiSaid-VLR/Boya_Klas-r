from django.shortcuts import render

from .models import Cihaz

def anasayfa(request):
    cihazlar = Cihaz.objects.all()
    return render(request, 'anasayfa.html', {'cihazlar': cihazlar})

def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def iletisim(request):
    return render(request, 'iletisim.html')