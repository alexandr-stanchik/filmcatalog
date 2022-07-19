# from django.conf.urls import url
from django.template.defaulttags import url
from django.urls import path, include

from catalog.views import *

urlpatterns = [
    path('', index, name='index'),
    path('movies/', FilmListView.as_view(), name='films'),  # Movie
    path('movie/<int:pk>/', film_detail, name='film-detail'),
    path('my-movies/', TrackedFilmsByUserListView.as_view(), name='my-films'),
    path('directors/', DirectorListView.as_view(), name='directors'),  # Director
    path('director/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('accounts/registration/', register, name='registration'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),

    # url(r'^$', index, name='index'),
    # url(r'^books/$', views.BookListView.as_view(), name='books'),
]
