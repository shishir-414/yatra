from django.http import JsonResponse
from django.views import View
import json

class UserView(View):
    def get(self, request):
        users= \
        [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'},
            {'id': 3, 'name': 'Charlie'}
        ]
        return JsonResponse(users,status=200, safe=False)

    def post(self,request):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            if not name or not email:
                return JsonResponse({'error': 'Name and email are required.'}, status=400)
            return JsonResponse(
                {
                    'message': 'successfully created user',
                    'status': 201,
                    'data': {
                        'email': email,
                        'name': name
                    }

                },status=201
            )
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class UserDetailView(View):

    def get(self, request, id):
        return JsonResponse({
            "status": 200,
            "message": f"User {id} fetched"
        })

    def put(self, request, id):
        return JsonResponse({
            "status": 200,
            "message": f"User {id} updated"
        })

    def delete(self, request, id):
        return JsonResponse({
            "status": 200,
            "message": f"User {id} deleted"
        })