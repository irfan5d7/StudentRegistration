from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sisapp.models import StudyTerm


class StudyTermCreate(CreateView):
    model = StudyTerm
    fields = ['term_id',
              'term_start_date',
              'term_end_date',
              'term_season',
              'term_year']
    success_url = '/studyterm/list'


class StudyTermListView(ListView):
    model = StudyTerm


class StudyTermDetailView(DetailView):
    model = StudyTerm


class StudyTermUpdateView(UpdateView):
    model = StudyTerm
    fields = ['term_id',
              'term_start_date',
              'term_end_date',
              'term_season',
              'term_year']
    success_url = '/studyterm/list'


class StudyTermDeleteView(DeleteView):
    model = StudyTerm
    success_url = '/studyterm/list'
