from django.urls import path, include
from people import views
from rest_framework import routers


urlpatterns = [
    path("people/", views.PeopleAPIList.as_view(),name="people"),
    path("people/<int:pk>/", views.PeopleAPIUpdate.as_view(),name="people"),
    path("peopledelete/<int:pk>/", views.PeopleAPIDelete.as_view(),name="people")
]
