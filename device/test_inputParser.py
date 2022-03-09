import pytest
import input_data_parser

# def test_validate_json_with_valide_file() -> None:
#     validJson = input_data_parser.write_to_database('./data/sample_patient1.json')
#     assert validJson[0] == True

def test_validate_json_with_invalide_file() -> None:
    validJson = input_data_parser.write_to_database('./data/sample_patient1.json')
    assert validJson[0] == False

def test_validate_json_with_invalide_file_two() -> None:
    validJson = input_data_parser.write_to_database('./data/sample.txt')
    assert validJson[0] == False