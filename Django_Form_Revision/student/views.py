from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from student.forms import *
from student.models import *

# Create your views here.
class StudentCreateView(View):
    template_name = "student/student_form.html"
    page_title = "Add New Students"
    def get(self, request):
        form = StudentForm()
        context = {"form": form, "page_title": self.page_title}
        return render(request, self.template_name, context)
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            print(student)
            messages.success(request, f"Student {student} created successfully!")
            return redirect('student_detail', pk = student.pk)
        context = {'form': form, 'page_title': self.page_title}
        return render(request, self.template_name, context)

class StudentUpdateView(View):
    template_name = 'student/student_form.html'
    page_title = "Edit Student Details"
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(instance=student)
        context = {'form': form, 'student': student}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        # First Stds ra form ko data liyera
        student = get_object_or_404(Student, pk=pk)
        # form bata post gareko data request garra liyo
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_detail', pk=student.pk)
        context = {'form': form, 'student': student, 'page_title': self.page_title}
        return render(request, self.template_name, context)

class StudentDetailView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        # Model ma Std table ma department vnya Foreign Key ho
        # ForeignKey ko data access gareko std table bata department ko data
        department = student.department          # ki ta Department object farkauxa ki None farkauxa
        department_name = student.department.name if student.department else "No Department"

        # ManyToMany Field ko data Access garna laii
        courses = student.courses.all()          # Course ko QuerySet farkauxa

        # OneToOneField ko data access garna laii
        # Careful if profile doesn't exist
        if StudentProfile.objects.filter(student=student).exists():
            profile = student.profile
        else:
            profile = None

        context = {'student': student, 'department': department, 'department_name': department_name, 'courses': courses, 'profile': profile,}
        return render(request, 'student/student_detail.html', context)

class StudentListView(View):
    template_name = 'student/student_list.html'
    def get(self, request):
        # SELECT 'department' FROM students jastaii vayo 
        # prefetch_related().all: ? 
        students = Student.objects.select_related('department').prefetch_related('courses').all()
        context = {'students': students}
        return render(request, self.template_name, context)

class StudentProfileCreateUpdateView(View):
    template_name = 'student/profile_form.html'
    page_title = "Student Profile"
    def get(self, request, student_pk):
        student = get_object_or_404(Student, pk=student_pk)
        if StudentProfile.objects.filter(student=student).exists():
            profile = StudentProfile.objects.get(student=student)
        else:
            profile = None
        form = StudentProfileForm(instance=profile)
        context = {'form': form, 'student': student, 'title': self.page_title}
        return render(request, self.template_name, context)

    def post(self, request, student_pk):
        student = get_object_or_404(Student, pk=student_pk)
        if StudentProfile.objects.filter(student=student).exists():
            profile = StudentProfile.objects.get(student=student)
        else:
            profile = None
        form = StudentProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            profile.student = student
            profile.save()
            messages.success(request, "Profile saved successfully!")
            return redirect('student_detail', pk=student.pk)
        context = {'form': form, 'student': student, 'title': self.page_title}
        return render(request, self.template_name, context)