from functools import wraps
from django.http import HttpResponseForbidden

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden('Access denied: You do not have permission to perform this action.')
        return wrapper
    return decorator