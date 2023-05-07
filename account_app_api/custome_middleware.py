from django.http import JsonResponse

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed before view is called

        if request.path != "/backend/signin/" and request.path != "/backend/signup/" and request.path != "/backend/sendotp/":

            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Authentication required'}, status=401)

        response = self.get_response(request)

        # Code to be executed after view is called

        return response