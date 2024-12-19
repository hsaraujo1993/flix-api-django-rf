from rest_framework import permissions


class AppPermissionGlobal(permissions.BasePermission):

    def has_permission(self, request, view):

        method_permissions = {
            'GET': ['genres.view_genre', 'actors.view_actor', 'movies.view_movie', 'reviews.view_review'],
            'OPTIONS': ['genres.view_genre', 'actors.view_actor', 'movies.view_movie', 'reviews.view_review'],
            'HEAD': ['genres.view_genre', 'actors.view_actor', 'movies.view_movie', 'reviews.view_review'],
            'POST': ['genres.add_genre', 'actors.add_actor', 'movies.add_movie', 'reviews.add_review'],
            'PUT': ['genres.change_genre', 'actors.change_actor', 'movies.change_movie', 'reviews.change_review'],
            'PATCH': ['genres.change_genre', 'actors.change_actor', 'movies.change_movie', 'reviews.change_review'],
            'DELETE': ['genres.delete_genre', 'actors.delete_actor', 'movies.delete_movie', 'reviews.delete_review'],
        }

        required_perms = method_permissions.get(request.method, [])

        return request.user.has_perms(required_perms)
