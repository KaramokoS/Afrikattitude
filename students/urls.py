from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static

app_name = 'student'

urlpatterns = [
    path('courses/', StudentCourseListView.as_view(), name='student_course_list'),
    path('courses/<pk>', cache_page(60*15)(StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('courses/<pk>/<module_id>/', cache_page(60*15)(StudentCourseDetailView.as_view()), name='student_course_detail_module'),
    path('register/', StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
]
