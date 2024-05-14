from django.shortcuts import render
from . import models


def all_cloth(request):
    if request.method == 'GET':
        cloth = models.Cloth.objects.filter().order_by('-id')
        return render(request, template_name='cloth/all_cloth.html', context={'products': cloth})


def male_cloth(request):
    if request.method == 'GET':
        male = models.Cloth.objects.filter(tags__name='мужская одежда').order_by('-id')
        return render(request, template_name='cloth/male.html',
                      context={'male': male})


def female_cloth(request):
    if request.method == 'GET':
        female = models.Cloth.objects.filter(tags__name='женская одежда').order_by('-id')
        return render(request, template_name='cloth/female.html',
                      context={'female': female})


def kids_cloth(request):
    if request.method == 'GET':
        kids = models.Cloth.objects.filter(tags__name='детская одежда').order_by('-id')
        return render(request, template_name='cloth/kids.html',
                      context={'kids': kids})
