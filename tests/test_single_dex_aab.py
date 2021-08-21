from dexparser import AABParser

from . import TEST_SINGLE_AAB_FILEPATH


def test_load_aab_from_filedir():
    aab = AABParser(filedir=TEST_SINGLE_AAB_FILEPATH)
    assert aab.is_multidex == False


def test_load_aab_file_fileobj():
    with open(TEST_SINGLE_AAB_FILEPATH, 'rb') as f:
        aab = AABParser(fileobj=f.read())
        assert aab.is_multidex == False
