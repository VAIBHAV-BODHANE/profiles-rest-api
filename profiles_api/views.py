from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list"""

        an_apiview = [
            'Vaibhav',
            'Akshay',
            'Apex',
            'APEXDEAD'
        ]

        return Response({'message': 'Hello Wolrd', 'an_apiview': an_apiview})