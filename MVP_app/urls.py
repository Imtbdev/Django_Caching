from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", views.non_cached_view, name="non_cached"),
    path("per-view-cached/", views.per_view_cached_view, name="per_view_cached"),
    path("cached/", views.cached_view, name="cached"),
    path("filesystem-cached/", views.filesystem_cached_view, name="filesystem_cached"),
    path("database-cached/", views.database_cached_view, name="database_cached"),
    path("dummy-cached/", views.dummy_cached_view, name="dummy_cached"),
]
