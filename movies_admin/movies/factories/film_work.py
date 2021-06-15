import datetime
import random
import uuid

import factory.fuzzy
from movies.factories.person import PersonFactory, RoleFactory
from movies.models import Cast, FilmWork


class FilmWorkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FilmWork
        django_get_or_create = ("uuid",)

    title = factory.Sequence(lambda n: "FilmWork Title {:02}".format(n))
    description = factory.Sequence(lambda n: "FilmWork Description %s" % n)
    creation_date = factory.LazyFunction(datetime.datetime.now)
    certificate = factory.Sequence(lambda n: "FilmWork Certificate %s" % n)
    rating = random.randint(0, 9)
    type = factory.fuzzy.FuzzyChoice(FilmWork.MovieType.choices, getter=lambda c: c[0])
    uuid = uuid.uuid4()

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of genres were passed in, use them
            for genre in extracted:
                self.genres.add(genre)


class CastFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cast
        django_get_or_create = ("person", "film_work", "role")

    person = factory.SubFactory(PersonFactory)
    film_work = factory.SubFactory(FilmWorkFactory)
    role = factory.SubFactory(RoleFactory)
