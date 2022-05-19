from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterUserSerializer


class RegisterUserAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)
