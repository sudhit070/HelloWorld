from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
# from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContactSerializer
from rest_framework import status


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactApi(APIView):
    def post(self, request):
        data = request.data
        try:
            serializer = ContactSerializer(data=data)
            if serializer.is_valid() :
                serializer.save()
                return Response(data={'msgs': 'All done'}, status=status.HTTP_200_OK)
            else :
                 return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(data={'msg': 'Something Went Wrong'}, status=status.HTTP_400_BAD_REQUEST)