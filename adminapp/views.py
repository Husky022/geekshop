from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


@user_passes_test(lambda u:u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')

@user_passes_test(lambda u:u.is_superuser)
def admin_users_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)

@user_passes_test(lambda u:u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)

@user_passes_test(lambda u:u.is_superuser)
def admin_users_update(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {'form': form, 'current_user': user}
    return render(request,'adminapp/admin-users-update-delete.html', context)

@user_passes_test(lambda u:u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users_read'))