from django.db import models

from django.contrib.auth.models import User

class Product(models.Model):
    hunter=models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=100)
    mobile=models.IntegerField()
    career=models.TextField(max_length=200, choices=(
    ( 'To secure a position with a stable and profitable organization,where i can be a member of a team and utilize my bussiness experience to the fullest','OBJECTIVE1' ),
    ( 'To obtain a challenging position in a high quality engineering environment where my resourceful experience and academic skills will add value to organizational operations', 'OBJECTIVE2' )
    ))
    inter=models.CharField(max_length=40)
    high=models.CharField(max_length=40)
    btech=models.CharField(max_length=40)
    image=models.ImageField(upload_to='images/',blank=True)
    work=models.CharField(max_length=100)
    title1=models.CharField(max_length=40)
    description1=models.CharField(max_length=30)
    duartion1=models.CharField(max_length=40)
    role1=models.CharField(max_length=40)
    teamsize1=models.IntegerField(blank=True)
    title2=models.CharField(max_length=30 ,default=False)
    description2=models.CharField(max_length=40,blank=True)
    duartion2=models.TextField(max_length=40,blank=True)
    role2=models.CharField(max_length=40,blank=True)
    teamsize2=models.IntegerField(blank=True)
    field=models.CharField(max_length=40)
    skill1=models.CharField(max_length=40)
    skill2=models.CharField(max_length=40,blank=True)
    skill3=models.CharField(max_length=40,blank=True)
    achievement1=models.CharField(max_length=40,blank=True)
    achievement2=models.CharField(max_length=40,blank=True)
    achievement3=models.CharField(max_length=40,blank=True)
    achievement4=models.CharField(max_length=40,blank=True)
    achievement5=models.CharField(max_length=40,blank=True)
    votes_total=models.IntegerField(default=1 )
    def __str__(self):
        return self.email

    class Meta:
        ordering=['-id']
