from .models import Information

def information_processor(request):
    """ Предоставляет information во все шаблоны """
    return {
        'information': Information.get_solo()
    }
