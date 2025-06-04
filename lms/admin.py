from django.contrib import admin
from .models import Student, Curriculum, Lesson, Attendance, Invoice


admin.site.register(Student)
admin.site.register(Curriculum)
admin.site.register(Lesson)
admin.site.register(Attendance)
admin.site.register(Invoice)
