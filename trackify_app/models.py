from django.db import models
from clock import Clock
from clock import subtract_time, create_clock_from_str 
# Create your models here.

from django.contrib.auth.models import User

class Project(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=8, null=True, blank=True)
    idol = models.CharField(max_length=8, null=True, blank=True)
    clicks = models.IntegerField(null=True, blank=True)
    pressess = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return (f'{self.name}')
   
    @property
    def total_screens(self):
        screenshots = self.screenshot_set.all()  # type: ignore
        count = screenshots.count()
        return count

    @property
    def get_screenshot(self):
        screenshot = (self.screenshot_set.all()).first()  # type: ignore
        if screenshot:
            return str(screenshot.screenshot)
        else:
            return 'none'
    
    @property
    def get_activity(self):
        if self.time:
            total_time = create_clock_from_str(self.time)
            if self.idol:
                idol = create_clock_from_str(self.idol)
            else:
                idol = create_clock_from_str('00:00:00')
            work_time = subtract_time(total_time, idol)
            work_time_seconds = work_time.get_total_seconds()
            total_time_seconds = total_time.get_total_seconds()
            activity = (work_time_seconds * 100) / total_time_seconds
            return int(activity)
        return 0
    
    @property
    def get_worktime(self):
        if self.time:
            total_time = create_clock_from_str(self.time)
            if self.idol:
                idol = create_clock_from_str(self.idol)
            else:
                idol = create_clock_from_str('00:00:00') 
            work_time = subtract_time(total_time, idol)
            return work_time.get_time()
        return '00:00:00'




class ScreenShot(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='',default='')
    

class UserSetting(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Screenshot_dalay = models.IntegerField(null=True)
    
    
class TimeSheet(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('View', 'View'),
        ('Submit', 'Submit'),
        ('Approve', 'Approve'),
        ('Deny', 'Deny'),
    )
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='Open')