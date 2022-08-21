from flask import request
from flask_restx import Namespace, Resource

from project.container import favorite_movie_service, user_service, movie_service
from project.services.auth_service import auth_required
from project.setup.api.models import favorite_movie

api = Namespace('favorites')


@api.route('/movies/<int:movie_id>')
class FavoritesView(Resource):
    @api.marshal_with(favorite_movie, as_list=True, code=200, description='OK')
    @auth_required
    def post(self, movie_id):
        token = request.headers.environ.get('HTTP_AUTHORIZATION').replace("Bearer ", "")
        user = user_service.get_user_by_token(token)

        return user

    @api.marshal_with(favorite_movie, as_list=True, code=200, description='OK')
    @auth_required
    def delete(self, movie_id):
        #favorite_movie_id = movie_service.get_item(movie_id)

        favorite_movie_service.delete_movie(movie_id)
