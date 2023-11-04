from django.contrib import admin
from django.urls import path
from mob_number_checker.views import main, verification, verification_completed

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main),
    path("verification-<int:pk>", verification),
    path("verification_completed", verification_completed),
]
