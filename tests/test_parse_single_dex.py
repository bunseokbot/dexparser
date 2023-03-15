from dexparser import Dexparser, DEXParser

from . import TEST_DEX_FILEPATH


def test_parse_header():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.header.get('checksum') == 2459812747

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    assert dex.header.get('checksum') == 2459812747


def test_parse_strings():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_strings()

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_strings()


def test_parse_typeids():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_typeids()

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_typeids()


def test_parse_methods():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_methods()

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_methods()


def test_parse_protoids():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_protoids()

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_protoids()


def test_parse_fieldids():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_fieldids()

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_fieldids()


def test_parse_classdef_data():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_classdef_data()

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    assert dex.get_classdef_data()


def test_parse_class_data():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    offset = dex.get_classdef_data()[0]['class_data_off']
    assert dex.get_class_data(offset=offset)

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    offset = dex.get_classdef_data()[0]['class_data_off']
    assert dex.get_class_data(offset=offset)


def test_parse_annotations():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    offset = dex.get_classdef_data()[0]['annotation_off']
    assert dex.get_annotations(offset=offset)

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    offset = dex.get_classdef_data()[0]['annotation_off']
    assert dex.get_annotations(offset=offset)


def test_parse_class_data():
    dex = Dexparser(filedir=TEST_DEX_FILEPATH)
    offset = dex.get_classdef_data()[710]['static_values_off']

    for i, class_def in enumerate(dex.get_classdef_data()):
        offset = class_def['static_values_off']
        if offset == 0:
            continue

        values = dex.get_static_values(offset=offset)

    dex = DEXParser(filedir=TEST_DEX_FILEPATH)
    offset = dex.get_classdef_data()[0]['static_values_off']
    assert dex.get_static_values(offset=offset)
