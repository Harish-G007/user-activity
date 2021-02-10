from django.shortcuts import render
from rest_framework import generics
from .models import Member, ActivityPeriode
from .serializers import MemberSerializer


class MemberCreateView(generics.CreateAPIView):
    serializer_class = MemberSerializer
    queryset = ActivityPeriode.objects.all()