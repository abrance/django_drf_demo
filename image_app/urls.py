from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from image_app import views


urlpatterns = [
    # url(r'^image_app/$', views.ImageListView.as_view(), name='image_app'),
    # url(r'^image_app/(?P<pk>\d+)/$', views.ImageDetailView.as_view(), name='image-detail'),

    # url(r'^image_app/$', views.ImageViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create',
    #     'favorite_img': 'favorite_img'
    # })),
    # url(r'^image_app/(?P<pk>\d+)/$', views.ImageViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),    # 这里的已经能自动生成参数name了

]

from rest_framework.routers import SimpleRouter, DefaultRouter
# router = SimpleRouter()
router = DefaultRouter()

# 2. 注册视图集
router.register(r'image_app', views.ImageViewSet, base_name='image_app')

# 3. 添加到urlpatterns中
urlpatterns += router.urls


# router = DefaultRouter()
# # router.register('books', views.BookInfoViewSet, name='books')
# router.register('image_app', views.ImageListView)
#
# urlpatterns += router.urls
#
