from django.db import models

# Create your models here.

class Mailing(models.Model):
    id = models.AutoField(primary_key=True)  
    start_datetime = models.DateTimeField() 
    message_text = models.TextField() 
    mobile_operator_code = models.CharField(max_length=3) 
    tag = models.CharField(max_length=50)
    end_datetime = models.DateTimeField() 

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return f"Рассылка номер {self.id}"


class Messages(models.Model):
    id = models.AutoField(primary_key=True)  
    sent_datetime = models.DateTimeField(auto_now_add=True)  
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE, related_name='messages')  
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='messages') 

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Сообщение {self.id} для клиента {self.client.id} в рассылке {self.mailing.id}"