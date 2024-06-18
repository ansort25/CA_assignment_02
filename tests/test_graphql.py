from implementation.graphql.rick_and_morty_character import RMCharactersGql
import implementation.graphql.queries as q

rmc = RMCharactersGql()


def test_query_alien_hivemind_characters_with_success():
    """
    Expecting 200 OK with 2 characters
    """
    response = rmc.post_query(query=q.ALIEN_HIVEMIND_CHARACTERS)
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()['data']
    results = data['characters']['results']
    assert len(results) == 2
    for character in results:
        assert character['species'] == 'Alien'
        assert character['type'] == 'Hivemind'


def test_query_dead_asd_characters_with_success():
    """
    Expecting 200 OK with 0 characters
    """
    response = rmc.post_query(query=q.DEAD_ASD_NO_RESULTS_CHARACTERS)
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()['data']
    results = data['characters']['results']
    assert len(results) == 0


def test_query_id_name_species_gender_with_id_1_with_success():
    """
    Expecting 200 OK with 1 character and only fields id, name, species and gender are present and that character is the
    one with id 1
    """
    response = rmc.post_query(query=q.ID_NAME_SPECIES_GENDER_1_CHARACTER)
    assert response.status_code == 200
    assert response.elapsed.microseconds < 1000000
    data = response.json()['data']
    character = data['character']
    assert character['id'] == '1'
    assert character['name'] == 'Rick Sanchez'
    assert character['species'] == 'Human'
    assert character['gender'] == 'Male'
    for k in character.keys():
        assert k in ['id', 'name', 'species', 'gender']
