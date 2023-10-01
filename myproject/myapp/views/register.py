from rest_framework.authtoken.models import Token
from ..models import UserManager
from  ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

def register_user(request, is_super=False):
    email = request.data.get("email")
    password = request.data.get("password")
    password2 = request.data.get("password2")
    user_manager = UserManager()
    serializer = UserSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if password != password2:
        return Response({'error': 'Password incorrect'},
                        status=status.HTTP_400_BAD_REQUEST)

    if email is None and password is None:
        return Response({'error': 'Please provide email & password'},
                        status=status.HTTP_400_BAD_REQUEST)

    if is_super:
        user = user_manager.create_superuser(email=email, password=password)
    else:
        user = user_manager.create_user(email=email, password=password)

    if not user:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'is_super': user.is_superuser},
                    status=status.HTTP_200_OK)