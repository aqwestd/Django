from django.shortcuts import render
from .models import Lesson
from django.utils import timezone:
# Create your views here.
def post_list(request):
    return render(request, 'student/post_list.html', {})