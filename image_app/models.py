from django.db import models


class ImageInfo(models.Model):
    """图片模型类"""
    img_title = models.CharField(max_length=20, verbose_name='标题')
    img = models.ImageField(upload_to='media', verbose_name='信息')
    # 这里以后要填入width_field,height_field，ImageField的属性
    img_pub_date = models.DateField(auto_now=True, verbose_name='发布日期')
    img_read = models.IntegerField(default=0, verbose_name='阅读量')
    img_good_star = models.IntegerField(default=0, verbose_name='好评量')
    # img_comment_info = models.CharField(default='', max_length=200, verbose_name='评论')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        db_table = 'tb_images'
        verbose_name = '图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.img_title


class ImageSearchContext(models.Model):
    """图片搜索字段模型类"""
    txt = models.CharField(max_length=100, verbose_name='字段')
    txt_img_info = models.ForeignKey('ImageInfo', on_delete=models.CASCADE, verbose_name='所属图片')
    # img_comment_info = models.CharField(default='', max_length=200, verbose_name='评论')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        db_table = 'tb_images_search_context'
        verbose_name = '图片搜索字段'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.txt
