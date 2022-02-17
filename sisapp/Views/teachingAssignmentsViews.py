from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from sisapp.models import TeachingAssignments


class TeachingAssignmentCreate(CreateView):
    model = TeachingAssignments
    fields = ['instructor_id',
              'course_id',
              'term_id']
    success_url = '/teachingassignments/list'

class TeachingAssignmentsListView(ListView):
    model = TeachingAssignments


class TeachingAssignmentsDetailView(DetailView):
    model = TeachingAssignments


class TeachingAssignmentsUpdateView(UpdateView):
    model = TeachingAssignments
    fields = ['instructor_id',
              'course_id',
              'term_id']
    success_url = '/teachingassignments/list'


class TeachingAssignmentsDeleteView(DeleteView):
    model = TeachingAssignments
    success_url = '/teachingassignments/list'
