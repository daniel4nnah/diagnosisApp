from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from initprototipo import views

router = routers.DefaultRouter()
router.register(r'todos', views.users_list, 'todo')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/users/', views.users_list),
    path('api/medico/', views.personal_salud),
]
