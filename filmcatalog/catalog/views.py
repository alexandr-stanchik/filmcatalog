from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import generic

from .models import *
from .forms import UserRegistrationForm, FilmInstanceEdit


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def index(request):
    num_films = Film.objects.all().count()
    num_directors = Director.objects.count()  # сокращенно
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'catalog/index.html',
        context={'num_films': num_films,
                 'num_directors': num_directors,
                 'num_visits': num_visits,
                 },
    )


class FilmListView(generic.ListView):
    model = Film
    paginate_by = 10


class DirectorListView(generic.ListView):
    model = Director
    paginate_by = 10


class DirectorDetailView(generic.DetailView):
    model = Director

    # film =
    def get_context_data(self, **kwargs):
        context = super(DirectorDetailView, self).get_context_data(**kwargs)
        context['film_list'] = Film.objects.filter(director=self.kwargs['pk'])
        return context


def film_detail(request, pk):
    data = {'status': {'name': 'status'},
            'tracked_status': {'name': 'tracked_status',
                               'tracked': 'tracked',
                               'untracked': 'untracked'},
            }
    film = Film.objects.get(pk=pk)

    if request.method == 'POST':
        if data['status']['name'] in request.POST:
            new_status = request.POST['status']
            try:
                film_instance = FilmInstance.objects.filter(film=film).get(viewer=request.user.pk)
                film_instance.set_status(new_status)
                film_instance.save()
            except ObjectDoesNotExist:
                film_instance = FilmInstance()
                film_instance.film = film
                film_instance.viewer = User.objects.get(pk=request.user.pk)
                film_instance.set_status(new_status)
                film_instance.save()
        elif data['tracked_status']['name'] in request.POST:
            try:
                film_instance = FilmInstance.objects.filter(film=film).get(viewer=request.user.pk)
                film_instance.delete()
            except ObjectDoesNotExist:
                film_instance = FilmInstance()
                film_instance.film = film
                film_instance.viewer = User.objects.get(pk=request.user.pk)
                film_instance.save()

    film = Film.objects.get(pk=pk)
    form = FilmInstanceEdit()
    status = ""
    tracked_status = data['tracked_status']['untracked']
    try:
        status = FilmInstance.objects.filter(film=film).get(viewer=request.user.pk).get_status()
        tracked_status = data['tracked_status']['tracked']
    except ObjectDoesNotExist:
        print(ObjectDoesNotExist.args)
    context = {
        'filminstance_status': status,
        'film': film,
        'form': form,
        'tracked_status': tracked_status,
        'data': data,
    }
    return render(request, "catalog/film_detail.html", context)


class TrackedFilmsByUserListView(LoginRequiredMixin, generic.ListView):
    model = FilmInstance
    template_name = 'catalog/film-instance_list_viewer_user.html'
    paginate_by = 10

    def get_queryset(self):
        return FilmInstance.objects.filter(viewer=self.request.user)
