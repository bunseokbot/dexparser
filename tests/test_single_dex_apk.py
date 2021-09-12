from dexparser import APKParser

from . import TEST_SINGLE_APK_FILEPATH


def test_load_apk_from_filedir():
    apk = APKParser(filedir=TEST_SINGLE_APK_FILEPATH)
    assert apk.is_multidex is False


def test_load_apk_file_fileobj():
    with open(TEST_SINGLE_APK_FILEPATH, 'rb') as f:
        apk = APKParser(fileobj=f.read())
        assert apk.is_multidex is False
