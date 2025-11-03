from django.urls import path, include
from people import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"people", views.PeopleViewSet)
print(router.urls)

urlpatterns = [path("", include(router.urls))]
