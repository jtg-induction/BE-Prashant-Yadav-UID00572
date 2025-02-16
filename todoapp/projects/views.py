from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from projects import (
    models as project_models,
    serializers as project_serializers
)

class ProjectMemberApiViewSet(ModelViewSet):
    """
       constraints
        - a user can be a member of max 2 projects only
        - a project can have at max N members defined in database for each project
       functionalities
       - add users to projects

         Request
         { user_ids: [1,2,...n] }
         Response
         {
           logs: {
             <user_id>: <status messages>
           }
         }
         following are the possible status messages
         case1: if user is added successfully then - "Member added Successfully"
         case2: if user is already a member then - "User is already a Member"
         case3: if user is already added to 2 projects - "Cannot add as User is a member in two projects"

         there will be many other cases think of that

       - update to remove users from projects

         Request
         { user_ids: [1,2,...n] }

         Response
         {
           logs: {
             <user_id>: <status messages>
           }
         }

         there will be many other cases think of that and share on forum
    """
    permission_classes = [AllowAny]
    serializer_class = project_serializers.ProjectMemberSerializer

    def get_serializer_context(self):
        context =  super().get_serializer_context()
        context['action'] = self.kwargs.get('action')
        return context

    def get_queryset(self):
        project_id = self.kwargs.get('pk')
        return project_models.Project.objects.filter(id=project_id)
