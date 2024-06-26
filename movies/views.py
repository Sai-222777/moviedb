from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Movie

# Create your views here.

def moviesList(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query) | Movie.objects.filter(genre__icontains=query)
    else:
        movies = Movie.objects.all()

    paginator = Paginator(movies, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'movies/movies_list.html',{'page_obj':page_obj})

def movieDetail(request,pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})