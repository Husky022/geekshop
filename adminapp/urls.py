from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('admin-users-read/', adminapp.admin_users_read, name='admin_users_read'),
    path('admin-users-create/', adminapp.admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:id>', adminapp.admin_users_update, name='admin_users_update'),

]