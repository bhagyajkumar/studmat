from django.contrib import admin
from .models import Branch, Semester, StudyMaterial, Subject, University

admin.site.register(University)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(Branch)
admin.site.register(StudyMaterial)
