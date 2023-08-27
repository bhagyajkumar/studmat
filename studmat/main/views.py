from django.shortcuts import render, get_object_or_404
from . import models


def home_view(request):
    universities = models.University.objects.all()
    return render(request, "home_view.html", {"universities": universities})

def university_view(request, unv_name):
    university_query = models.University.objects.filter(name=unv_name)
    university = get_object_or_404(university_query)
    branches = models.Branch.objects.filter(university=university)
    return render(request, "university_view.html", {"unv_name": unv_name, "branches": branches})

def branch_view(request, unv_name, slug):
    university_query = models.University.objects.filter(name=unv_name)
    university = get_object_or_404(university_query)
    branch = get_object_or_404(models.Branch.objects.filter(university=university, slug=slug))
    print(branch)

def semester_view(request, unv_name, slug, sem):
    pass
    