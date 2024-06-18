from implementation.rest.rick_morty_character import RMCharacters

rmc = RMCharacters()


def test_get_filtered_name_smith_with_success():
    """
    Testing /character/?name=Smith
    Expecting 200 OK
    """
    response = rmc.get_filtered(name='Smith')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 19
    assert data['info']['next'] is None
    for character in data['results']:
        assert 'Smith' in character['name']


def test_get_filtered_name_andrei_with_no_success():
    """
    Testing /character/?name=Andrei
    Expecting 404 OK
    """
    response = rmc.get_filtered(name='Andrei')
    assert response.status_code == 404
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['error'] == 'There is nothing here'


def test_get_filtered_status_alive_with_success():
    """
    Testing /character/?status=Alive
    Expecting 200 OK
    """
    response = rmc.get_filtered(status='Alive')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 439
    assert data['info']['pages'] == 22
    for character in data['results']:
        assert character['status'] == 'Alive'


def test_get_filtered_status_dead_with_success():
    """
    Testing /character/?status=Dead
    Expecting 200 OK
    """
    response = rmc.get_filtered(status='Dead')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 287
    assert data['info']['pages'] == 15
    for character in data['results']:
        assert character['status'] == 'Dead'


def test_get_filtered_status_unknown_with_success():
    """
    Testing /character/?status=Unknown
    Expecting 200 OK
    """
    response = rmc.get_filtered(status='Unknown')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 100
    assert data['info']['pages'] == 5
    for character in data['results']:
        assert character['status'] == 'unknown'


def test_get_filtered_status_noalive_with_no_success():
    """
    Testing /character/?status=noalive
    Expecting 404 Not Found
    """
    response = rmc.get_filtered(status='noalive')
    assert response.status_code == 404
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['error'] == 'There is nothing here'


def test_get_filtered_species_human_with_success():
    """
    Testing /character/?species=human
    Expecting 200 OK
    Test fails because there are some status values with 'Humanoid'. It means that the API checks for characters that
    have species that contains 'human', and it does not search for exact match. I would raise an issue for this. Also,
    it is not case-sensitive.
    """
    response = rmc.get_filtered(species='human')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 434
    assert data['info']['pages'] == 22
    for character in data['results']:
        assert character['species'] == 'Human'


def test_get_filtered_species_fish_with_no_success():
    """
    Testing /character/?species=fish
    Expecting 404 Not Found
    """
    response = rmc.get_filtered(species='fish')
    assert response.status_code == 404
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['error'] == 'There is nothing here'


def test_get_filtered_type_mytholog_with_success():
    """
    Testing /character/?type=Mytholog
    Expecting 200 OK
    """
    response = rmc.get_filtered(type='Mytholog')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 6
    for character in data['results']:
        assert character['type'] == 'Mytholog'


def test_get_filtered_type_grgrgr_with_no_success():
    """
    Testing /character/?type=grgrgr
    Expecting 404 Not Found
    """
    response = rmc.get_filtered(type='grgrgr')
    assert response.status_code == 404
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['error'] == 'There is nothing here'


def test_get_filtered_gender_male_with_success():
    """
    Testing /character/?gender=male
    Expecting 200 OK
    """
    response = rmc.get_filtered(gender='male')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 610
    for character in data['results']:
        assert character['gender'] == 'Male'


def test_get_filtered_gender_female_with_success():
    """
    Testing /character/?gender=female
    Expecting 200 OK
    """
    response = rmc.get_filtered(gender='female')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 148
    for character in data['results']:
        assert character['gender'] == 'Female'


def test_get_filtered_gender_genderless_with_success():
    """
    Testing /character/?gender=genderless
    Expecting 200 OK
    """
    response = rmc.get_filtered(gender='genderless')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 19
    for character in data['results']:
        assert character['gender'] == 'Genderless'


def test_get_filtered_gender_unknown_with_success():
    """
    Testing /character/?gender=unknown
    Expecting 200 OK
    """
    response = rmc.get_filtered(gender='unknown')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 49
    for character in data['results']:
        assert character['gender'] == 'unknown'


def test_get_filtered_gender_xyz_with_no_success():
    """
    Testing /character/?gender=xyz
    Expecting 404 Not Found
    """
    response = rmc.get_filtered(gender='xyz')
    assert response.status_code == 404
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['error'] == 'There is nothing here'


def test_get_filtered_status_unknown_and_type_mytholog_with_success():
    """
    Testing /character/?status=unknown&type=mytholog
    Expecting 200 OK
    """
    response = rmc.get_filtered(status='unknown', type='mytholog')
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['info']['count'] == 2
    for character in data['results']:
        assert character['status'] == 'unknown'
        assert character['type'] == 'Mytholog'


def test_get_filtered_name_smith_and_type_mytholog_with_no_success():
    """
    Testing /character/?name=smith&type=mytholog
    Expecting 404 Not Found
    """
    response = rmc.get_filtered(name='smith', type='mytholog')
    assert response.status_code == 404
    assert response.elapsed.microseconds < 1000000
    data = response.json()
    assert data['error'] == 'There is nothing here'
