from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    path('studentapi/add/', views.StudentCreate.as_view()),
    path('studentapi/<int:pk>', views.StudentRetrieve.as_view()),    #for browsable api
    path('studentapi/update/<int:pk>', views.StudentUpdate.as_view()),
    path('studentapi/delete/<int:pk>', views.StudentDelete.as_view()),
]
