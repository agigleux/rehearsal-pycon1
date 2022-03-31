from pokedex import helper


def test_fetch_all_pokemon(connection_wrapper_mock):
    assert len(helper.fetch_all_pokemons()) == 1
