from dexparser import Dexparser, DEXParser

from . import TEST_DEX_FILEPATH


def test_load_dex_from_filedir():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)


def test_load_dex_from_filedir_with_new_dexparser():
    dex = DEXParser(filedir=TEST_DEX_FILEPATH)


def test_load_dex_file_fileobj():
    with open(TEST_DEX_FILEPATH, 'rb') as f:
        dex = Dexparser(fileobj=f.read())


def test_load_dex_file_fileobj_with_new_dexparser():
    with open(TEST_DEX_FILEPATH, 'rb') as f:
        dex = DEXParser(fileobj=f.read())
