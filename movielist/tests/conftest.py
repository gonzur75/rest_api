import os
import sys

import pytest
from faker import Faker
from rest_framework.test import APIClient

from movielist.models import Person
from showtimes.tests.utils import create_fake_cinema
from .utils import faker, create_fake_movie

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


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
