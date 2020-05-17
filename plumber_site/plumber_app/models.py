from django.db import models

class AppointmentInfo(models.Model):
    your_name = models.CharField(max_length=100)
    your_phone = models.IntegerField(max_length=15)
    your_email = models.EmailField(max_length=150)
    your_address = models.CharField(max_length=100)
    your_time = models.DateField(auto_now_add=False)
    your_date = models.TimeField(auto_now_add=False)
    your_message = models.CharField(max_length=200)


    def __str__(self):
        return self.your_name + '  | ' + str(self.your_phone) + '  | ' + str(self.your_email) 

    class Meta:
        ordering = ['-id']
        



        