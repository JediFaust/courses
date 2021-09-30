from django.urls import path
from coursesapp import views

# Wiring views to URLs

urlpatterns = [
    path('coursesapp/', views.course_list),
    path('coursesapp/<int:pk>/', views.course_detail),
]