from django.urls import path
from .views import home, phone_detail, add_phone, edit_phone, delete_phone

urlpatterns = [
    path('', home, name='home'),
    path('phone/<int:phone_id>/', phone_detail, name='phone_detail'),
    path('phone/add/', add_phone, name='add_phone'),
    path('phone/edit/<int:phone_id>/', edit_phone, name='edit_phone'),
    path('phone/delete/<int:phone_id>/', delete_phone, name='delete_phone'),
]

