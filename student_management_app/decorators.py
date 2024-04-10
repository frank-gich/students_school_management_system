from django.http import HttpResponseForbidden


def hod_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "1":
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("you dont have permission to acces this page")
    return _wrapped_view

def staff_required(vew_func):
    def _wraped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "2":
            return view_fuc(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("you dont have acces to this page")
    return _wraped_view

def student_required(vew_func):
    def _wraped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "":
            return view_fuc(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("you dont have acces to this page")
    return _wraped_view