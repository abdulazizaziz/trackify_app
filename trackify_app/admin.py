from django.contrib import admin
from .models import Project, ScreenShot, TimeSheet, UserSetting
# Register your models here.
class UserSettingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserSetting._meta.get_fields() if field.name != "id"]


admin.site.register(UserSetting, UserSettingAdmin)
admin.site.register(Project)
admin.site.register(ScreenShot)
admin.site.register(TimeSheet)
