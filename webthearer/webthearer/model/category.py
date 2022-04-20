from typing import List

from webthearer.webthearer.model.movie import Movie


class Category:

    def __init__(self, id, title, description, image_path, movie_list: list[Movie]):
        self._id = id
        self._title = title
        self._description = description
        self._image_path = image_path
        self._movie_list = movie_list


    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    
    def getTitle(self):
        return self._title

    def setTitle(self, titulo):
        self._title = titulo


    def getDescription(self):
        return self._description
    
    def setDescription(self, description):
        self._description = description

    
    def getImagePath(self):
        return self._image_path

    def setImagePath(self, image_path):
        self._image_path = image_path

    
    def getMovieList(self):
        return self._movie_list

    def setMovieList(self, movie):
        self._movie_list.append(movie)