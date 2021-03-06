from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    city = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    # Essa configuração permite que a tabela seja de nome diferente da classe, se não usar a tabela 
    # criada pelo migrationsusará o mesmo nome da classe
    class Meta:
        db_table = 'pet'


    # User admin pass
    # Master@2    