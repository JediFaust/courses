from rest_framework import serializers
from coursesapp.models import Course, LANGUAGE_CHOICES, STYLE_CHOICES


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'actual', 'language', 'style']