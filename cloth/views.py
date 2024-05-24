from django.shortcuts import render
from django.views import generic
from . import models


class AllClothView(generic.ListView):
    template_name = 'cloth/all_cloth.html'
    context_object_name = 'cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


# def all_cloth(request):
#     if request.method == 'GET':
#         cloth = models.Cloth.objects.filter().order_by('-id')
#         return render(request, template_name='cloth/all_cloth.html', context={'cloth': cloth})


class MaleClothView(generic.ListView):
    template_name = 'cloth/male.html'
    context_object_name = 'male'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='мужская одежда').order_by('-id')


# def male_cloth(request):
#     if request.method == 'GET':
#         male = models.Cloth.objects.filter(tags__name='мужская одежда').order_by('-id')
#         return render(request, template_name='cloth/male.html',
#                       context={'male': male})


class FemaleClothView(generic.ListView):
    template_name = 'cloth/female.html'
    context_object_name = 'female'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='женская одежда').order_by('-id')


# def female_cloth(request):
#     if request.method == 'GET':
#         female = models.Cloth.objects.filter(tags__name='женская одежда').order_by('-id')
#         return render(request, template_name='cloth/female.html',
#                       context={'female': female})


class KidsClothView(generic.ListView):
    template_name = 'cloth/kids.html'
    context_object_name = 'kids'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='детская одежда').order_by('-id')


# def kids_cloth(request):
#     if request.method == 'GET':
#         kids = models.Cloth.objects.filter(tags__name='детская одежда').order_by('-id')
#         return render(request, template_name='cloth/kids.html',
#                       context={'kids': kids})



