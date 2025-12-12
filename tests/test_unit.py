from app.main import replace_text

dummy_map = {
    "a": "4",
    "s": "5",
    "i": "1"
}

def test_char_replacement():
    assert replace_text("nasi", dummy_map) == "n451"

def test_mixed_case():
    assert replace_text("Aku", dummy_map) == "4ku"

def test_no_replacement():
    assert replace_text("bmw", dummy_map) == "bmw"