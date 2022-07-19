from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.pk)])


    def __str__(self):
        return f'{self.last_name} {self.first_name}'


# получить статус фильма относительно ида пользователя. Статус фильма можно взять у ИнстанцииФильма
# инстация фильма знает статус по иду. можно лил полу
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the film")
    year = models.CharField(max_length=4)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    def display_genre_all(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    @classmethod
    def get_status_list(cls):
        all_status_list = []
        for i in FilmInstance.STATUS:
            all_status_list.append(i[1])
        return all_status_list


class FilmInstance(models.Model):
    film = models.ForeignKey(Film, on_delete=models.SET_NULL, null=True)
    viewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    STATUS = (
        ('w', 'Want to see'),
        ('a', 'Want to see again'),
        ('c', 'Completed'),
        ('n', "Haven't see"),
    )

    MARK = tuple((str(i), str(i)) for i in range(1, 6))

    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='w')

    mark = models.CharField(max_length=2, choices=MARK, blank=True, default='')

    def get_status(self):
        status = self.status
        for i in self.STATUS:
            if self.status == i[0]:
                status = i[1]
        return status

    def set_status(self, st):
        for i in self.STATUS:
            if i[1] == st:
                self.status = i[0]

    @classmethod
    def get_status_list(cls):
        all_status_list = []
        for i in cls.STATUS:
            all_status_list.append(i[1])
        return all_status_list

    def __str__(self):
        return f'{self.id} {self.film.title} {self.get_status()} '
