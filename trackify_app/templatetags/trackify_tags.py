from ..models import Project
from django import template

register = template.Library()

@register.simple_tag
def get_project(user):
    project = Project.objects.get(user=user)
    return project.name

@register.simple_tag
def get_project_activity(user):
    project = Project.objects.get(user=user)
    return project.get_activity

@register.simple_tag
def get_project_time(user):
    project = Project.objects.get(user=user)
    return project.get_worktime

@register.simple_tag
def get_screenshot(project):
    screenshots = project.screenshot_set.all()  # type: ignore
    if screenshots:
        return screenshots[0].screenshot
    return 'none'