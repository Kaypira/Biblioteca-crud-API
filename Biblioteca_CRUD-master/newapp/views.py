from django.shortcuts import redirect, render, get_object_or_404
from .models import Member
from datetime import datetime


def index(request):
    mem = Member.objects.all()
    return render(request, 'index.html', {'mem': mem})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    title = request.POST['title']
    author = request.POST['author']
    genre = request.POST['genre']
    pages = request.POST['pages']
    publisher = request.POST['publisher']
    published_date = request.POST['published_date']
    mem = Member(title=title, author=author, genre=genre, pages=pages, publisher=publisher, published_date=published_date)
    mem.save()
    return redirect("/")

def delete(request, id):
    mem = get_object_or_404(Member, id=id)
    mem.delete()
    return redirect("/")

def update(request, id):
    mem = get_object_or_404(Member, id=id)
    return render(request, 'update.html', {'mem': mem})

def uprec(request, id):
    title = request.POST['title']
    author = request.POST['author']
    genre = request.POST['genre']
    pages = request.POST['pages']
    publisher = request.POST['publisher']
    published_date = request.POST['published_date']
    
    mem = get_object_or_404(Member, id=id)
    mem.title = title
    mem.author = author
    mem.genre = genre
    mem.pages = pages
    mem.publisher = publisher
    mem.published_date = published_date
    mem.save()
    return redirect("/")
