# Third Party Libraries
from apistar.exceptions import NotFound
from django.http import Http404
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404


def aps_get_object_or_404(klass, *args, **kwargs):
    """
    mock django exceptions to apistar exeception
    """
    try:
        result = get_object_or_404(klass, *args, **kwargs)
    except Http404 as erreur:
        raise NotFound(erreur)

    return result


def aps_get_list_or_404(klass, *args, **kwargs):
    """
    mock django exceptions to apistar exeception
    """
    try:
        result = get_list_or_404(klass, *args, **kwargs)
    except Http404 as erreur:
        raise NotFound(erreur)

    return result
