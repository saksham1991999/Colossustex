from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from . import models, forms

def HomeView(request):

    return redirect('employee:home')


def ToDoList(request):
    todolists = models.to_do.objects.filter(user=request.user)
    context = {
        'todolists': todolists,
    }
    return render(request, 'apps_todoList.html',context)


def ToDoEdit(request, id):

    return redirect('core:todo')


def ToDoMarkDelete(request, id):
    todo = models.to_do.objects.get(id=id)
    todo.is_deleted = True
    todo.is_completed = False
    todo.is_important = False
    todo.save()
    return redirect('core:todo')


def ToDoMarkImportant(request, id):
    todo = models.to_do.objects.get(id=id)
    todo.is_important = True
    todo.save()
    return redirect('core:todo')


def ToDoMarkComplete(request, id):
    todo = models.to_do.objects.get(id=id)
    todo.is_completed = True
    todo.is_important = False
    todo.save()
    return redirect('core:todo')


def ToDoPermanentDelete(request, id):
    todo = models.to_do.objects.get(id=id)
    todo.delete()
    return redirect('core:todo')


def ToDoReviveTask(request, id):
    todo = models.to_do.objects.get(id=id)
    todo.is_deleted = False
    todo.save()
    return redirect('core:todo')

def NotesList(request):
    notes = models.note.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, 'notes.html',context)