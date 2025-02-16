from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from projects import models as project_models
from users import models as user_models


class ProjectMemberAPITests(APITestCase):

    def setUp(self):
        self.user1 = user_models.CustomUser.objects.create(
            email='test1@gmail.com',
            first_name='test',
            last_name='user',
            password='somepassword'
        )
        self.user2 = user_models.CustomUser.objects.create(
            email='test2@gmail.com',
            first_name='test',
            last_name='user',
            password='somepassword'
        )
        self.user3 = user_models.CustomUser.objects.create(
            email='test3@gmail.com',
            first_name='test',
            last_name='user',
            password='somepassword'
        )
        self.project1 = project_models.Project.objects.create(
            name="TestProject1", max_members=2
        )
        self.project2 = project_models.Project.objects.create(
            name="TestProject2", max_members=3
        )
        self.project3 = project_models.Project.objects.create(
            name="TestProject3", max_members=4
        )
        self.url_add = reverse(
            'projects:projectmemberupdate', kwargs={'pk': self.project1.id, 'action': 'add'}
        )
        self.url_remove = reverse(
            'projects:projectmemberupdate', kwargs={'pk': self.project1.id, 'action': 'remove'}
        )

    def test_adding_members_to_project(self):
        response = self.client.patch(
            self.url_add,
            {'user_ids': [self.user2.id, self.user3.id]},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(project_models.ProjectMember.objects.filter(
            project=self.project1, member=self.user2).exists())
        self.assertTrue(project_models.ProjectMember.objects.filter(
            project=self.project1, member=self.user3).exists())
        self.assertEqual(
            response.data['logs'][self.user2.id], 'Successfully added to the project.')
        self.assertEqual(
            response.data['logs'][self.user3.id], 'Successfully added to the project.')

    def test_remove_users_from_project(self):
        project_models.ProjectMember.objects.create(
            project=self.project1, member=self.user1)
        project_models.ProjectMember.objects.create(
            project=self.project1, member=self.user2)
        response = self.client.patch(
            self.url_remove,
            {'user_ids': [self.user1.id, self.user2.id]},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(project_models.ProjectMember.objects.filter(
            project=self.project1, member=self.user1).exists())
        self.assertFalse(project_models.ProjectMember.objects.filter(
            project=self.project1, member=self.user2).exists())
        self.assertEqual(
            response.data['logs'][self.user1.id], 'Successfully removed from the project.')
        self.assertEqual(
            response.data['logs'][self.user2.id], 'Successfully removed from the project.')

    def test_addding_existing_member(self):
        project_models.ProjectMember.objects.create(
            project=self.project1, member=self.user1)
        response = self.client.patch(
            self.url_add,
            {'user_ids': [self.user1.id]},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['logs'][self.user1.id], 'User is already a member of this project.')

    def test_user_already_in_two_projects(self):
        project_models.ProjectMember.objects.create(
            project=self.project2, member=self.user1)
        project_models.ProjectMember.objects.create(
            project=self.project3, member=self.user1)
        response = self.client.patch(
            self.url_add,
            {'user_ids': [self.user1.id]},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(project_models.ProjectMember.objects.filter(
            project=self.project1, member=self.user1).exists())
        self.assertEqual(response.data['logs'][self.user1.id],
                         'Cannot add user as they are already in two projects.')

    def test_cannot_add_members_project_full(self):
        project_models.ProjectMember.objects.create(
            project=self.project1, member=self.user1)
        project_models.ProjectMember.objects.create(
            project=self.project1, member=self.user2)
        response = self.client.patch(
            self.url_add,
            {'user_ids': [self.user3.id]},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(project_models.ProjectMember.objects.filter(
            project=self.project1, member=self.user3).exists())
        self.assertEqual(response.data['logs'][self.user3.id],
                         'Project has reached its maximum member count.')

    def test_cannot_remove_non_member(self):
        response = self.client.patch(
            self.url_remove,
            {'user_ids': [self.user1.id]},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['logs'][self.user1.id], 'User is not a member of this project.')
