from django.contrib import admin
from django.urls import path
from newsportal import views
admin.site.site_header = "CDC ADMIN"
admin.site.site_title = "CDC ADMIN"
admin.site.index_title = "CDC ADMIN"

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    
    
    path('addnews/', views.addnews, name='addnews'),
    path('allnews/', views.allnews, name='allnews'),
    path('newsdetails/<int:pk>/', views.newsdetails, name='newsdetails'),
    path('editnews/<int:pk>/', views.editnews, name='editnews'),
    path('deletenews/<int:pk>/', views.deletenews, name='deletenews'),
    path('detailsnews/<int:pk>/', views.detailsnews, name='detailsnews'),
   
    
    
    path('index/', views.index, name='index'),
     
    path('contact/', views.contact, name='contact'),
    path('achievement/', views.achievement, name='achievement'),
    path('sports/', views.sports, name='sports'),
    path('event/', views.event, name='event'),
    path('Career_DC/', views.Career_DC, name='Career_DC'),
    path('ece/', views.ece, name='ece'),
    path('cse/', views.cse, name='cse'),
    path('ee/', views.ee, name='ee'),
    path('ce/', views.ce, name='ce'),
    path('me/', views.me, name='me'),
    path('event/annualfest/', views.annualfest, name='annualfest'),
    path('event/blood/', views.blood, name='blood'),
    path('dept/ece/introduction/', views.introduction1, name='introduction1'),
    path('dept/cse/introduction/', views.introduction2, name='introduction2'),
    path('dept/me/introduction/', views.introduction3, name='introduction3'),
    path('dept/ee/introduction/', views.introduction4, name='introduction4'),
    path('dept/ce/introduction/', views.introduction5, name='introduction5'),
    path('dept/ece/lab/', views.lab1, name='lab1'),
    path('dept/cse/lab/', views.lab2, name='lab2'),
    path('dept/me/lab/', views.lab3, name='lab3'),
    path('dept/ee/lab/', views.lab4, name='lab4'),
    path('dept/ce/lab/', views.lab5, name='lab5'),
    path('leadership/', views.leadership, name='leadership'),
    path('dept/ece/practice/', views.practice, name='practice'),
    path('dept/cse/practice/', views.practice1, name='practice1'),
    path('dept/me/practice/', views.practice2, name='practice2'),
    path('dept/ee/practice/', views.practice3, name='practice3'),
    path('dept/ce/practice/', views.practice4, name='practice4'),
    path('event/puja/', views.puja, name='puja'),
    path('event/vishwakarma/', views.vishwakarma, name='vishwakarma'),
    path('event/carnival/', views.carnival, name='carnival'),
    
    
    
    

]
