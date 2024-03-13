from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from . forms import MovieForm
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})

def add_movie(request):
    if request.method=="POST":
        title=request.POST.get('title',)
        desc = request.POST.get('desc', )
        category = request.POST.get('category',)
        date = request.POST.get('date', )
        actors = request.POST.get('actors', )
        trailer_link = request.POST.get('trailer_link', )
        img = request.FILES['img']
        movie=Movie(title=title,desc=desc,category=category,date=date,actors=actors,trailer_link=trailer_link,img=img)
        movie.save()

    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')



# views.py
from .forms import SearchForm

def search(request):
    query = request.GET.get('q')
    results = Movie.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})

