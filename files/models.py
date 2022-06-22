from django.db import models

# Create your models here.
class FilesAdmin(models.Model):
    name=models.CharField(max_length=50)
    fil=models.FileField(upload_to='media')

    def __str__(self):
        return self.name
