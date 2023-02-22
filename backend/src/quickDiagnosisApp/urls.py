from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from initprototipo import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'todos', views.users_list, 'todo')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('api/users/', views.users_list),
    path('api/medico/', views.personal_salud),
    path('api/externo/', views.usuario_externo),
    path('api/csv/', views.import_csv),

]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
