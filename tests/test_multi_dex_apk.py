from dexparser import APKParser

from . import TEST_MULTI_APK_FILEPATH


def test_load_apk_from_filedir():
    dex = APKParser(filedir=TEST_MULTI_APK_FILEPATH)
    assert dex.is_multidex == True


def test_load_apk_file_fileobj():
    with open(TEST_MULTI_APK_FILEPATH, 'rb') as f:
        dex = APKParser(fileobj=f.read())
        assert dex.is_multidex == True
