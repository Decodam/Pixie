import django_filters
from Auth.models import Profile
from .models import Tag

class Userfilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = {
            'user__username': ['icontains']
        }

class Tagfilter(django_filters.FilterSet):
    class Meta:
        model = Tag
        fields = {
            'name': ['icontains']
        }


