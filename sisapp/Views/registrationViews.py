from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from sisapp.models import Registration


class RegistrationCreate(CreateView):
    model = Registration
    fields = ['student_id',
              'course_id',
              'term_id']
    success_url = '/registration/list'


class RegistrationListView(ListView):
    model = Registration


class RegistrationDetailView(DetailView):
    model = Registration


class RegistrationUpdateView(UpdateView):
    model = Registration
    fields = ['student_id',
              'course_id',
              'term_id']
    success_url = '/registration/list'


class RegistrationDeleteView(DeleteView):
    model = Registration
    success_url = '/registration/list'
