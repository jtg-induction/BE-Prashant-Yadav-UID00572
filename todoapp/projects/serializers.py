from django.db.models import Count

from rest_framework import serializers

from projects import models as project_models
from users import models as user_models


class ProjectWithMemberName(serializers.ModelSerializer):
    done = serializers.SerializerMethodField()
    project_name = serializers.CharField(source="name")

    def get_done(self, obj):
        return True if obj.status == 2 else False

    class Meta:
        model = project_models.Project
        fields = ['project_name', 'done', 'max_members']


class ProjectSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    existing_member_count = serializers.IntegerField()

    class Meta:
        model = project_models.Project
        fields = ["id", "name", "status",
                  "existing_member_count", "max_members"]

    def get_status(self, obj):
        return obj.get_status_display()


class UserReportSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()
    completed_count = serializers.IntegerField()

    class Meta:
        model = user_models.CustomUser
        fields = ["first_name", "last_name", "email",
                  "pending_count", "completed_count"]


class ProjectReportSerializer(serializers.ModelSerializer):
    project_title = serializers.CharField(source="name")
    report = UserReportSerializer(source="reports", many=True, read_only=True)

    class Meta:
        model = project_models.Project
        fields = ['project_title', 'report']


class ProjectMemberSerializer(serializers.ModelSerializer):
    user_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=user_models.CustomUser.objects.all(),
        write_only=True
    )

    class Meta:
        model = project_models.Project
        fields = ['user_ids']

    def update(self, instance, validated_data):
        action = self.context['action']
        existing_members = instance.members.values_list('id', flat=True)
        remaining_slots = instance.max_members - len(existing_members)
        valid_users = [user.id for user in validated_data['user_ids']]
        logs = {}

        if action == 'add':
            user_data = list(user_models.CustomUser.objects.filter(id__in=valid_users).annotate(
                project_count=Count('projects')
            ))
            new_members = []
            for user in user_data:
                if remaining_slots <= 0:
                    logs[user.id] = 'Project has reached its maximum member count.'
                elif user.project_count >= 2:
                    logs[user.id] = 'Cannot add user as they are already in two projects.'
                elif user.id in existing_members:
                    logs[user.id] = 'User is already a member of this project.'
                else:
                    logs[user.id] = 'Successfully added to the project.'
                    new_members.append(project_models.ProjectMember(
                        project=instance, member=user))
                    remaining_slots -= 1
            project_models.ProjectMember.objects.bulk_create(new_members)
        elif action == 'remove':
            for user_id in valid_users:
                if user_id not in existing_members:
                    logs[user_id] = 'User is not a member of this project.'
                else:
                    logs[user_id] = 'Successfully removed from the project.'
            project_models.ProjectMember.objects.filter(
                member_id__in=valid_users).delete()
        self.context['logs'] = logs

        return instance

    def to_representation(self, instance):
        data = {}
        data['logs'] = self.context['logs']
        return data
