from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.Login),
    path('home/',views.Home),
    path('logout/',views.Logout),
    path('ChangePassword/',views.ChangePassword)
]
