from implementation.rest.rick_morty_character import RMCharacters

rmc = RMCharacters()


def test_get_by_id_with_id_25_with_success():
    """
    Testing /character/25
    Expecting 200 OK
    """
    response = rmc.get_by_id(ids='25')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['id'] == 25
    assert data['name'] == 'Armothy'


def test_get_by_id_with_id_92_13_with_success():
    """
    Testing /character/92,13
    Expecting 200 OK
    """
    response = rmc.get_by_id(ids=('92', '13'))
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert len(data) == 2
    assert data[0]['id'] == 13
    assert data[0]['name'] == 'Alien Googah'
    assert data[1]['id'] == 92
    assert data[1]['name'] == 'Davin'


def test_get_by_id_with_id_negative_1_4_with_success():
    """
    Testing /character/-1,4
    Expecting 200 OK
    """
    response = rmc.get_by_id(ids=('-1', '4'))
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert len(data) == 1
    assert data[0]['id'] == 4
    assert data[0]['name'] == 'Beth Smith'


def test_get_by_id_with_id_0_with_no_success():
    """
    Testing /character/0
    Expecting 404 Not Found
    """
    response = rmc.get_by_id('0')
    assert response.status_code == 404
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['error'] == 'Character not found'


def test_get_by_id_with_id_900_with_no_success():
    """
    Testing /character/0
    Expecting 404 Not Found
    """
    response = rmc.get_by_id('900')
    assert response.status_code == 404
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['error'] == 'Character not found'
