# Third Party Libraries
from apistar.exceptions import NotFound
from django.shortcuts import get_object_or_404 as django_get_object_or_404
from django.shortcuts import _get_queryset


def get_object_or_404(klass, *args, **kwargs):
    """
    Use get() to return an object, or raise a Http404 exception if the object
    does not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Like with QuerySet.get(), MultipleObjectsReturned is raised if more than
    one object is found.
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except AttributeError:
        klass__name = klass.__name__ if isinstance(klass, type) else klass.__class__.__name__
        raise ValueError("First argument to get_object_or_404() must be a Model, Manager, "
                         "or QuerySet, not '%s'." % klass__name)
    except queryset.model.DoesNotExist:
        raise NotFound('No %s matches the given query.' % queryset.model._meta.object_name)
