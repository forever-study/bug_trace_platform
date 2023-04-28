from bug_trace.project_settings.django_settings import *



try:
    from .local_settings import *
except:
    import traceback
    traceback.print_exc()