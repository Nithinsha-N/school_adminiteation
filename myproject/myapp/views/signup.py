from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .register import register_user


@api_view(['POST'])
def teacher_signup(request):
    return register_user(request=request, is_super=True)


@api_view(['POST'])
def student_signup(request):
    return register_user(request=request, is_super=False)