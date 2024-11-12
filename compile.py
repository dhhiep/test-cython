from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import os


def find_pyx(path, exclude_dir_names=None):
    if exclude_dir_names is None:
        exclude_dir_names = []
    extensions = []
    for root, dirs, files in os.walk(path):
        # Exclude directories by name
        dirs[:] = [d for d in dirs if d not in exclude_dir_names]
        for file in files:
            if file.endswith(".py") and file != "setup.py":
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, path)
                module = os.path.splitext(rel_path)[0].replace(os.sep, ".")
                extensions.append(Extension(module, [full_path]))
    return extensions


exclude_dir_names = ["venv", "__pycache__", ".git", "build"]

extensions = [
    Extension(module, [source], extra_compile_args=["-Wno-unreachable-code"])
    for module, source in [
        (ext.name, ext.sources[0])
        for ext in find_pyx(".", exclude_dir_names=exclude_dir_names)
    ]
]

setup(
    name="your_project",
    packages=find_packages(),
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3"},
        build_dir="build",
        annotate=False,
    ),
    zip_safe=False,
)
