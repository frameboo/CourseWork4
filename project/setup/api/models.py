from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Быков'),
})

movie: Model = api.model('Фильмы', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Корпорация монстров'),
    'description': fields.String(required=True, max_length=100,
                                 example='В мире монстров есть такая работа — пугать человеческих детей. '
                                         'Смешной мультфильм от Pixar про жизнь страшилищ'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=vpKxMNGPVMY'),
    'year': fields.String(required=True, example=2001),
    'rating': fields.String(required=True, example=8.4),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='monstermike@mail.ru'),
    'password': fields.String(required=True, example='MikeTheMonster'),
    'name': fields.String(required=True, example='Mike'),
    'surname': fields.String(required=True, example='Wazowski'),
    'favorite_genre_rel': fields.Nested(genre)
})

favorite_movie: Model = api.model('Избранные фильмы', {
    'id': fields.Integer(required=True, example=1),
    'user_idr': fields.Nested(user),
    'movie_idr': fields.Nested(movie)
})
