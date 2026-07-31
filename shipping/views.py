from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OrderRequestSerializer
from .services import recommend_box

def home(request):
    return JsonResponse({
        "message": "AI-Assisted Box Selection System",
        "status": "Running",
        "api": "/api/recommend-box/",
        "admin": "/admin/"
    })

class RecommendBoxAPIView(APIView):

    def post(self, request):

        serializer = OrderRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        box = recommend_box(serializer.validated_data["items"])
        if isinstance(box, dict):
           return Response(
              box,
              status=status.HTTP_400_BAD_REQUEST
           )

        if box is None:
            return Response(
                {
                    "message": "No suitable box found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {
                "recommended_box": box.name,
                "cost": str(box.cost),
                "dimensions": {
                    "length": box.length,
                    "width": box.width,
                    "height": box.height,
                },
                "max_weight": box.max_weight,
            }
        )