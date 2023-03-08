from .auth import auth_ns, user_ns
from .main import movies_ns, directors_ns, genres_ns, favorites_ns

__all__ = [
    'user_ns',
    'auth_ns',
    'movies_ns',
    'directors_ns',
    'genres_ns',
    'favorites_ns'
]
