from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from auth_app.api.views import RegistrationViewSet, LogoutViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('registrationapi', RegistrationViewSet, basename = 'registrationapi')
router.register('logoutapi', LogoutViewSet, basename = 'logoutapi')

urlpatterns = [
    
    path('', include(router.urls)),
    path('loginapi/', obtain_auth_token, name = 'loginapi'),

]
