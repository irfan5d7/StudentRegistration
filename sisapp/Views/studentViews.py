from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sisapp.models import Student


class StudentCreate(CreateView):
    # specify the model for create view
    model = Student

    # specify the fields to be displayed

    fields = ['student_id',
              'student_first_name',
              'student_last_name',
              'student_email',
              'student_phone',
              'student_address']
    success_url = '/student/list'


class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['student_id',
              'student_first_name',
              'student_last_name',
              'student_email',
              'student_phone',
              'student_address']
    success_url = '/student/list'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/student/list'
