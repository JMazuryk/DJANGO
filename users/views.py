from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class TestView(APIView):
    def get(self, request):
        return Response("Hello World mGet")

    def post(self, request):
        return Response("Hello World method post")

    def put(self, request):
        return Response("Hello World method put")

    def patch(self, request):
        return Response("Hello World method patch")

    def delete(self, request):
        return Response("Hello World method delete")


users = [
    {'id': 1, 'name': 'max1', 'age': 15},
    {'id': 2, 'name': 'max2', 'age': 16},
    {'id': 3, 'name': 'max3', 'age': 17},
    {'id': 4, 'name': 'max4', 'age': 18},
]


class UserListCreateView(APIView):
    def get(self, request):
        return Response(users)

    def post(self, *args, **kwargs):
        params_dict = self.request.query_params.dict()
        print(params_dict)
        new_user = self.request.data
        users.append(new_user)
        return Response(new_user)


class UserRetrieveUpdateDestroy(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        for user in users:
            if user['id'] == pk:
                return Response (user)
        return Response('Not Found')
        # print(kwargs.get('pk'))
        # print(kwargs.get('name'))
