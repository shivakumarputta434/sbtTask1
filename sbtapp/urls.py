from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('home',views.home,name='home'),
    path('empdata',views.EmpData.as_view(),name='empdata'),
    path('empdata/<int:id>',views.EmpData.as_view(),name='empdata'),
    path('obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]