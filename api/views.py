from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from trackify_app.models import *



class Projects(viewsets.ModelViewSet):
    def get_queryset(self):
        get = self.request.query_params.get('get')
        size = self.request.query_params.get('size')
        if size is not None:
            self.pagination_class = PageNumberPagination
            PageNumberPagination.page_size = size
        if get is not None:
            queryset = Project.objects.prefetch_related('screenshots', 'timesheets').all()
        else:
            queryset = Project.objects.all()
        return queryset

    def get_serializer_class(self, *args, **kwargs):
        get = self.request.query_params.get('get')
        if get is not None:
            return SimpleProjectSerializer
        return ProjectSerializer


class ScreenShots(viewsets.ModelViewSet):
    serializer_class = ScreenShotSerializer
    def get_queryset(self):
        queryset = ScreenShot.objects.all()
        size = self.request.query_params.get('size')
        if size is not None:
            self.pagination_class = PageNumberPagination
            PageNumberPagination.page_size = size
        return queryset


class UserSettings(viewsets.ModelViewSet):
    serializer_class = UserSettingSerializer
    def get_queryset(self):
        queryset = UserSetting.objects.all()
        size = self.request.query_params.get('size')
        if size is not None:
            self.pagination_class = PageNumberPagination
            PageNumberPagination.page_size = size
        return queryset



class TimeSheets(viewsets.ModelViewSet):
    serializer_class = TimeSheetSerializer
    def get_queryset(self):
        queryset = TimeSheet.objects.all()
        size = self.request.query_params.get('size')
        if size is not None:
            self.pagination_class = PageNumberPagination
            PageNumberPagination.page_size = size
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TimeSheetSerializer
        return CreateTimeSheetSerializer

