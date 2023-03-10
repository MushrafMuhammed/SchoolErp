from rest_framework import serializers

from teacher.models import Attendance, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

class CheckAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ["student","date"]
        