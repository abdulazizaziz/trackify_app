from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register('projects', Projects, basename='projects')
router.register('screenshots', ScreenShots, basename='screenshots')
router.register('usersettings', UserSettings, basename='screenshots')
router.register('timesheets', TimeSheets, basename='timesheets')


project_router = routers.NestedDefaultRouter(router, 'projects', lookup='project')
project_router.register('screenshots', ScreenShots, basename='project-screenshtos')
# project_router.register('timesheets', project_view.TimeSheets, basename='timesheet-screenshtos')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls))
]