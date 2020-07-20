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
