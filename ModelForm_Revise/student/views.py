from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from student.forms import StudentForm
from student.models import Student

# Create your views here.
class StudentCreate(View):
    template_name = 'student/student_form.html'
    def get(self, request):
        form = StudentForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = StudentForm(request.POST)
        # Validating the Form 
        if form.is_valid():
            form.save()
            return render(request, 'student/student_success.html')
        return render(request, self.template_name, {'form': form})

class StudentList(View):
    template_name = 'student/student_list.html'
    def get(self, request):
        students = Student.objects.all()
        context = {'students': students}
        return render(request, self.template_name, context)
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name, email)
        Student.objects.create(name = name, email = email)
        students = Student.objects.all()
        print(students)
        context = {'students': students}
        return render(request, self.template_name, context)

class StudentDetails(View):
    template_name = 'student/student_detail.html'
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        context = {'student': student}
        return render(request, self.template_name, context)
    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.save()
        return redirect('student:student_detail', pk = student.pk)

class StudentUpdate(View):
    template_name = 'student/student_form.html'
    def get(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        form = StudentForm(instance=student)
        context = {'form': form}
        return render(request, self.template_name, context)
    def post(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return render(request, 'student/student_success.html')
        context = {'form': form}
        return render(request, self.template_name, context)

class StudentDelete(View):
    template_name = 'student/student_confirm_delete.html'
    def get(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        context = {'student': student}
        return render(request, self.template_name, context)
    def post(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        student.delete()
        return redirect('student:student_list')