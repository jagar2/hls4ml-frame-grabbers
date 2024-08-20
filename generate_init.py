import os
import sys

def generate_init_py(package_dir):
    """
    Auto-generates an __init__.py file that imports all modules in the package
    and adds them to the __all__ list.
    """
    modules = []
    with open(os.path.join(package_dir, '__init__.py'), 'w') as init_file:
        init_file.write('# Auto-generated __init__.py\n\n')
        for filename in os.listdir(package_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                modules.append(module_name)
                init_file.write(f'from . import {module_name}\n')
        init_file.write(f'\n__all__ = {modules}\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_init.py <package_directory>")
        sys.exit(1)

    package_dir = sys.argv[1]
    if not os.path.isdir(package_dir):
        print(f"Error: {package_dir} is not a valid directory")
        sys.exit(1)

    generate_init_py(package_dir)
    print(f"__init__.py generated in {package_dir}")
