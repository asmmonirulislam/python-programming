Module: one .py file.

Package: a folder of modules. Modern packages often still include an __init__.py file.

Imports: from app.services.links import create_link means: in the folder app/services/ , open
the file links.py and take create_link .

Run modules from the project root with python -m app.main , so imports resolve the same way every
time.

The if __name__ == "__main__": guard runs code only when the file is executed directly, not when it
is imported.