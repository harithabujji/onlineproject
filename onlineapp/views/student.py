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
class CreateStudentView(LoginRequiredMixin,CreateView):
    login_url = "onlineapp:login"
    model = Student
    form_class = studentform
    permission_required = "onlineapp.add_student"
    permission_denied_message = "user does not have permission to add a student"
    #template_name = 'onlineapp/student_form.html'

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        test_form = MockTestForm()
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
        })
        return context

    def post(self, request, *args, **kwargs):
        login_url = "onlineapp:login"
        college = get_object_or_404(College, pk=kwargs.get('pk'))
        student_form = studentform(request.POST)
        test_form = MockTestForm(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.college = college
            student.save()

            if test_form.is_valid():
                score = test_form.save(commit=False)
                score.total = sum(test_form.cleaned_data.values())
                score.student = student
                score.save()

        return redirect('onlineapp:college_detail_html',college.id)



class UpdateStudentView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = "onlineapp:login"
    permission_required = "onlineapp.change_student"
    permission_denied_message = "user does not have permission to change a student"
    model = Student
    form_class = studentform
    template_name = 'onlineapp/student_form.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentView, self).get_context_data(**kwargs)
        student_form = context.get('student')
        test_form =MockTestForm(instance=student_form.mocktest1)
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
        })

        return context

    def post(self, request, *args, **kwargs):
        login_url = "onlineapp:login"
        student = Student.objects.get(pk=kwargs.get('pk'))
        form = studentform(request.POST, instance=student)
        test_form = MockTestForm(request.POST, instance=student.mocktest1)
        test = test_form.save(False)
        test.total = sum(test_form.cleaned_data.values())
        form.save()
        test_form.save()
        return redirect("onlineapp:college_detail_html", self.kwargs.get('college_id'))


class DeleteStudentView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = "onlineapp:login"
    permission_required = "onlineapp.delete_student"
    permission_denied_message = "user does not have permission to delete a student"
    model=Student

    success_url = reverse_lazy('onlineapp:college_html')

    def get(self,request,*args,**kwargs):
        return self.post(request,args,kwargs)

    def post(self, request, *args, **kwargs):
        self.delete(request, args, kwargs)
        return redirect("onlineapp:college_detail_html", self.kwargs.get('college_id'))