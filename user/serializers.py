from rest_framework import serializers

from user import models
from user.models import OrderModel


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.OrderModel
        fields = '__all__'
        extra_kwargs = {
            "u_id": {
                "write_only": True
            }
        }




# class OrderSerializers(serializers.Serializer):
#     name = serializers.CharField()
#     # 定义外键第一种方式，u_id必须和数据库字段名称一致
#     u_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         order = OrderModel.objects.create(**validated_data)
#         return order
    # 定义外键第二种方式
    # u = serializers.PrimaryKeyRelatedField(queryset=models.UserModel.objects.all())

    # 定义外键第三种方式,获取关联表的__str__函数返回字段
    # u = serializers.StringRelatedField()

    # 获取序列化对象
    # u = UserSerializers()



