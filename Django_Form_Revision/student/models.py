from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Course(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.title} ({self.code})"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    # Yeuta department ma Many Stds le admission lina sakxa
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="students")
    # Many stds le Many Course study garna sakxaan 
    courses = models.ManyToManyField(Course, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StudentProfile(models.Model):
    # yeuta student ko yeuta matra profile huna sakxa
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    dob = models.DateField()
    bio = models.TextField(max_length=400)

    def __str__(self):
        return f"Profile of {self.student}"