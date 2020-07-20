from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from  login_app.models import User

# Create your views here.
def show_books(request):
    if (not 'user_id' in request.session.keys()) or (request.session['user_id'] == ''):
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'books': Book.objects.all().order_by('-created_at'),
    }
    return render(request,'books/books.html', context)

def show_book(request,book_id):
    book = Book.objects.get(id=book_id)
    mode = ''

    if book.uploaded_by_id == request.session['user_id']: 
        mode = 'edit'
    else:
        mode = 'view'

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'book': book,
        'mode': mode,
    }

    return render(request,f"/books/show.html", context)

def create_book(request):
    #print(request.POST)
    errors = {}

    errors = Book.objects.basic_validator(request.POST, request.session['user_id'])
    if errors: 
        for k,v in errors.items():
            messages.add_message(request,messages.ERROR,v)
        
    else:
        book = Book.objects.create_book(request.POST, request.session['user_id'])
        book.users_who_like.add(User.objects.get(id=request.session['user_id']))


    return redirect("/books")

def add_to_favorites(request,book_id):
    pass

def remove_from_favorites(request,book_id):
    pass