from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializers, OrderSerializers
from user.models import UserModel, OrderModel
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin


class SaveUser(APIView):

    def get(self, request):
        pass

    def post(self, request):
        data = request.data
        serializer = UserSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = {"code": 200}
        for i in serializer.data:
            result[i] = serializer.data[i]
        return Response(result)


class QueryUser(APIView):
    def get(self, request):
        querySet = UserModel.objects.all()
        serializer = UserSerializers(instance=querySet, many=True)
        jsonResult = {"code": 200, "userList":serializer.data}
        return Response(jsonResult)

    def post(self, request):
        pass


class GetUser(APIView):
    def get(self, request, id):
        querySet = UserModel.objects.get(id=id)
        serializer = UserSerializers(instance=querySet)
        jsonResult = {"code": 200, "data": serializer.data}
        return Response(jsonResult)

    def post(self, request):
        pass


class UpdateUser(APIView):
    def get(self, request):
        pass

    def post(self, request):
        data = request.data
        querySet = UserModel.objects.get(id=data.get("id"))
        serializer = UserSerializers(data=data, instance=querySet)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("修改成功")


class DeleteUser(APIView):
    def get(self, request, id):
        UserModel.objects.get(id=id).delete()
        return Response("删除成功")

    def post(self, request):
        pass


class SaveOrder(GenericAPIView,
                CreateModelMixin):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers

    def get(self, request):
        pass

    def post(self, request):
        self.create(request)
        return Response("保存成功")


class UpdateOrder(GenericAPIView,
                  UpdateModelMixin):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers
    lookup_field = "id"

    def get(self, request):
        pass

    def post(self, request, id):
        self.update(request)
        return Response("修改成功")


class ListOrder(GenericAPIView,
                ListModelMixin):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers

    def get(self, request):

        return self.list(request)

    def post(self, request):
        pass


class QueryOrder(GenericAPIView,
                 RetrieveModelMixin):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers

    def get(self, request, pk):

        return self.retrieve(request)

    def post(self, request):
        pass


class DelOrder(GenericAPIView,
               DestroyModelMixin):

    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers

    def get(self, request, pk):
        self.destroy(request)
        return Response("删除成功")

    def post(self, request):
        pass
