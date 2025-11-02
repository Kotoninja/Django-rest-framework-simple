from django.urls import path, include
from people import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"people", views.PeopleViewSet)


urlpatterns = [path("", include(router.urls))]
