from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_null=False, allow_blank=False, min_length=10, max_length=50)
    surname = serializers.CharField(allow_null=False, allow_blank=False, min_length=5, max_length=50)
    year_of_study = serializers.IntegerField()
    def create(self, validated_data):
        student = Student(**validated_data)
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.student_year_of_study = validated_data.get('student_year_of_study', instance.student_year_of_study)
        instance.save()
        return instance

