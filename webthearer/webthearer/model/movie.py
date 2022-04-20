class Movie:
    
    def __init__(self, id, title, description, image_path, movie_path, piblication_data, likes_send, visualizations):
        self.id = id
        self.title = title
        self.description = description
        self.image_path = image_path
        self.movie_path = movie_path
        self.publication_data = piblication_data
        self.likes_send = likes_send
        self.visualizations = visualizations
        


    def getId(self):
        return self.id 

    def setId(self, id):
        self.id = id 

    
    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    
    def getDescription(self):
        return self.description

    def set_description(self, description):
        self.description


    def getImagePath(self):
        return self.image_path

    def setImagePath(self, image_path):
        self.image_path = image_path


    def getMoviePath(self):
        return self.movie_path

    def setMoviePath(self, movie_path):
        self.movie_path = movie_path


    def getPublicationData(self):
        return self.publication_data

    def setPublicationData(self, publication_data):
        self.publication_data = publication_data
    

    def getLikesSend(self):
        return self.likes_send

    def setLikesSend(self, likes_send):
        self.likes_send = likes_send


    def getVisualizations(self):
        return self.visualizations

    def setVisualizations(self, visualizations):
        self.visualizations = visualizations


