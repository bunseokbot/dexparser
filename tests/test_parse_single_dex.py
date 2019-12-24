from dexparser import Dexparser

from . import TEST_DEX_FILEPATH


def test_parse_header():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.header.get('checksum') == 2459812747


def test_parse_strings():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_strings()


def test_parse_typeids():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_typeids()


def test_parse_methods():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_methods()


def test_parse_protoids():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_protoids()


def test_parse_fieldids():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_fieldids()


def test_parse_classdef_data():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_classdef_data()


def test_parse_class_data():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    offset = dex.get_classdef_data()[0]['class_data_off']
    assert dex.get_class_data(offset=offset)


def test_parse_annotations():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    offset = dex.get_classdef_data()[0]['annotation_off']
    assert dex.get_annotations(offset=offset)
