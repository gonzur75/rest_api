import pytest
from pytz import UTC

from showtimes.models import Cinema, Screening
from showtimes.tests.utils import fake_cinema_data, fake_screening_data, faker


@pytest.mark.django_db
def test_add_cinema(client, set_up):
    cinemas_pre_test = Cinema.objects.count()
    new_cinema = fake_cinema_data()
    response = client.post("/cinemas/", new_cinema, format='json')
    assert response.status_code == 201
    assert Cinema.objects.all().count() == cinemas_pre_test + 1
    for key, value in new_cinema.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_get_cinema_list(client, set_up):
    response = client.get("/cinemas/", {}, format='json')

    assert response.status_code == 200
    assert Cinema.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_cinema_detail(client, set_up):
    cinema = Cinema.objects.first()
    response = client.get(f"/cinemas/{cinema.id}/", {}, format='json')
    assert response.status_code == 200
    for field in ('name', 'city', 'movies'):
        assert field in response.data


@pytest.mark.django_db
def test_delete_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.delete(f"/cinemas/{cinema.id}/", {}, format='json')
    assert response.status_code == 204
    cinema_ids = [cinema.id for cinema in Cinema.objects.all()]
    assert cinema.id not in cinema_ids


@pytest.mark.django_db
def test_update_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.get(f"/cinemas/{cinema.id}/", {}, format="json", content_type='application/json')
    cinema_data = response.data
    new_name = 'MCF'
    cinema_data['name'] = new_name
    response = client.patch(f"/cinemas/{cinema.id}/", cinema_data, format="json", content_type='application/json')
    assert response.status_code == 200
    cinema_obj = Cinema.objects.get(id=cinema.id)
    assert cinema_obj.name == new_name


@pytest.mark.django_db
def test_add_screening(client, set_up):
    pre_test_screening = Screening.objects.count()
    new_screening = fake_screening_data()
    response = client.post("/screenings/", new_screening, format='json')
    assert response.status_code == 201
    assert Screening.objects.count() == pre_test_screening + 1
    new_screening['date'] = f"{new_screening['date']}Z"
    for key, value in new_screening.items():
        # Compare contents regardless of their order
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_get_screening_list(client, set_up):
    response = client.get("/screenings/", {}, format='json')

    assert response.status_code == 200
    assert Screening.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_screening_detail(client, set_up):
    screening = Screening.objects.first()
    response = client.get(f"/screenings/{screening.id}/", {}, format='json')
    assert response.status_code == 200
    for field in ('cinema', 'movie', 'date'):
        assert field in response.data

@pytest.mark.django_db
def test_delete_screening(client, set_up):
    screening = Screening.objects.first()
    response = client.delete(f"/screenings/{screening.id}/", {}, format='json')
    assert response.status_code == 204
    screening_ids = [obj.id for obj in Screening.objects.all()]
    assert screening.id not in screening_ids


@pytest.mark.django_db
def test_update_screening(client, set_up):
    screening = Screening.objects.first()
    response = client.get(f"/screenings/{screening.id}/", {}, format='json')
    screening_data = response.data
    new_date = faker.date_time(tzinfo=UTC)
    screening_data['date'] = new_date
    response = client.patch(f"/screenings/{screening.id}/",
                            screening_data, format='json',
                            content_type='application/json')
    assert response.status_code == 200
    compare_obj = Screening.objects.get(id=screening.id)
    assert compare_obj.date == new_date


