# Memperbaiki metadata widgets
import json

file_path = "computer_vision_torch.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nbook = json.load(f)

# Memperbaiki metadata widgets tanpa hapus output
if "widgets" in nbook["metadata"]:
    if "application/vnd.jupyter.widget-state+json" in nbook["metadata"]["widgets"]:
        # Menambahkan kunci 'state' jika hilang
        if "state" not in nbook["metadata"]["widgets"]["application/vnd.jupyter.widget-state+json"]:
            nbook["metadata"]["widgets"]["application/vnd.jupyter.widget-state+json"]["state"] = {}
            print("Kunci 'state' berhasil ditambahkan!")

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nbook, f, indent=1)