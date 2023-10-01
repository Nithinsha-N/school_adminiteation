from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token


@csrf_exempt
@api_view(['POST'])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None and password is None:
        return Response({'error': 'Please provide user & password'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'is_super': user.is_superuser},
                    status=status.HTTP_200_OK)