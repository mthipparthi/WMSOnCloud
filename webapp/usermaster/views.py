from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
import json

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import ListView

from usermaster.models import UserMaster
from usermaster.forms import UserLoginForm
from usermaster.forms import UserCreationForm
from usermaster.forms import UserUpdateForm
from usermaster.forms import UserSearchForm

from enterprise.models import EnterpriseMaster

from braces.views import JSONResponseMixin
from django.core import serializers


from crispy_forms.utils import render_crispy_form

from django.core.urlresolvers import reverse

# import transction
from django.db import transaction


import logging

class AjaxableResponseRowMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseRowMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        print "I am in ajax"
        response = super(AjaxableResponseRowMixin, self).form_valid(form)
        if self.request.is_ajax():
            print "Value of primary Key",self.object.pk
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response

class AjaxableResponseMultiRowMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMultiRowMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        print "I am in ajax"
        response = super(AjaxableResponseMultiRowMixin, self).form_valid(form)
        if self.request.is_ajax():
            print "Value of primary Key",self.object.pk
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


#    Create    your    views    here.
def    UserLoginView(request):
    print "UserLoginView"
    logger = logging.getLogger(__name__)
    if request.method == 'POST':
        logger.debug('Start user login')
        form = UserLoginForm(request.POST)
        print form.errors
        if form.is_valid():
            print "Valid"
            email = request.POST.get('email','')
            password = request.POST.get('password','')
            enterprise_id = request.POST.get('enterprise_id','')

            logger.debug("Login with user id - %s and enterprise id - %s", email, enterprise_id)

            ''' TODO if enterprise is not valid, register error. '''

            user = authenticate(email=email,    password=password)
            if user is not None and user.is_active:
                login(request,    user)
                request.session['organisation_id']=user.enterprise_id
                request.session['store_id']=user.store_id
                request.session['user_id']=user.id
                return HttpResponseRedirect('/apphome/')
        else:
            print "InValid Form"
    else:
        form = UserLoginForm()
    return render(request,'index.html',{'form':form,})

#    Create    your    views    here.
def UserSearchView(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email',    '')
            last_name = request.POST.get('last_name',    '')
            enterprise_id = request.POST.get('enterprise_id',    '')
            store_id = request.POST.get('store_id',    '')
            condition = Q(email=email) \
                    | Q(enterprise_id=enterprise_id) \
                    | Q(store_id=store_id) \
                    | Q(last_name=last_name)

            users_list = get_user_model().objects.filter(condition)
            data = serializers.serialize("json", users_list)
            response_kwargs={}
            response_kwargs['content_type'] = 'application/json'
            print data
            return HttpResponse(data, **response_kwargs)
            #return render(request,'usermaster/users_list_form.html',{'users_list': users_list})
    else:
        form = UserSearchForm()
    return render(request,'usermaster/user_search_form.html',{'form':form,})


# class  UserCreationView(AjaxableResponseRowMixin,CreateView):
#     model = UserMaster
#     form_class = UserCreationForm
#     template_name = 'usermaster/user_create_form.html'


def UserCreationFunc(request):
    print "UserCreationFunc"
    logger = logging.getLogger(__name__)
    logger.debug("Begin User Creation with session organisation %s", request.session['organisation_id'])
    session_variables = ['enterprise_id', 'user_id']
    if request.method == 'POST':
        print "create post"

        form = UserCreationForm(request.POST, request=request, sessionvars= session_variables)
        form.addSessionRelatedFields()

        if form.is_valid():
            logger.debug("Form data is successfully validated")
            logger.debug("Enterprise id value is set - %s", form.cleaned_data['enterprise_id'])
            if form.save():
                form.clearSessionRelatedFields()
                logger.debug("User creation succeeded")
                return reverse('user_detail')
            else:
                form.clearSessionRelatedFields()
                logger.debug("User creation failed")
                return {'success': False}
        else:
            logger.debug("Form data is failed to validate and errors are %s", form.errors)
            return {'success': False}
            #form_error = render_crispy_form(form)
            #return {'success': False, 'form_error': form_error}

    else:
        logger.debug("User creation form generation with organisation %s", request.session['organisation_id'])
        form = UserCreationForm(None, request=request, sessionvars= session_variables)
        return render(request,'usermaster/user_create_form.html',{'form':form,})



class    UserUpdateView(UpdateView):
    model = UserMaster
    form_class = UserUpdateForm
    template_name = 'usermaster/user_update_form.html'

class    UserDeleteView(DeleteView):
    model = UserMaster
    template_name = 'usermaster/user_delete_form.html'
    success_url = 'Success'


#class UserDetailView(JSONResponseMixin,DetailView):
class UserDetailView(DetailView):
    model = UserMaster
    template_name = 'usermaster/user_detail_form.html'
    #content_type = 'application/javascript'
    #json_dumps_kwargs = {'indent': 2}

    #def get(self, request, *args, **kwargs):
        #self.object = self.get_object()
        #context_dict = self.object.as_json()
        #context_dict = {
        #    'email': self.object.email,
        #    'first_name': self.object.first_name,
        #}
        #return self.render_json_response(context_dict)

