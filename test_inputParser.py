import pytest
import input_data_parser

def test_sample() -> None:
    pass

def test_validate_json_with_valide_file() -> None:
    validJson = input_data_parser.validate_json('./unitTests/sample_patient1.json')
    assert validJson == True

def test_validate_json_with_invalide_file() -> None:
    validJson = input_data_parser.validate_json('./unitTests/sample_fail_file.json')
    assert validJson == False

def test_validate_json_with_invalide_file_two() -> None:
    validJson = input_data_parser.validate_json('./unitTests/sample.txt')
    assert validJson == False