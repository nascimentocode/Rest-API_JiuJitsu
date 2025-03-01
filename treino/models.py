from django.db import models

belt_choices = (
        ('B', 'Branca'),
        ('A', 'Azul'),
        ('R', 'Roxa'),
        ('M', 'Marrom'),
        ('P', 'Preta')
    )

class Students(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    belt = models.CharField(max_length=1, choices=belt_choices, default='B')
    birthdate = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ClassesHeld(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    current_belt = models.CharField(max_length=1, choices=belt_choices, default='B')
    
    def __str__(self):
        return self.student.name