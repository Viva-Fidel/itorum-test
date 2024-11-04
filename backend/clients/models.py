from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True) 
    phone_number = models.CharField(max_length=11, unique=True) 
    mobile_operator_code = models.CharField(max_length=3) 
    tag = models.CharField(max_length=50)  

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"Клиент {self.id} - {self.phone_number}"
    
    # Функция для вырезания тел. оператора
    def save(self, *args, **kwargs):
        if self.phone_number and self.phone_number.startswith('7'):
            self.mobile_operator_code = self.phone_number[1:4] 
        super().save(*args, **kwargs)