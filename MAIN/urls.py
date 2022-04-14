from django.contrib import admin
from django.urls import path, include
from MAIN import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('member/', include("APPS.MEMBER.urls")),
    path('order/', include("APPS.ORDER.urls")),
    path('pick/', include("APPS.PICK.urls")),
    path('present/', include("APPS.PRESENT.urls")),
    path('review/', include("APPS.REVIEW.urls")),
    path('product/', include("APPS.PRODUCT.urls")),
    path('service/', include("APPS.SERVICE.urls")),
]