from django.urls import path
from CRUDAPP import views
urlpatterns = [
    path('students/', views.get_student),
    path('students/', views.create_student),
    path('students/<int:pk>/', views.student_details),
    path('students/<int:pk>/', views.update_student),
    path('students/<int:pk>/', views.delete_student),
]
# from django.urls import path
# from CRUDAPP import views

# urlpatterns = [
#     path('students/', views.student_list_create),                 # GET + POST
#     path('students/<int:pk>/', views.student_detail_update_delete),  # GET + PUT + DELETE
# ]
