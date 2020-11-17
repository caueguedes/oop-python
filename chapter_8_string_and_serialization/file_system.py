import pathlib
from zipfile import ZipFile

def count_sloc(dir_path):
    sloc = 0
    for path in dir_path.iterdir():
        if path.name.startswith("."):
            continue
        if path.is_dir():
            sloc += count_sloc(path)
            continue
        if path.suffix != ".py":
            continue
        with path.open() as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    sloc += 1
    return sloc


root_path = pathlib.Path(".")
print(f"{count_sloc(root_path)} lines of python code")

# Some pathlib functions
pathlib.Path().absolute()
pathlib.Path().parent()  # returns path to parent folder
pathlib.Path().exists()
pathlib.Path().mkdir()


ZipFile(pathlib.Path('nothing.zip'), 'w').writestr('filename', 'contents')
