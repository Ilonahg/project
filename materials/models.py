from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='course_previews/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='lesson_previews/', blank=True, null=True)
    description = models.TextField()
    video_link = models.URLField()

    def __str__(self):
        return f"{self.course.name} - {self.name}"
