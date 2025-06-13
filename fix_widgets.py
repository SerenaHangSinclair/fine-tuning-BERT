# pip install nbformat
import nbformat

# Load the notebook
notebook_path = "Serena_Lab2_CS8321_(I added_BERT).ipynb"
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Remove broken metadata.widgets if it exists
if "widgets" in nb.metadata:
    print("Removing metadata.widgets...")
    del nb.metadata["widgets"]

# Save the cleaned notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print(" metadata.widgets removed, outputs kept.")