from rest_framework import filters

class IsPublicOrSuperuser(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(is_published=True)