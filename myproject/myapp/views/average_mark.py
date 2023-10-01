# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Mark,Teacher
from ..serializers import AverageMarksBySubjectSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg

class AverageMarksBySubjectForTeacher(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Check if the user is a teacher (superuser)
        if not request.user.is_superuser:
            return Response({'detail': 'You are not authorized to access this endpoint.'}, status=403)

        # Get the logged-in teacher based on their username
        teacher = Teacher.objects.get(user=request.user)

        # Calculate average marks by subject for the teacher
        average_marks = (
            Mark.objects
            .filter(subject__teacher=teacher)
            .values('subject__name')
            .annotate(average_mark=Avg('score'))
        )

        # Serialize the data
        serializer = AverageMarksBySubjectSerializer(average_marks, many=True)

        return Response(serializer.data)
