import os


def project_dir(*paths):
    base = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(base, *paths)
