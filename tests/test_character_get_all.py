import pytest
from implementation.rick_morty_character import RMCharacters

rmc = RMCharacters()


def test_get_all_without_page_with_success():
    """
    Testing /character/
    Expecting 200 OK
    """
    response = rmc.get_all()
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 826
    assert data['info']['next'] == 'https://rickandmortyapi.com/api/character/?page=2'
    assert data['results'][0]['id'] == 1
    assert data['results'][0]['name'] == 'Rick Sanchez'


def test_get_all_with_page_3_with_success():
    """
    Testing /character/?page=3
    Expecting 200 OK
    """
    response = rmc.get_all(page=3)
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 826
    assert data['info']['next'] == 'https://rickandmortyapi.com/api/character/?page=4'
    assert data['results'][0]['id'] == 41
    assert data['results'][0]['name'] == 'Big Boobed Waitress'


def test_get_all_with_page_0_with_success():
    """
    Testing /character/?page=0
    Expecting 200 OK
    """
    response = rmc.get_all(page=0)
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 826
    assert data['info']['next'] == 'https://rickandmortyapi.com/api/character/?page=2'
    assert data['results'][0]['id'] == 1
    assert data['results'][0]['name'] == 'Rick Sanchez'


def test_get_all_with_page_1000_with_no_success():
    """
    Testing /character/?page=100
    Expecting 404 Not Found
    """
    response = rmc.get_all(page=100)
    assert response.status_code == 404
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['error'] == 'There is nothing here'
