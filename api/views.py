"""
Views to process API requests.
"""

from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import IPEDSDictionary
from .serializers import IPEDSDictionarySerializer

@api_view(['GET'])
def get_ipeds_dictionary(request):
    """
    Get data from the IPEDSDictionary model.

    Valid keys to pass in:
    - model_name: The name of the model in which the variable is stored. Use
      this when you want to get all variables for a particular model(s).
    - varname: The raw, non-human-readable name of the column.

    Parameter values should be formatted as a list, even if you are only
    querying a single value. E.g., {'varname': ['ZIP']}
    """
    valid_keys = [
        'model_name',
        'varname',
    ]
    queryset = IPEDSDictionary.objects.all()

    if request.query_params:

        # Validate keys passed in params
        invalid_keys = [key for key in request.query_params
                        if key not in valid_keys]
        if invalid_keys:
            raise Http404(f'Invalid keys: {invalid_keys}')

        # Filter
        for key, value in dict(request.query_params).items():
            kwarg = {f'{key}__in': value}
            queryset = queryset.filter(**kwarg)

    serializer = IPEDSDictionarySerializer(queryset, many=True)

    return Response(serializer.data)
