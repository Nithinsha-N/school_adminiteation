from rest_framework import serializers


class AverageMarksBySubjectSerializer(serializers.Serializer):
    subject = serializers.CharField()
    average_mark = serializers.DecimalField(max_digits=5, decimal_places=2)