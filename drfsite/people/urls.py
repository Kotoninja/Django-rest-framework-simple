from django.urls import path
from people import views


urlpatterns = [
    path("people/", views.PeopleViewSet.as_view({"get":"list"})),
    path("people/<int:pk>/", views.PeopleViewSet.as_view({"put":"update"})),
]
