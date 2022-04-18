
import faker


import pytest

from movielist.models import Person
from showtimes.tests.utils import create_fake_cinema
from movielist.tests.utils import faker, create_fake_movie


@pytest.fixture
def set_up():
    for _ in range(5):
        Person.objects.create(name=faker.name())
    for _ in range(5):
        create_fake_movie()
    for _ in range(3):
        create_fake_cinema()
    # for _ in range(3):
    #     create_fake_screening()