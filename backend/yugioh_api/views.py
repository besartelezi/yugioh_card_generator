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
    

class MonsterCardDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, card_id, user_ïd):
        '''
        Helper method to get the object with the given card_id, and user_id
        '''
        try:
            return MonsterCard.objects.get(id = card_id, user = user_ïd)
        except MonsterCard.DoesNotExist:
            return None
        
    # 3. Retrieve
    def get(self, request, card_id, *args, **kwargs):
        '''
        Retrieves the Monster Card with given card_id
        '''
        card_instance = self.get_object(card_id, request.user.id)
        if not card_instance:
            return Response(
                {
                    "res": "Object with card id does not exist"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = MonsterCardSerializer(card_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 4. Update
    def put(self, request, card_id, *args, **kwargs):
        '''
        Updates the Monster Card with given card_id if exists
        '''
        card_instance = self.get_object(card_id, request.user.id)
        if not card_instance:
            return Response(
                {
                    "res": "Object with card id does not exist"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
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
        serializer = MonsterCardSerializer(instance = card_instance, data = data, partial = True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 5. Delete
    def delete(self, request, card_id, *args, **kwargs):
        '''
        Deletes the Monster Card with given card_id if exists
        '''
        card_instance = self.get_object(card_id, request.user.id)
        if not card_instance:
            return Response(
                {
                    "res": "Object with given card id does not exist"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        card_instance.delete()
        return Response(
            {
                "res": "Object deleted!"
            },
            status=status.HTTP_200_OK
        )
