def test_index(client, connection_wrapper_mock):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Pokedex</h1>\n " in response.data
