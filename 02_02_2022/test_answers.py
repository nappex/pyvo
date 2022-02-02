import pytest

from answers import get_result

def make_mock_input(generator):
    def mock_input(*args, **kwargs):
        return next(generator)
    return mock_input


def test_get_result(monkeypatch):
    def generator_of_inputs():
        yield from ("Mocknuta_odpoved_c_1", "Mocknuta_odpoved_c_2")

    gen = generator_of_inputs()
    mocked_input = make_mock_input(gen)
    monkeypatch.setattr('builtins.input', mocked_input)

    result = get_result()

    assert result == ["Mocknuta_odpoved_c_1", "Mocknuta_odpoved_c_2"]

