from django.db import models

class University(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.university.name})"

class Semester(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.branch}"

class Subject(models.Model):
    name = models.CharField(max_length=200)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudyMaterial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to="media/materials/")
    upload_date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
