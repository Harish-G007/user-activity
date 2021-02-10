from rest_framework import serializers
from .models import ActivityPeriode, Member
from django.contrib.auth.models import User


class ActivityPeriodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriode
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name"]


class MemberSerializer(serializers.ModelSerializer):
    activity_period = ActivityPeriodeSerializer(many=True)
    member = UserSerializer()

    class Meta:
        model = Member
        fields = ["member", "activity_period", "real_name", "tz"]

