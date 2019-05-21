from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from image_app import views


urlpatterns = [
    url(r'^image_app/$', views.ImageListView.as_view(), name='image_app'),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='books-detail'),
]

# router = DefaultRouter()
# # router.register('books', views.BookInfoViewSet, name='books')
# router.register('image_app', views.ImageListView)
#
# urlpatterns += router.urls
#
