from rest_framework.routers import DefaultRouter
from home_app.api.views import ContactformVS
from django.urls import path, include

router = DefaultRouter()
router.register('contactform', ContactformVS, basename = 'contactform')

urlpatterns = [
    path('', include(router.urls)),
]
