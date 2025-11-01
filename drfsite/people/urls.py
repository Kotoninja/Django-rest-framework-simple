from django.urls import path
from people import views


urlpatterns = [
    path("people/", views.PeopleListCreateAPI.as_view()),
    path("people/<int:pk>/", views.PeopleAPIUpdate.as_view()),
    path(
        "people/detail/<int:pk>/",
        views.PeopleAPIDetail.as_view(),
    ),
]
