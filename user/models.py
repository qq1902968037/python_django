from django.db import models

# Create your models here.


# 编写model
class UserModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=255)
    sal = models.IntegerField()

    class Meta:
        db_table = 'tb_user'


class OrderModel(models.Model):

    name = models.CharField(max_length=255)
    u_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_column="u_id")

    class Meta:
        db_table = 'tb_order'

