from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("image_classification.urls")),
    path("image_classification/", include("image_classification.urls")),
]