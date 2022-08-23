from rest_framework import routers
from rental import views

router = routers.DefaultRouter()
router.register('friends', views.FriendViewSet),
router.register('belongings', views.BelongingViewSet),
router.register('borrowings', views.BorrowedViewSet)