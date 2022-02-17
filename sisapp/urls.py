from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView
from django.views.static import serve

import sisapp.views
from sisapp.Views import studentViews, courseViews, departmentViews, instructorViews, registrationViews, studyTermViews, \
    teachingAssignmentsViews

app_name = 'sisapp'

urlpatterns = [

                  # /Course urls

                  path('course/create', courseViews.CourseCreate.as_view(template_name='course/course_create.html'),
                       name='course_create'),
                  path('course/list', courseViews.CourseListView.as_view(template_name='course/course_list.html'),
                       name='course_list'),
                  path('course/details/<pk>',
                       courseViews.CourseDetailView.as_view(template_name='course/course_list_item.html'),
                       name='course_details'),
                  path('course/edit/<pk>',
                       courseViews.CourseUpdateView.as_view(template_name='course/course_edit.html'),
                       name='course_edit'),
                  path('course/delete/<pk>',
                       courseViews.CourseDeleteView.as_view(template_name='course/course_delete.html'),
                       name='course_delete'),

                  #  /Department urls

                  path('department/create',
                       departmentViews.DepartmentCreate.as_view(template_name='department/department_create.html'),
                       name='department_create'),
                  path('department/list',
                       departmentViews.DepartmentListView.as_view(template_name='department/department_list.html'),
                       name='department_list'),
                  path('department/details/<pk>',
                       departmentViews.DepartmentDetailView.as_view(
                           template_name='department/department_list_item.html'),
                       name='department_details'),
                  path('department/edit/<pk>',
                       departmentViews.DepartmentUpdateView.as_view(template_name='department/department_edit.html'),
                       name='department_edit'),
                  path('department/delete/<pk>',
                       departmentViews.DepartmentDeleteView.as_view(template_name='department/department_delete.html'),
                       name='department_delete'),

                  # Instructor Urls
                  path('instructor/create',
                       instructorViews.InstructorCreate.as_view(template_name='instructor/instructor_create.html'),
                       name='instructor_create'),
                  path('instructor/list',
                       instructorViews.InstructorListView.as_view(template_name='instructor/instructor_list.html'),
                       name='instructor_list'),
                  path('instructor/details/<pk>',
                       instructorViews.InstructorDetailView.as_view(template_name='instructor'
                                                                                  '/instructor_list_item.html'),
                       name='instructor_details'),
                  path('instructor/edit/<pk>',
                       instructorViews.InstructorUpdateView.as_view(template_name='instructor/instructor_edit.html'),
                       name='instructor_edit'),
                  path('instructor/delete/<pk>',
                       instructorViews.InstructorDeleteView.as_view(template_name='instructor/instructor_delete.html'),
                       name='instructor_delete'),

                  # Registration Urls

                  path('registration/create',
                       registrationViews.RegistrationCreate.as_view(
                           template_name='registration/registration_create.html'),
                       name='registration_create'),
                  path('registration/list',
                       registrationViews.RegistrationListView.as_view(
                           template_name='registration/registration_list.html'),
                       name='registration_list'),
                  path('registration/details/<pk>',
                       registrationViews.RegistrationDetailView.as_view(template_name='registration'
                                                                                      '/registration_list_item.html'),
                       name='registration_details'),
                  path('registration/edit/<pk>',
                       registrationViews.RegistrationUpdateView.as_view(
                           template_name='registration/registration_edit.html'),
                       name='registration_edit'),
                  path('registration/delete/<pk>',
                       registrationViews.RegistrationDeleteView.as_view(
                           template_name='registration/registration_delete.html'),
                       name='registration_delete'),

                  # Student urls
                  path('student/create',
                       studentViews.StudentCreate.as_view(template_name='student/student_create.html'),
                       name='student_create'),
                  path('student/list',
                       studentViews.StudentListView.as_view(template_name='student/student_list.html'),
                       name='student_list'),
                  path('student/details/<pk>', studentViews.StudentDetailView.as_view(template_name='student'
                                                                                                    '/student_list_item.html'),
                       name='student_details'),
                  path('student/edit/<pk>',
                       studentViews.StudentUpdateView.as_view(template_name='student/student_edit.html'),
                       name='student_edit'),
                  path('student/delete/<pk>',
                       studentViews.StudentDeleteView.as_view(template_name='student/student_delete.html'),
                       name='student_delete'),

                  # study Term
                  path('studyterm/create',
                       studyTermViews.StudyTermCreate.as_view(template_name='studyTerm/studyTerm_create.html'),
                       name='studyTerm_create'),
                  path('studyterm/list',
                       studyTermViews.StudyTermListView.as_view(template_name='studyTerm/studyTerm_list.html'),
                       name='studyTerm_list'),
                  path('studyterm/details/<pk>',
                       studyTermViews.StudyTermDetailView.as_view(template_name='studyTerm/studyTerm_list_item.html'),
                       name='studyTerm_details'),
                  path('studyterm/edit/<pk>',
                       studyTermViews.StudyTermUpdateView.as_view(template_name='studyTerm/studyTerm_edit.html'),
                       name='studyTerm_edit'),
                  path('studyterm/delete/<pk>',
                       studyTermViews.StudyTermDeleteView.as_view(template_name='studyTerm/studyTerm_delete.html'),
                       name='studyTerm_delete'),

                  # TeachingAssignment
                  path('teachingassignments/create', teachingAssignmentsViews.TeachingAssignmentCreate.as_view(
                      template_name='teachingAssignment/teachingAssignment_create.html'),
                       name='teachingAssignments_create'),
                  path('teachingassignments/list',
                       teachingAssignmentsViews.TeachingAssignmentsListView.as_view(
                           template_name='teachingAssignment/teachingAssignment_list.html'),
                       name='teachingAssignments_list'),
                  path('teachingassignments/details/<pk>',
                       teachingAssignmentsViews.TeachingAssignmentsDetailView.as_view(
                           template_name='teachingAssignment/teachingAssignment_list_item.html'),
                       name='teachingAssignments_details'),
                  path('teachingassignments/edit/<pk>',
                       teachingAssignmentsViews.TeachingAssignmentsUpdateView.as_view(
                           template_name='teachingAssignment/teachingAssignment_edit.html'),
                       name='teachingAssignments_edit'),
                  path('teachingassignments/delete/<pk>',
                       teachingAssignmentsViews.TeachingAssignmentsDeleteView.as_view(
                           template_name='teachingAssignment/teachingAssignment_delete.html'),
                       name='teachingAssignments_delete'),

                  path("", sisapp.views.index, name='index'),
                  path('about', sisapp.views.about, name='about'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
