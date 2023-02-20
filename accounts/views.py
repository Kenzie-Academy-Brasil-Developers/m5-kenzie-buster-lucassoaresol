from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer


class UserView(APIView):
    def post(self, req: Request) -> Response:
        req.data["is_superuser"] = req.data.get("is_employee", False)

        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
