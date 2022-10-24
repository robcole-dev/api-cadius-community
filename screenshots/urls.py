from django.urls import path
from screenshots import views


urlpatterns = [
    path('screenshots/', views.ScreenshotList.as_view()),
    path('screenshots/<int:pk>/', views.ScreenshotDetail.as_view()),
]
