from django.shortcuts import render
from .models import Movies
from django.db import IntegrityError

# Create your views here.
def populate_data(request):
    resume = list()
    try:
        movie_1 = Movies(episode_nb=1, title="The Phantom Menace", director="George Lucas", producer="Rick McCallum",
                      release_date="1999-05-19")
        movie_1.save()
        resume.append("Ok")
    except IntegrityError as e:
        resume.append("The Phantom Menace:")
        resume.append(e)
    try:
        movie_2 = Movies(episode_nb=2, title="Attack of the Clones", director="George Lucas", producer="Rick McCallum",
                  release_date="2002-05-16")
        movie_2.save()
        resume.append("Ok")
    except IntegrityError as e:
        resume.append("Attack of the Clones:")
        resume.append(e)
    try:
        movie_3 = Movies(episode_nb=3, title="Revenge of the Sith", director="George Lucas", producer="Rick McCallum",
                  release_date="2005-05-19")
        movie_3.save()
        resume.append("Ok")
    except IntegrityError as e:
        resume.append("Revenge of the Sith:")
        resume.append(e)
    try:
        movie_4 = Movies(episode_nb=4, title="A New Hope", director="George Lucas", producer="Gary Kurtz, Rick McCallum",
                  release_date="1977-05-25")
        movie_4.save()
        resume.append("Ok")
    except IntegrityError as e:
        resume.append("A New Hope:")
        resume.append(e)
        print(e)
    try:
        movie_5 = Movies(episode_nb=5, title="The Empire Strikes Back", director="George Lucas", producer="Gary Kutz, Rick McCallum",
                  release_date="1980-05-17")
        movie_5.save()
        resume.append("Ok")
    except IntegrityError as e:
        resume.append("The Empire Strikes Back:")
        resume.append(e)
    try:
        movie_6 = Movies(episode_nb=6, title="Return of the Jedi", director="Richard Marquand", producer="Howard G. Kazanjian, George Lucas, Rick McCallum",
                  release_date="1983-05-25")
        movie_6.save()
        resume.append("Ok")
    except IntegrityError as e:
        resume.append("Return of the Jedi:")
        resume.append(e)
    try:
        movie_7 = Movies(episode_nb=7, title="The Force Awakens", director="J. J. Abrams", producer="Kathleen Kennedy, J. J. Abrams, Bryan Burk",
                  release_date="2015-12-11")
        movie_7.save()
        resume.append("Ok")
    except IntegrityError as e:
        resume.append("The Force Awakens:")
        resume.append(e)
    return render(request, "ex03/populate.html", {"resume": resume})

def display_data(request):
    data = Movies.objects.all()
    return render(request, "ex03/display.html", {"data": data})
