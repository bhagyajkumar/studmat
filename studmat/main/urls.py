from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view),
    path("<unv_name>/", views.university_view),
    path("<unv_name>/<slug>", views.branch_view)
]