from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.


# Change forms register django

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50)
    option_four = models.CharField(max_length=50, default='')
    option_five = models.CharField(max_length=50,default='')
    option_count_one = models.IntegerField(default=0)
    option_count_two = models.IntegerField(default=0)
    option_count_three = models.IntegerField(default=0)
    option_count_four = models.IntegerField(default=0)
    option_count_five = models.IntegerField(default=0)

    def __str__(self) :
        return self.question + ":" + self.option_one + ":" + self.option_two + ":" +self.option_three

    def total(self):
        return self.option_count_one + self.option_count_two + self.option_count_three + self.option_count_four + self.option_count_five
    

#class Profile(models.Model):
#    user = models.ForeignKey(User,on_delete=models.CASCADE)
#    id_user = models.IntegerField()

#    def __str__(self):
#        return self.user.username
    
class Rate(models.Model):
    question = models.TextField()
    rate_one = models.IntegerField(default=0)
    rate_two = models.IntegerField(default=0)
    rate_three = models.IntegerField(default=0)
    rate_four = models.IntegerField(default=0)
    rate_five = models.IntegerField(default=0)
    rate_1_count = models.IntegerField(default=0)
    rate_2_count = models.IntegerField(default=0)
    rate_3_count = models.IntegerField(default=0)
    rate_4_count = models.IntegerField(default=0)
    rate_5_count = models.IntegerField(default=0)


    
