from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
# from .api import api
from tracks.api import tracksApi


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/", api.urls),
    path("tracks/", tracksApi.urls),
]