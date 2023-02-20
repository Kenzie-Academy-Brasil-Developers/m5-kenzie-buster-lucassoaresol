from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsUserEmployee
from .serializers import MovieSerializer
from .models import Movie


class MovieView(APIView):
    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

    def post(self, req: Request) -> Response:
        authentication_classes = [JWTAuthentication]
