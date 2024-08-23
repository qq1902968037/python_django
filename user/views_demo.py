from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.generic import View


from user.models import UserModel, OrderModel
from user.serializers import UserSerializers, OrderSerializers
import json


# Create your views here.




def test(request):
    user = UserModel.objects.get(id=2)
    order = user.ordermodel_set.all()
    serializer = UserSerializers(instance=user)
    # serializer = UserSerializers(instance=user, many=False)
    data = serializer.data
    order_list = []
    for o in order:
        order_list.append({
            "name": o.name
        })
    data['order_list'] = order_list
    return JsonResponse(data, safe=False)


def test2(request):
    user = UserModel.objects.all()
    userSerializer = UserSerializers(instance=user, many=True)

    for i in range(0, len(userSerializer.data)):
        uid = userSerializer.data[i]['id']
        order = OrderModel.objects.filter(u_id=uid)
        orderModel = OrderSerializers(instance=order, many=True)
        userSerializer.data[i]['order_list'] = orderModel.data
    return JsonResponse(userSerializer.data, safe=False)


class SaveUser(View):

    def get(self, request):
        data = {"name": "admin", "age": 22, "sex": "男", "sal": 10000}
        header = request.META['HTTP_USER_AGENT']
        print(header)
        # UserModel.objects.create(**data)
        userModel = UserModel(**data)
        # userModel.save()
        return HttpResponse("添加成功")

    def post(self, request):
        # header = request.META['HTTP_USER_AGENT']
        # print(header)
        # data = json.loads(request.body)
        # userModel = UserModel(**data)
        # userModel.save()
        userSerializer = UserSerializers(data=json.loads(request.body.decode()))
        if not userSerializer.is_valid():
            return HttpResponse("反序列化失败")
        userSerializer.save()
        return HttpResponse("添加成功")

class UpdateUser(View):

    def get(self, request):
        # UserModel.objects.create(**data)
        UserModel.objects.filter(id=2).update(name="李四")
        return HttpResponse("修改成功")

    def post(self, request):
        pass


class QueryUser(View):

    def get(self, request):
        object = UserModel.objects.all()
        userModel = UserSerializers(data=object, many=True)
        try:
            userModel.is_valid()
        except:
            print("序列化失败")
        return JsonResponse(userModel.data, safe=False)

    def post(self, request):
        object = UserModel.objects.all()
        data = serializers.serialize('json', object)
        return JsonResponse(data, safe=False)


class OrderSave(View):

    def post(self, request):
        data = json.loads(request.body.decode())
        orderSerializers = OrderSerializers(data=data)
        if not orderSerializers.is_valid(raise_exception=True):
            return HttpResponse("反序列化失败")
        orderSerializers.save()
        return HttpResponse("添加成功")

