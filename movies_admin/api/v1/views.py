from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import CharField, F, Q, Value
from django.db.models.functions import Concat
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from movies.models import FilmWork, Role


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ["get"]

    def get_queryset(self):
        return (
            FilmWork.objects.order_by("-rating")
            .values("title", "description", "creation_date", "rating", "type")
            .annotate(
                id=F("uuid"),
                genres=ArrayAgg("genres__genre"),
                actors=ArrayAgg(
                    Concat("people__first_name", Value(" "), "people__last_name", output_field=CharField()),
                    filter=Q(cast__role__role=Role.RoleType.ACTOR),
                ),
                directors=ArrayAgg(
                    Concat("people__first_name", Value(" "), "people__last_name", output_field=CharField()),
                    filter=Q(cast__role__role=Role.RoleType.DIRECTOR),
                ),
                writers=ArrayAgg(
                    Concat("people__first_name", Value(" "), "people__last_name", output_field=CharField()),
                    filter=Q(cast__role__role=Role.RoleType.WRITER),
                ),
            )
        )

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class Movies(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        page_size = self.get_paginate_by(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                "count": paginator.count,
                "total_pages": paginator.num_pages,
                "prev": page.previous_page_number() if page.has_previous() else None,
                "next": page.next_page_number() if page.has_next() else None,
            }
        else:
            context = {"count": None, "total_pages": None, "prev": None, "next": None}

        context["result"] = list(queryset)
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def get_context_data(self, *, object_list=None, **kwargs):
        film_work = self.get_object()
        return film_work
