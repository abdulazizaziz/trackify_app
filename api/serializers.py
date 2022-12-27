from rest_framework import serializers
from trackify_app.models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'user',
            'name',
            'time',
            'idol',
            'clicks',
            'pressess',
            # -----
            'total_screens',
            'get_screenshot',
            'get_activity',
            'get_worktime',
        ]


class ScreenShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenShot
        fields = [
            'id',
            'screenshot',
            'project'
        ]
    def create(self, validated_data):
        try:
            project_id = self.context["project_id"]
        except:
            return ScreenShot.objects.create(**validated_data)
        return ScreenShot.objects.create(project_id=project_id, **validated_data)

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = [
            'id',
            'user',
            'Screenshot_dalay',
        ]

class TimeSheetSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    def get_status(self, obj):
        return obj.get_status_display()
    class Meta:
        model = TimeSheet
        fields = [
            'id',
            'status',
            'project',
        ]

class CreateTimeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSheet
        fields = [
            'id',
            'status',
            'project',
        ]


class SimpleProjectSerializer(serializers.ModelSerializer):
    screenshots = ScreenShotSerializer(many=True, read_only=True)
    timesheets = TimeSheetSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = [
            'id',
            'user',
            'name',
            'time',
            'idol',
            'clicks',
            'pressess',
            'screenshots',
            'timesheets',
        ]