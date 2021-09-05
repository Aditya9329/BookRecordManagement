from django.urls import path
from api import views
urlpatterns=[
    path('',views.student_detail),
    path('queryset/',views.student_list),
    path('new/',views.NewStudent),
]