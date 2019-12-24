from dexparser import Dexparser

from . import TEST_DEX_FILEPATH


def test_load_dex_from_filedir():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)


def test_load_dex_file_fileobj():
    with open(TEST_DEX_FILEPATH, 'rb') as f:
        dex = Dexparser(fileobj=f.read())
