from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, ScreenShot, TimeSheet, UserSetting
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from project import Project as _Project
from clock import Clock, seconds_to_clock
from clock import create_clock_from_str, subtract_time


# Create your views here.

def total_time_worked(projects):
    total_time = 0
    for project in projects:
        if project.time:
            time = create_clock_from_str(project.time)
            if project.idol:
                idol = create_clock_from_str(project.idol)
            else:
                idol = create_clock_from_str('00:00:00')
            work_time = subtract_time(time, idol)
            work_time = work_time.get_total_seconds()

            total_time += work_time

    return seconds_to_clock(total_time)


def total_activity(projects):
    activity = 0
    total_time = 0
    for project in projects:
        time = create_clock_from_str(project.time)
        time_seconds = time.get_total_seconds()
        total_time += time_seconds

    work_time = total_time_worked(projects)
    total_worktime = work_time.get_total_seconds()
    activity = (total_worktime * 100) / total_time

    return int(activity)


def index(request):
    context = {}
    try:
        users = User.objects.all().exclude(username='admin')
        try:
            projects = Project.objects.all()
            total_time = total_time_worked(projects)
            activity = total_activity(projects)
            context.update({
                'projects': projects,
                'total_time': total_time.get_time(),
                'total_activity': activity,
                'users': users})
            try:
                screenshots = ScreenShot.objects.all()
                context.update({'screenshots': screenshots})
            except:
                pass
        except:
            pass
    except:
        pass

    return render(request, 'index.html', context)


def approvals(request):
    timesheets = TimeSheet.objects.all()
    if request.method == 'GET':
        if request.GET.get('View'):
            timesheet = TimeSheet.objects.get(id=request.GET['View'])
            timesheet.status = 'View'
            timesheet.save()
        elif request.GET.get('Submit'):
            timesheet = TimeSheet.objects.get(id=request.GET['Submit'])
            timesheet.status = 'Submit'
            timesheet.save()
        elif request.GET.get('Approve'):
            timesheet = TimeSheet.objects.get(id=request.GET['Approve'])
            timesheet.status = 'Approve'
            timesheet.save()
        elif request.GET.get('Deny'):
            timesheet = TimeSheet.objects.get(id=request.GET['Deny'])
            timesheet.status = 'Deny'
            timesheet.save()
        else:
            return render(request, 'approvals.html', {'timesheets': timesheets})
    return render(request, 'approvals.html', {'timesheets': timesheets})


def screenshots(request):
    try:
        users_list = User.objects.all().exclude(username='admin')
        project = Project.objects.get(user=users_list[0])
        if request.method == 'POST':
            selected_user = User.objects.get(username=request.POST['username'])
            project = Project.objects.get(user=selected_user)
            return render(request, 'screenshots.html', {'users': users_list, 'user': selected_user, 'project': project})
        return render(request, 'screenshots.html', {'users': users_list, 'project': project})
    except:
        return render(request, 'screenshots.html')


def users(request):
    projects = Project.objects.all()
    if request.method == 'GET':
        delete_user(request.GET.get('Delete'))

    if 'query' in request.GET:
        query = request.GET['query']
        users = User.objects.filter(username__icontains=query).exclude(username='admin')
        return render(request, 'users.html', {'projects': projects, 'users': users})
    else:
        users = User.objects.all().exclude(username='admin')
        usernames = User.objects.all().values_list('username', flat=True)
        if request.method == 'POST':
            if request.POST['username'] in usernames:
                messages.info(request, 'User cannot be added as Username has been already taken')
                return render(request, 'users.html', {'projects': projects, 'users': users})
            user = User(
                username=request.POST['username'],
                email=request.POST['email'])

            user.set_password(request.POST['password'])
            user.save()
            try:
                project = Project.objects.get(name=request.POST['project'])
                project.user = user
                project.save()
                messages.success(request, 'User succesfully added')
            except:
                return render(request, 'users.html', {'projects': projects, 'users': users})
    return render(request, 'users.html', {'projects': projects, 'users': users})


def settings_projects(request):
    return render(request, 'settings_projects.html')


def projects(request):
    projects = Project.objects.all()
    if 'query' in request.GET:
        query = request.GET['query']
        projects = Project.objects.filter(name__icontains=query)
        return render(request, 'projects.html', {'projects': projects})
    if request.method == 'POST':
        for project in projects:
            if project.name == request.POST['project_name']:
                messages.info(request, 'Project with this name already exists')
                return render(request, 'projects.html', {'projects': projects})

        project = Project(name=request.POST['project_name'])
        project.save()
        TimeSheet.objects.create(project=project)
        return redirect('projects')
    return render(request, 'projects.html', {'projects': projects})


def view_screenshots(request, pk):
    project = Project.objects.get(id=pk)
    try:
        screenshots = project.screenshot_set.all()  # type: ignore
        return render(request, 'view_screenshots.html', {'screenshots': screenshots})
    except:
        return redirect('index')


def delete_user(pk):
    try:
        user = User.objects.get(id=pk)
        user.delete()
    except:
        pass
    return redirect('users')


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('projects')


def sign_in(username, password):
    return authenticate(username=username, password=password) is not None


def get_object(username):  # this method returns user, user settings and all the projects of that user
    object = {}
    try:
        user = User.objects.get(username=username)
        try:
            project = Project.objects.get(user=user)
            user_projects = []
            user_projects.append(
                {
                    "project name": project.name,
                    "project time": project.time,
                    "project idol": project.idol,
                    "project screenshots": get_screenshots(project),
                    "project clicks": project.clicks,
                    "project presses": project.pressess
                }
            )
            object.update({"projects": user_projects})
        except Project.DoesNotExist:
            object.update({"projects": list()})
            # projects contain list of projects
        try:
            user_setting = UserSetting.objects.get(user=user)
            object.update({'settings': user_setting.Screenshot_dalay})  # type: ignore
        except UserSetting.DoesNotExist:
            object.update({"settings": {"screenshot delay": 5}})

    except User.DoesNotExist:
        print("The user does not exist")
    return object


def get_screenshots(project):  # this method returns list of screenshots of a given project
    screenshots = project.screenshot_set.all()
    user_screenshots = []
    for screenshot_ in screenshots:
        user_screenshots.append(screenshot_.screenshot.name)
    return user_screenshots


def update_project(username, project: _Project):
    try:
        user = User.objects.get(username=username)
        try:
            project_obj = Project.objects.get(name=project.project_name)
            project_obj.name = project.project_name
            project_obj.time = project.project_time
            project_obj.idol = project.project_idol_time
            project_obj.clicks = project.clicks
            project_obj.pressess = project.presses
            project_obj.save()

            screenshots = project_obj.screenshot_set.all()  # type: ignore

            for screenshot in screenshots:
                screenshot.delete()

            for screenshot in project.screen_shots:
                ScreenShot.objects.create(
                    project=project_obj,
                    screenshot=screenshot.replace("static/screenshots/", '')
                )

        except Project.DoesNotExist:
            project_obj = Project(
                user=user,
                name=project.project_name,
                time=project.project_time,
                idol=project.project_idol_time,
                clicks=project.clicks,
                pressess=project.presses,
            )
            project_obj.save()

            for screenshot in project.screen_shots:
                ScreenShot.objects.create(
                    project=project_obj,
                    screenshot=screenshot,
                )

    except User.DoesNotExist:
        print("The user does not exist")


def update_userSetting(username, screenshot_delay):
    try:
        user = User.objects.get(username=username)
        try:
            user_setting = UserSetting.objects.get(user=user)
            user_setting.Screenshot_dalay = screenshot_delay
            user_setting.save()
        except UserSetting.DoesNotExist:
            UserSetting.objects.create(
                user=user,
                screenshot_delay=screenshot_delay
            )
    except User.DoesNotExist:
        print("The user does not exist")


def settings(request):
    return render(request, 'settings.html')


def teams(request):
    return render(request, 'teams.html')


def time_activity(request):
    try:
        projects = Project.objects.all()
        return render(request, 'time_activity.html', {'projects': projects})
    except:
        return render(request, 'time_activity.html')


def todos(request):
    return render(request, 'todos.html')


def urls(request):
    return render(request, 'urls.html')


def viewedit(request):
    return render(request, 'viewedit.html')


def weekly(request):
    return render(request, 'weekly.html')


def apps(request):
    return render(request, 'apps.html')


def quickcheck(request):
    return render(request, 'quickcheck.html')


def reports(request):
    return render(request, 'reports.html')
