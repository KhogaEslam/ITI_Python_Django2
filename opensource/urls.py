from django.conf.urls import url
import views

urlpatterns = [
    
    url(r'^hello' , views.show_all_students),
    url(r'^student/(?P<st_id>[0-9]+)/details$'  , views.details ),
    url(r'student/new', views.new_student),
    url(r'student/(?P<st_id>[0-9]+)/edit' , views.edit_student),
    url(r'student/(?P<st_id>[0-9]+)/delete' , views.del_student)
   

]