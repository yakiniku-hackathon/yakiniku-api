from django.urls import path

from .views import get_glb_model, get_glb_vps

urlpatterns = [
    path("glb/model/", get_glb_model, name="get_glb_model"),
    path("glb/vps/", get_glb_vps, name="get_glb_vps"),
]