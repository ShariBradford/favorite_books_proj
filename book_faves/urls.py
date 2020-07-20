from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_books),
    path('<int:book_id>',views.show_book),
    path('new',views.create_book),
    path('<int:book_id>/favorite',views.add_to_favorites),
    path('<int:book_id>/unfavorite',views.remove_from_favorites),
]