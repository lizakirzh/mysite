from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html


User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField(max_length=80, verbose_name="заголовок")
    description = models.TextField("описание")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    auction = models.BooleanField("возможность торга", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField("дата создания", auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")

    class Meta: 
        db_table = 'advertisements'

    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
