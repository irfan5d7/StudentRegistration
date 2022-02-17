from django.db import models


# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_first_name = models.CharField(max_length=32)
    student_last_name = models.CharField(max_length=32)
    student_email = models.EmailField()
    student_phone = models.CharField(max_length=32)
    student_address = models.TextField()

    def __str__(self):
        return self.student_first_name + " " + self.student_last_name


class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=32)

    def __str__(self):
        return self.department_name


class StudyTerm(models.Model):
    seasons = (
        ('SPRING', 'Spring'),
        ('FALL', 'Fall'),
    )
    term_id = models.AutoField(primary_key=True)
    term_start_date = models.DateField()
    term_end_date = models.DateField()
    term_season = models.CharField(max_length=32, choices=seasons)
    term_year = models.CharField(max_length=8)

    def __str__(self):
        return "{} - {}".format(self.term_season, self.term_year)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.CharField(max_length=16)
    course_name = models.CharField(max_length=32)
    course_dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Registration(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    term_id = models.ForeignKey(StudyTerm, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student_id) + "-" + str(self.course_id)


class Instructor(models.Model):
    instructor_first_name = models.CharField(max_length=32)
    instructor_last_name = models.CharField(max_length=32)
    instructor_email = models.EmailField()
    instructor_dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.instructor_first_name + " " + self.instructor_last_name


class TeachingAssignments(models.Model):
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    term_id = models.ForeignKey(StudyTerm, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.instructor_id) + " - " + str(self.course_id)
