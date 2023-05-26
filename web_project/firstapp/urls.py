from django.urls import path
from firstapp import views
urlpatterns = [
    path("",views.home,name="home"),
    path("add_pet/",views.add_pet,name="pet_list"),
     path('project/<int:pet_id>/', views.pet_detail, name='pet_detail'),

    path('delete_post/<int:pk>',
         views.delete_pet, name="delete_pet"),
    path('edit_pet/<int:pet_id>/', views.edit_pet, name='edit_pet'),
]
