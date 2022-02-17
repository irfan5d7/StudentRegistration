from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sisapp.models import Department


class DepartmentCreate(CreateView):
    model = Department
    fields = ['department_id', 'department_name']
    success_url = '/department/list'


class DepartmentListView(ListView):
    model = Department


class DepartmentDetailView(DetailView):
    model = Department

    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentDetailView,
                        self).get_context_data(*args, **kwargs)
        return context


class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['department_id', 'department_name']
    success_url = '/department/list'


class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = '/department/list'
