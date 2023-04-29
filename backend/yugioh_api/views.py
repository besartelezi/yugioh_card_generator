from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import MonsterCard
from .serializers import MonsterCardSerializer

# Create your views here.
# This class view will deal with the endpoint, handling all GET for MonsterCards, and POST for creating new MonsterCards
class MonsterCardListApiView(APIView):
    # add permissions to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Monster Cards for given requested user
        '''
        monster_cards = MonsterCard.objects.filter(user = request.user.id)
        serializer = MonsterCardSerializer(monster_cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the Monster Card with given data
        '''
        data = {
            'name': request.data.get('name'),
            'attribute': request.data.get('attribute'),
            'stars': request.data.get('stars'),
            'type': request.data.get('type'),
            'description': request.data.get('description'),
            'attack': request.data.get('attack'),
            'defense': request.data.get('defense'),
            'user': request.user.id,
        }
        serializer = MonsterCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)