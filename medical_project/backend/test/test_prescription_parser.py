from backend.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_virat():
    document_text = """
        Dr John >mith, M.D

    2 Non-Important street,
    New York, Phone (900)-323- ~2222

    Name:  Virat Kohli Date: 2/05/2022




    Address: 2 cricket blvd, New Delhi

    | Omeprazole 40 mg

    Directions: Use two tablets daily for three months

    Refill: 3 times
        """

    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_empty():
    return PrescriptionParser('')

def test_get_name(doc_1_virat,doc_2_empty):
    assert doc_1_virat.get_field('patient_name') == 'Virat Kohli'
    assert doc_2_empty.get_field('patient_name') == None

def test_get_address(doc_1_virat):
    assert doc_1_virat.get_field('patient_address') == '2 cricket blvd, New Delhi'

