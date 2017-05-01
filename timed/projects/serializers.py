"""Serializers for the projects app."""

from rest_framework_json_api.relations import ResourceRelatedField
from rest_framework_json_api.serializers import ModelSerializer

from timed.projects import models


class CustomerSerializer(ModelSerializer):
    """Customer serializer."""

    projects = ResourceRelatedField(read_only=True,
                                    many=True)

    included_serializers = {
        'projects': 'timed.projects.serializers.ProjectSerializer'
    }

    class Meta:
        """Meta information for the customer serializer."""

        model  = models.Customer
        fields = [
            'name',
            'email',
            'website',
            'comment',
            'archived',
            'projects',
        ]


class ProjectSerializer(ModelSerializer):
    """Project serializer."""

    customer = ResourceRelatedField(queryset=models.Customer.objects.all())
    tasks    = ResourceRelatedField(read_only=True,
                                    many=True)

    included_serializers = {
        'customer': 'timed.projects.serializers.CustomerSerializer',
        'tasks':    'timed.projects.serializers.TaskSerializer'
    }

    class Meta:
        """Meta information for the project serializer."""

        model  = models.Project
        fields = [
            'name',
            'comment',
            'estimated_hours',
            'archived',
            'customer',
            'tasks',
        ]


class TaskSerializer(ModelSerializer):
    """Task serializer."""

    activities = ResourceRelatedField(read_only=True,
                                      many=True)
    project    = ResourceRelatedField(queryset=models.Project.objects.all())

    included_serializers = {
        'activities': 'timed.tracking.serializers.ActivitySerializer',
        'project':    'timed.projects.serializers.ProjectSerializer'
    }

    class Meta:
        """Meta information for the task serializer."""

        model  = models.Task
        fields = [
            'name',
            'estimated_hours',
            'archived',
            'project',
            'activities',
        ]