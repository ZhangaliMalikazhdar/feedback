from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Feedback
from .forms import FeedbackForm
from .serializers import FeedbackSerializer


def list_and_create(request):
    feedbacks = Feedback.objects.filter(is_accepted=True)
    form = FeedbackForm()
    if request.method == "POST":
        print('posted')
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            form.Feedback()
            form.save()
            return JsonResponse({"name": name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "feedback.html", {"form": form, 'feedbacks': feedbacks})


def sort_by_email(request):
    form = FeedbackForm()
    if request.method == 'POST':
        feedbacks = Feedback.objects.filter(is_accepted=True).order_by('email')
    else:
        feedbacks = Feedback.objects.filter(is_accepted=True).order_by('-date_created')

    context = {"form": form, 'feedbacks': feedbacks}
    return render(request, 'feedback.html', context)


def sort_by_name(request):
    form = FeedbackForm()
    if request.method == 'POST':
        feedbacks = Feedback.objects.filter(is_accepted=True).order_by('name')
    else:
        feedbacks = Feedback.objects.filter(is_accepted=True).order_by('-date_created')

    context = {"form": form, 'feedbacks': feedbacks}
    return render(request, 'feedback.html', context)


def sort_by_date(request):
    form = FeedbackForm()
    if request.method == 'POST':
        feedbacks = Feedback.objects.filter(is_accepted=True).order_by('-date_created')
    else:
        feedbacks = Feedback.objects.filter(is_accepted=True).order_by('-date_created')

    context = {"form": form, 'feedbacks': feedbacks}
    return render(request, 'feedback.html', context)


# @api_view(['GET'])
# def sort_by_name(request):
#     sort_form = FeedbackForm(request.POST)
#     if sort_form.is_valid():
#         needed_sort = sort_form.cleaned_data.get("sort_form")
#     else:
#         needed_sort = ''
#     feedbacks = Feedback.objects.filter(is_accepted=True)
#     queryset = feedbacks.order_by('name')
#     serializer = FeedbackSerializer(queryset, many=True)
#     return HttpResponse(serializer.data, status=HTTP_200_OK)

