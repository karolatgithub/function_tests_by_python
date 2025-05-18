import pytest
from name_function import get_formattes_name

@pytest.fixture
def simple_names():
    """ dane wejsciowe i wyjscie do testow """
    return {'names': ['abcde', 'efghijklm'], 'output': 'Abcde Efghijklm'}

@pytest.fixture
def full_names():
    """ dane wejsciowe i wyjscie do testow """
    return {'names': ['abcde', 'xyz', 'efghijklm'], 'output': 'Abcde Xyz Efghijklm'}

@pytest.fixture
def full_names2n():
    """ dane wejsciowe i wyjscie do testow """
    return {'names': [None, '', 'efghijklm'], 'output': 'Efghijklm'}

def test_simple_get_formattes_name(simple_names):
    """ Czy dobrze dziala funkcja get_formattes_name z imieniem i nazwiskiem """
    names=simple_names['names'];
    assert get_formattes_name(names[0], names[1]) == simple_names['output']

def test_full_get_formattes_name(full_names):
    """ Czy dobrze dziala funkcja get_formattes_name z imieniem, drugim
    imieniem i nazwiskiem """
    names=full_names['names'];
    assert get_formattes_name(names[0], names[1], names[2]) == full_names['output']

def test_full2nd_get_formattes_name(full_names2n):
    """ Czy dobrze dziala funkcja get_formattes_name z imieniem, drugim
    imieniem i nazwiskiem """
    names=full_names2n['names'];
    assert get_formattes_name(names[0], names[1], names[2]) == full_names2n['output']

def test_empty_get_formattes_name():
    """ Czy dobrze dziala funkcja get_formattes_name bez """
    assert get_formattes_name() == None

def test_none1s_get_formattes_name():
    """ Czy dobrze dziala funkcja get_formattes_name z pustym """
    assert get_formattes_name(None) == None

def test_none2nd_get_formattes_name():
    """ Czy dobrze dziala funkcja get_formattes_name z pustym """
    assert get_formattes_name(None, None) == None

def test_none3rd_get_formattes_name():
    """ Czy dobrze dziala funkcja get_formattes_name z pustym """
    assert get_formattes_name(None, None, None) == None
