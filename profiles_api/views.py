from rest_framework.views import APIView
from rest_framework.response import Response


class ApiView(APIView):
    """Api view"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview =[
            'Uses HTTP methods as function (get, post, pathc, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the must control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': "Hello my friend", 'an_apiview': an_apiview})
