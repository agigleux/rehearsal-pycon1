from unittest.mock import Mock

import pytest
from pokedex import app as poke_app


@pytest.fixture()
def app():
    poke_app.app.config.update({
        "TESTING": True,
    })
    yield poke_app.app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def connection_wrapper_mock():
    poke_app.helper.ConnectionWrapper.get_all_pokemons = Mock(return_value=[(1, "Foo", "", "Bar")])

