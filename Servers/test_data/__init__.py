import json
from pathlib import Path

data_path = Path(__file__).parent

JSON_1K = json.loads((data_path / "1K.json").read_text())
JSON_10K = json.loads((data_path / "10K.json").read_text())
JSON_100K = json.loads((data_path / "100K.json").read_text())
JSON_500K = json.loads((data_path / "500K.json").read_text())
JSON_1M = json.loads((data_path / "1M.json").read_text())
JSON_5M = json.loads((data_path / "5M.json").read_text())
