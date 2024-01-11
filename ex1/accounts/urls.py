from django.urls import path
from . import views
# app_name="travello"
urlpatterns = [

    path('register/',views.register,name='register'),
    # path('returnback/',views.returnback,name='returnback')

]