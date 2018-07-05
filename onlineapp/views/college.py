from onlineapp.models import *
from django.views import View
from onlineapp.models import *
from django.shortcuts import *
import ipdb
from django.views.generic import *
from django import forms
from onlineapp.forms import *
from django.urls import *
from django.contrib.auth.mixins import *
app_name="onlineapp"
class CollegeView(LoginRequiredMixin,View):
    login_url = "onlineapp:login"
    def get(self,request,*args,**kwargs):
        pass
        colleges=College.objects.all()

        return render(
            request,
            template_name='onlineapp/colleges.html',
            context={
                "jails":colleges

            }
        )

class CollegeListView(LoginRequiredMixin,ListView):
    login_url = "onlineapp:login"
    model = College
    context_object_name = 'jails'
    template_name = "college_list.html"



    def get_context_data(self, **kwargs):
        context = super(CollegeListView,self).get_context_data(**kwargs)

        #context['data']=self.model.objects.all().values('name','student__name','student__email','student__mocktest1__total')

        context.update({'user_permissions' : self.request.user.get_all_permissions})
        return context


class CollegeDetailView(LoginRequiredMixin,DetailView):
    login_url = "onlineapp:login"

    model=College
    template_name = 'onlineapp/college_detail.html'

    success_url = reverse_lazy('onlineapp:college_detail.html')
    def get_object(self, queryset=None):
        #we are getting refernece of clg
        return get_object_or_404(College, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(CollegeDetailView,self).get_context_data(**kwargs)
        #import ipdb
        #ipdb.set_trace()
        college = context.get('college')
        students = list(college.student_set.order_by("-mocktest1__total"))
        context.update({'students':students,'user_permissions':self.request.user.get_all_permissions()})
        return context



class  CreateCollegeView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = "onlineapp:login"
    permission_required="onlineapp.add_college"
    permission_denied_message="User des not have permission to create a college"
    raise_exception=True
    model=College
    form_class = Addcollege
    success_url = reverse_lazy('onlineapp:college_html')


class UpdateCollegeView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = "onlineapp:login"
    permission_required="onlineapp.change_college"
    permission_denied_message = "user does not have permission to change a college"
    model=College

    form_class = Addcollege

    template_name = 'onlineapp/college_form.html'

    success_url = reverse_lazy('onlineapp:college_html')

    def get_object(self,queryset=None):
        #return get_object_or_404(College,**self.kwargs)
        return get_object_or_404(College,**{'pk': self.kwargs.get('pk')})

    def get_context_data(self,**kwargs):
        context=super(UpdateCollegeView,self).get_context_data(**kwargs)
        #import ipdb
        #ipdb.set_trace()
        college=context.get('college')
        students=list(college.student_set.order_by('-mocktest1__total'))
        context.update({
            'students':students,
            #'user_permissions':self.request.user.get_all_permissions()
        })
        return context

class DeleteCollegeView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = "onlineapp:login"
    permission_required = "onlineapp.delete_college"
    permission_denied_message = "user does not have permission to delete a college"
    model = College
    template_name = 'onlineapp/delete.html'
    success_url = reverse_lazy('onlineapp:college_html')

    def get_object(self, queryset=None):
        return get_object_or_404(College, **self.kwargs)


