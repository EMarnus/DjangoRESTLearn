from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.likeList.as_view()),
    path('likes/<int:pk>/', views.likeDetail.as_view())
]