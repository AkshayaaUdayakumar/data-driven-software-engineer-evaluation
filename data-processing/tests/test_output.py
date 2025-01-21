import os
import json
from src.output import save_to_json

def test_save_to_json(tmp_path):
    data = {"emails": ["test@example.com"], "phone_numbers": ["123-456-7890"], "dates": ["01/01/2023"]}
    output_file = tmp_path / "output.json"
    save_to_json(data, output_file)

    assert os.path.exists(output_file)
    with open(output_file, "r") as f:
        saved_data = json.load(f)
        assert saved_data == data
