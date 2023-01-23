from .forms import SubRubric


def bboard_context_processor(request):
    context = dict()
    context['rubrics'] = SubRubric.objects.all()
    return context
