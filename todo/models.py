from django.db import models

# Create your models here.

class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)

# Columns required for Comment: id |comment	|task_id (foreign key)|	created_at
class Comment(models.Model):
    comment = models.CharField(max_length=255)
    # Create a many to one relationship using models.ForeignKey()
    # Specify the desired behaviour on deletion of the object to which the 
    # foreign key 'points'. models.CASCADE means "Delete this, too."
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)