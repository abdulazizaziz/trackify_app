from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register('projects', Projects, basename='projects')
router.register('screenshots', ScreenShots, basename='screenshots')
router.register('usersettings', UserSettings, basename='screenshots')
router.register('timesheets', TimeSheets, basename='timesheets')


urlpatterns = [
    path('', include(router.urls))
]