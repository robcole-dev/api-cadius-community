from django.urls import path
from emojis import views


urlpatterns = [
    path('emojis/', views.EmojiList.as_view()),
    path('emojis/<int:pk>/', views.EmojiDetail.as_view()),
]