from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


r =DefaultRouter()
r.register('user',UserView,basename='user')
r.register('profile',ProfileView,basename='profile')
r.register('post',PostView,basename='post')
urlpatterns = [
]+r.urls

# refresh token
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjM5Mjk3NywiaWF0IjoxNzEyMzA2NTc3LCJqdGkiOiJkMTJlNjMzYjczYjY0Mzg2OWRiYzAxMTM4ZWEwZDIzMSIsInVzZXJfaWQiOjR9.ch4zp0BhYAm_uGlSmeJnx4fyq9oy0_DMD_c08Qe8yXk
