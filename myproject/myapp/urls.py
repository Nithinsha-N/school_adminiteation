from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import login,student_signup,teacher_signup,MarkViewSet,TeacherViewSet,SubjectViewSet,AverageMarksBySubjectForTeacher
from .views import viewsets

teacher = DefaultRouter()

teacher.register(r"mark", MarkViewSet)
teacher.register(r"profile",TeacherViewSet)
teacher.register(r"subjects", SubjectViewSet)


student = DefaultRouter()

# student.register(r"subjects", views.SubjectViewSetStudent)
# student.register(r"profile", views.StudentViewsetStudent)
# student.register(r"mark", views.MarkViewsetStudent)

app_name = 'api'
urlpatterns = [
    path("login/", login),
    path("teachers/signup/",teacher_signup),
    path("students/signup/", student_signup),
    path("teachers/averagemark",AverageMarksBySubjectForTeacher.as_view()),

    # path("teachers/", include((teacher.urls, 'teacher'))),
    # path("students/", include((student.urls, 'student')))
]