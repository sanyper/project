from django.urls import path
from . import views #ดึงฟังก์ชั้นในviews มาทำงาน

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('subject/', views.Subjects, name="subjects"),
    path('register/',views.Register, name="registerpage"),
    #path('class/', views.logout_view, name="logout_view"),
    path('studentinfo/', views.studentinfo, name="studentinfo"),
    

]
