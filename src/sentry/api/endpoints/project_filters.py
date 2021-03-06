from __future__ import absolute_import

from rest_framework.response import Response

from sentry import message_filters
from sentry.api.bases.project import ProjectEndpoint


class ProjectFiltersEndpoint(ProjectEndpoint):
    def get(self, request, project):
        """
        List a project's filters

        Retrieve a list of filters for a given project.

            {method} {path}

        """
        results = []
        for flt in message_filters.get_all_filter_specs():
            results.append(
                {
                    "id": flt.id,
                    # 'active' will be either a boolean or list for the legacy browser filters
                    # all other filters will be boolean
                    "active": message_filters.get_filter_state(flt.id, project),
                    "description": flt.description,
                    "name": flt.name,
                    "hello": flt.id + " - " + flt.name,
                }
            )
        results.sort(key=lambda x: x["name"])
        return Response(results)
