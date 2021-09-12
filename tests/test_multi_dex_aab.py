from dexparser import AABParser

from . import TEST_MULTI_AAB_FILEPATH


def test_load_aab_from_filedir():
    aab = AABParser(filedir=TEST_MULTI_AAB_FILEPATH)
    assert aab.is_multidex is True


def test_load_aab_file_fileobj():
    with open(TEST_MULTI_AAB_FILEPATH, 'rb') as f:
        aab = AABParser(fileobj=f.read())
        assert aab.is_multidex is True
