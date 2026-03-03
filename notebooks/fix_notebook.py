import json

with open('notebook1.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if 'outputs' in cell: 
        cell['outputs'] = []
    if 'execution_count' in cell: 
        cell['execution_count'] = None
    if cell['cell_type'] == 'code':
        source = cell['source']
        for i, line in enumerate(source):
            if "layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3))" in line:
                source[i] = "    layers.Input(shape=(128,128,3)),\n"
                source.insert(i+1, "    layers.Conv2D(32, (3,3), activation='relu'),\n")
                break
        
        has_warnings = any('import warnings' in line for line in source)
        if not has_warnings and len(source) > 0:
            source.insert(0, 'import warnings\n')
            source.insert(1, 'warnings.filterwarnings("ignore")\n')

with open('notebook1.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
