from django.urls import path
from .views import list_and_create, sort_by_name, sort_by_email, sort_by_date

urlpatterns = [
    path('', list_and_create, name='submit_form'),
    path('sort-by-name/', sort_by_name, name='sort_by_name'),
    path('sort-by-email/', sort_by_email, name='sort_by_email'),
    path('sort-by-date/', sort_by_date, name='sort_by_date'),
]
