from flowerposts.models import FlowerPost
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

# Decorator function that handles all handler method exceptions
def handle_exceptions(handler_function):
    def wrapper(*args, **kwargs):
        try:
            return handler_function(*args, **kwargs)
        except (FlowerPost.DoesNotExist, NotFound) as e:
            print(type(e))
            return Response({ 'message': str(e) }, 404)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
            return Response('An unknown error occurred', 500)
    return wrapper