from random import sample, choice

from faker import Faker

from movielist.models import Movie, Person
from showtimes.models import Cinema, Screening

faker = Faker("pl_PL")


def random_cinema():
    """Return a random Cinema object from db."""
    cinema = Cinema.objects.all()
    return choice(cinema)


def random_movies():
    """ Return a random Movie object from db."""
    movies = list(Movie.objects.all())
    return sample(movies, 3)


def random_screening():
    """Return a random Screening object from db."""
    screening = Screening.objects.all()
    return choice(screening)


def fake_cinema_data():
    """ Generate a dict of cinema data

    The format is compatible with serializers
    """
    cinema_data = {
        'name': faker.first_name(),
        'city': faker.city(),
    }
    # movies = Movie.objects.all()
    # movies_list = sample(list(movies), randint(1, len(movies)))
    # movie_titles = [m.title for m in movies_list]
    # cinema_data['movies'] = movie_titles
    return cinema_data


def find_movie_by_title(title):
    """Return the first Movie object that matches 'title' """
    return Movie.objects.filter(title=title).first()


def add_screening(cinema):
    movies = random_movies()
    for movie in movies:
        Screening.objects.create(cinema=cinema, movie=movie, date=faker.date_time())


def create_fake_cinema():
    """Generate new fake cinema and save to database"""
    cinema = Cinema.objects.create(**fake_cinema_data())
    add_screening(cinema)
    # cinema_data = fake_cinema_data()
    # # # movies_list = cinema_data['movies']
    # # # del cinema_data['movies']
    # # movies = list(Movie.objects.all())
    # # movies_list = sample(movies, 3)
    # #
    # # for movie in movies_list:
    # #     new_cinema = Cinema.objects.create(**cinema_data, )
    # #      # new_cinema.movies.add(find_movie_by_title(movie),
    # #      #                    through_defaults={'date': faker.date_time()})


def fake_screening_data():
    """Generate a dict of screening data

    The format is compatible with serializers
    """
    screening_data = {
        "cinema": random_cinema().name,
        "date": faker.iso8601(),
    }
    movie = choice(Movie.objects.all())
    screening_data['movie'] = movie.title

    return screening_data


def find_cinema_by_name(cinema):
    return Cinema.objects.filter(name=cinema).first()


# def create_fake_screening():
#     """Generate new fake screening and save to database"""
#     screening_data = fake_screening_data()
#     movie = screening_data['movie']
#     cinema = screening_data['cinema']
#     date = screening_data['date']
#     del screening_data['movie']
#     del screening_data['date']
#     del screening_data['cinema']
#     new_screening = Screening.objects.create(date=faker.date_time(),
#                                              movie=Movie.objects.first(),
#                                              cinema=find_cinema_by_name(cinema))
#     # new_screening.movie.add(find_movie_by_title(movie))
#     # new_screening.cinema.add(find_cinema_by_name(cinema))


def find_Screening_date(date):
    """Return the first `Screening` object that matches `date`."""
    return Person.objects.filter(date=date).first()
