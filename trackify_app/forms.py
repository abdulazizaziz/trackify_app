from django.forms import ModelForm
from .models import Project, UserSetting, ScreenShot
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class ScreenshotForm(ModelForm):
    class Meta:
        model = ScreenShot
        fields = '__all__'

class UserSettingForm(ModelForm):
    class Meta:
        model = UserSetting
        fields = '__all__'