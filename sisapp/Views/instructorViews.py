from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from sisapp.models import Instructor


class InstructorCreate(CreateView):
    model = Instructor
    fields = ['instructor_first_name',
              'instructor_last_name',
              'instructor_email',
              'instructor_dept_id']
    success_url = '/instructor/list'


class InstructorListView(ListView):
    model = Instructor


class InstructorDetailView(DetailView):
    model = Instructor


class InstructorUpdateView(UpdateView):
    model = Instructor
    fields = ['instructor_first_name',
              'instructor_last_name',
              'instructor_email',
              'instructor_dept_id']
    success_url = '/instructor/list'


class InstructorDeleteView(DeleteView):
    model = Instructor
    success_url = '/instructor/list'
