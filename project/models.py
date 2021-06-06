from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    duration = models.IntegerField()
    # avatar = models.ImageField()

    def __str__(self):
        return f"{self.name, self.id}"

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField()
    project = models.ForeignKey(Project, default=1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"
        