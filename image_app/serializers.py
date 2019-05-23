from rest_framework import serializers

from image_app.models import ImageInfo, ImageSearchContext


class ImageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageInfo
        # fields = '__all__'
        # 将所有字段序列化
        # read_only_fields = ('id', 'bread', 'bcomment')
        exclude = ('is_delete',)


class ImageSearchContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSearchContext
        exclude = ('is_delete',)
