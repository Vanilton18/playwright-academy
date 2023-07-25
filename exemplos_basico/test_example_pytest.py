import pytest


class Music:

    def __init__(self, nome):
        self.nome = nome

    def __eq__(self, outra):
        return self.nome == outra.nome


@pytest.fixture
def minha_musica():
    return Music("Black")


@pytest.fixture
def playlist(minha_musica):
    return [Music("Numb"), minha_musica]


def test_minha_musica_na_playlist(playlist):
    assert Music('Numb') in playlist
