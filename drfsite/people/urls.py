from django.urls import path
from people import views



urlpatterns = [
    path("people/", views.PeopleAPIView.as_view(),name="home"),
    path("people/<int:pk>/",views.PeopleAPIView.as_view(), name="people_update")
]
