from django.urls import path

from .views import signup, login, logout, password_change

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('password/change/',password_change, name='password_change' ),
    path('logout/',logout, name='logout')
]