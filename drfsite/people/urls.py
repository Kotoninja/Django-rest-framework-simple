from django.urls import path
from people import views



urlpatterns = [
    path("people/", views.PeopleListCreateAPI.as_view(),name="home"),
    path("people/<int:pk>/",views.PeopleListCreateAPI.as_view(), name="people_update")
]
