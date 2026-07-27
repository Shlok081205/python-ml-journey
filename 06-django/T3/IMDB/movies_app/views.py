from django.shortcuts import render, redirect
from .models import Movie

# View 1: Handle the form to add a new movie
def add_movie(request):
    if request.method == "POST":
        # Get the data from the HTML form
        movie_name = request.POST.get('name')
        movie_rating = request.POST.get('rating')
        
        # Save it to the database!
        Movie.objects.create(name=movie_name, rating=movie_rating)
        
        # Redirect the user to the movie list page after saving
        return redirect('movie_list')
        
    # If it's a GET request, just show the empty form
    return render(request, 'add_movie.html')

# View 2: Fetch all movies and display them
def movie_list(request):
    # Grab all movies from the database
    all_movies = Movie.objects.all()
    
    # Send them to the HTML template
    context = {'movies': all_movies}
    return render(request, 'movie_list.html', context)

def search_movies(request):
    # Get the search term from the URL (e.g., ?q=batman)
    query = request.GET.get('q')
    
    # If the user typed something, filter the database
    if query:
        # __icontains looks for partial, case-insensitive matches
        movies = Movie.objects.filter(name__icontains=query)
    else:
        # If the search box is empty, don't show any movies
        movies = None

    context = {
        'movies': movies,
        'query': query  # Pass the query back so we can show what they searched for
    }
    
    return render(request, 'search_movies.html', context)