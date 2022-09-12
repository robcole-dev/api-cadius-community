from django.urls import path
from servers import views


urlpatterns = [
    path('servers/', views.ServerList.as_view()),
    path('servers/<int:pk>/', views.ServerDetail.as_view()),
]
