from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    profile_pic=models.ImageField(upload_to='client_images/', null=True)
    name=models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="client"

    def __str__(s):
        return s.name
    
class Project(models.Model):
    name=models.CharField(max_length=50)
    client=models.ForeignKey(Client,on_delete=models.CASCADE,related_name="project_details")
    Users=models.ManyToManyField(User)
    class Meta:
        db_table="projects"