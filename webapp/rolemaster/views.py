from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.db.models import Q

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from usermaster.models import UserMaster
from usermaster.forms import UserLoginForm
from usermaster.forms import UserCreationForm
from usermaster.forms import UserUpdateForm
from usermaster.forms import UserSearchForm

#    Create    your    views    here.
def    UserLoginView(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email','')
            password = request.POST.get('password','')
            enterprise_id = request.POST.get('enterprise_id','')

            user = authenticate(email=email,    password=password)
            if user is not None:
                if user.is_active:
                    login(request,    user)
                    return HttpResponseRedirect('/apphome/')
    else:
        form = UserLoginForm()
    return render(request,'usermaster/user_login_form.html',{'form':form,})

#    Create    your    views    here.
def UserSearchView(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email',    '')
            last_name = request.POST.get('last_name',    '')
            enterprise_id = request.POST.get('enterprise_id',    '')
            store_id = request.POST.get('store_id',    '')
            users_list = get_user_model().objects.filter(Q(email=email) &
                                                        Q(enterprise_id=enterprise_id) &
                                                        Q(store_id=store_id) &
                                                        Q(last_name=last_name) )
            return render(request,'usermaster/users_list_form.html',{'users_list': users_list})
    else:
        form = UserSearchForm()
    return render(request,'usermaster/user_search_form.html',{'form':form,})

class  UserCreationView(CreateView):
    model = UserMaster
    form_class = UserCreationForm
    template_name = 'usermaster/user_create_form.html'

class    UserUpdateView(UpdateView):
    model = UserMaster
    form_class = UserUpdateForm
    template_name = 'usermaster/user_update_form.html'

class    UserDeleteView(DeleteView):
    model = UserMaster
    template_name = 'usermaster/user_delete_form.html'
    success_url = 'Success'

class    UserDetailView(DetailView):
    model = UserMaster
    template_name = 'usermaster/user_detail_form.html'


