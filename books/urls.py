from rest_framework.routers import DefaultRouter
from books import views

urlpatterns = [

]

router = DefaultRouter()
# router.register('books', views.BookInfoViewSet, name='books')
router.register('books', views.BookInfoViewSet)

urlpatterns += router.urls

