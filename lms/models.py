from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    parent_email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Curriculum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    date = models.DateField()
    duration_hours = models.DecimalField(max_digits=4, decimal_places=2)
    progress = models.DecimalField(max_digits=5, decimal_places=2, help_text="Progress percentage")

    def __str__(self):
        return f"{self.curriculum.title} - {self.date}"


class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    present = models.BooleanField(default=True)

    class Meta:
        unique_together = ("lesson", "student")

    def __str__(self):
        return f"{self.student.name} @ {self.lesson.date}"


class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.DateField(help_text="First day of month")
    sessions = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice {self.student.name} {self.month:%Y-%m}"
