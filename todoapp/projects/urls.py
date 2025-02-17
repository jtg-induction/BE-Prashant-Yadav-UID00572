from django.urls import path

from projects.views import ProjectMemberApiViewSet

app_name = 'projects'

urlpatterns = [
    path('<int:pk>/<str:action>/', ProjectMemberApiViewSet.as_view(
        {'put': 'update', 'patch': 'update'}), name='projectmemberupdate'),
]
