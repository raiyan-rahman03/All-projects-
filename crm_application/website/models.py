from django.db import models
default_img = 'blank-profile-picture-973460_1280.webp'



# Create your models here.
class student_record(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    roll_no = models.IntegerField()
    grade_level = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    phone= models.CharField(max_length=40)
    date_of_birth = models.DateField(max_length=40)
    address = models.CharField(max_length=150)
    class_room_no = models.CharField(max_length=10)
    image = models.ImageField(default=default_img)
   
    
    def __str__(self):
        return self.first_name +" "+ self.last_name



class result(models.Model):
   id = models.OneToOneField(student_record, on_delete=models.CASCADE, primary_key=True)
   gpa = models.DecimalField(max_digits=2, decimal_places=2) 
   bangla = models.IntegerField() 
   english = models.IntegerField() 
   math = models.IntegerField() 
   physics = models.IntegerField() 
   biology = models.IntegerField() 
   chemistry = models.IntegerField()
   









