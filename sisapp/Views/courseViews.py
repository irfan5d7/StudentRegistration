from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sisapp.models import Course, Department

from django.shortcuts import render, get_object_or_404


class CourseCreate(CreateView):
    model = Course
    fields = ['course_id',
              'course_name',
              'course_dept_id']
    success_url = "/course/list"


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class CourseDeleteView(DeleteView):
    model = Course
    success_url = "/course/list"


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['course_id',
              'course_name',
              'course_dept_id']

    success_url = "/course/list"
