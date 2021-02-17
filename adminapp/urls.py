from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('admin-users-read/', adminapp.UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', adminapp.UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>', adminapp.UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-delete/<int:pk>', adminapp.UserDeleteView.as_view(), name='admin_users_delete'),

]