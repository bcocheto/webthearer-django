from django.shortcuts import render
from webthearer.webthearer.model.category import Category
from webthearer.webthearer.model.movie import Movie

movie1 = Movie(1, "How To Skin and Debone a Fish", "Food", "debone.jpg", 'https://youtu.be/g-jsayvbpYU',
               '2 de abr. de 2022', 48000, 702.055)
movie2 = Movie(2, "How To Make Chicken Enchiladas", "Food", "enchiladas.jpeg", 'https://youtu.be/wNQx34RQZtI',
               '27 de ago. de 2020', 135000, 3.638.352)
movie3 = Movie(3, "How To Survive Squid Game", "Life Style", "squid-game.jpg", 'https://youtu.be/Im45WxYMDo4',
               '9 de out. de 2021', 284000, 5.142.651)
movie4 = Movie(4, "How To Protect Yourself From Coronavirus", "Life Style", "corona.jpeg",
               'https://youtu.be/UBy19XGCgpE', '1 de dez. de 2020', 226000, 4.614.020)
movie5 = Movie(5, "How To Speed Up Your Internet", "Technology", "internet.jpg", "https://youtu.be/58PuGTecJUU",
               "23 de jun. de 2021", 162000, 3.248.365)
movie6 = Movie(6, "How To Fix a Printer", "Technology", "printer.jpg", "https://youtu.be/wxNYCZeW7YI",
               "19 de fev. de 2021", 205000, 8.468.983)

category1 = Category(1, "Food",
                     "food, substance consisting essentially of protein, carbohydrate, fat, and other nutrients used in the body of an organism to sustain growth and vital processes and to furnish energy. The absorption and utilization of food by the body is fundamental to nutrition and is facilitated by digestion.",
                     "food.jpg", [movie1, movie2])
category2 = Category(2, "Life Style",
                     "defines a lifestyle as the way a person lives. This includes patterns of social relations, consumption, entertainment, and dress. A lifestyle typically also reflects an individual's attitudes, values or worldview.",
                     "lifestyle.jpg", [movie3, movie4])
category3 = Category(2, "Technology",
                     "the application of scientific knowledge for practical purposes, especially in industry.",
                     "technology.jpeg", [movie5, movie6])

categories = [category1, category2, category3]


def index(request):
    return render(request, 'index.html', {'list': categories})


def video(request, id):
    for category in categories:
        for movie in category.getMovieList():
            if movie.getId() == int(id):
                return render(request, 'movies.html', {'movie': movie})
