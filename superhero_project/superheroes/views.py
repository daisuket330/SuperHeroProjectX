from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all heroes': all_heroes
    }
    return render(request,'superheroes/index.html',context)

def detail(request, hero_id):
        single_hero = Superhero.objects.get(pk=hero_id)
        context = {
            'single_hero': single_hero
        }
        return(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        print("hit with post")
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchprhse = request.POST.get('catchprhse')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary=primary, secondary=secondary, catchprhse=catchprhse)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))

    else:
        return render(request, 'superheroescreate.html')
