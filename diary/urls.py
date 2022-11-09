from django.urls import path
from diary import views

urlpatterns = [
    path("", views.memory_list),
    path("<int:pk>/", views.memory_detail),
    path("new/", views.memory_new),
    path("<int:pk>/edit/", views.memory_edit),
    path("<int:pk>/delete/", views.memory_delete),
    path("gallery/", views.gallery),
    path("calendar/", views.calendar),
    path("info/", views.info),
    path("select/", views.select),
]
