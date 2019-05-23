from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from image_app.models import ImageInfo, ImageSearchContext
from image_app.serializers import ImageInfoSerializer, ImageSearchContextSerializer


# class ImageInfoViewSet(ModelViewSet):
#     queryset = ImageInfo.objects.all()
#     serializer_class = ImageInfoSerializer

# class ImageListView(ListCreateAPIView, GenericAPIView):
#     # 指定对象
#     serializer_class = ImageInfoSerializer
#     queryset = ImageInfo.objects.all()
    # def get(self, request):
    #     imgs = self.get_queryset()
    #
    #     serializer = self.get_serializer(imgs, many=True)
    #
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     # print(request.data)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)     # 验证失败，直接抛出400异常
    #
    #     # 2. 创建图书数据并保存到数据库
    #     # 反序列化-数据保存(调用create)
    #     serializer.save()
    #
    #     # 3. 将新增图书数据通过json返回
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ImageDetailView(RetrieveUpdateDestroyAPIView, GenericAPIView):
#     serializer_class = ImageInfoSerializer
#     queryset = ImageInfo.objects.all()

    # def get(self, request, pk):
    #     try:
    #         image = self.get_object()
    #     except ImageInfo.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     serializer = ImageInfoSerializer(image)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     img = self.get_object
    #
    #     serializer = ImageInfoSerializer(img, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     serializer.save()
    #
    #     return Response(serializer.data)
    #
    # def delete(self, request, pk):
    #     img = self.get_object()
    #
    #     serializer = ImageInfoSerializer(img, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     img.delete()
    #
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ImageViewSet(ModelViewSet):
    serializer_class = ImageInfoSerializer
    queryset = ImageInfo.objects.all()

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=['get'], detail=False)
    def favorite_img(self, request):
        # 获得好评最多的数据，从高到低
        # img_list = ImageInfo.objects.all().order_by('-img_good_star')
        img_list = self.get_queryset().order_by('-img_good_star')

        serializer = self.get_serializer(img_list, many=True)
        return Response(serializer.data)
