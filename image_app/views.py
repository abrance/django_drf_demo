from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView

from image_app.models import ImageInfo
from image_app.serializers import ImageInfoSerializer


# class ImageInfoViewSet(ModelViewSet):
#     queryset = ImageInfo.objects.all()
#     serializer_class = ImageInfoSerializer

class ImageListView(GenericAPIView):
    serializer_class = ImageInfoSerializer
    queryset = ImageInfo.objects.all()
    # 指定对象

    def get(self, request):
        imgs = self.get_queryset()

        serializer = self.get_serializer(imgs, many=True)

        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)     # 验证失败，直接抛出400异常

        # 2. 创建图书数据并保存到数据库
        # 反序列化-数据保存(调用create)
        serializer.save()

        # 3. 将新增图书数据通过json返回
        return Response(serializer.data, status=status.HTTP_201_CREATED)

