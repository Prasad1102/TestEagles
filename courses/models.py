from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

class Subject(BaseModel):
  subject_name = models.CharField(max_length = 100)
  subject_image = models.ImageField(upload_to = "public/static/", default="/")

  def __str__(self):
    return self.subject_name

class Lesson(BaseModel):
  title = models.CharField(max_length=250)
  content = models.TextField()
  subject = models.ForeignKey(Subject, related_name="lesson", on_delete=models.CASCADE)

  def __str__(self):
    return self.title