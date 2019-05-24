from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from image_app.models import ImageInfo, ImageSearchContext
from image_app.serializers import ImageInfoSerializer, ImageSearchContextSerializer


class StandardResultPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5

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
    # authentication_classes = [SessionAuthentication]    # 视图设置，只用设置一种就够了
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [AnonRateThrottle]       # 局部限流
    # filter_backends = [OrderingFilter]
    # pagination_class = StandardResultPagination

    # 可以带过滤参数了 image_app/?img_read=10
    # filter_field = ('img_read', 'img_pub_date')

    @action(methods=['get'], detail=False)
    def favorite_img(self, request):
        # 获得好评最多的数据，从高到低
        # img_list = ImageInfo.objects.all().order_by('-img_good_star')
        img_list = self.get_queryset().order_by('-img_good_star')

        serializer = self.get_serializer(img_list, many=True)
        return Response(serializer.data)
