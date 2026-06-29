from django.db import models

# Create your models here.
class players(models.Model):

    jn=models.IntegerField()
    pname=models.CharField(max_length=50)
    run=models.IntegerField()
    wickets=models.IntegerField()
    

    def __str__(self):
        return self.pname

    
    