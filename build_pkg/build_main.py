import os
import shutil
import click
from .Libraries import add_libraries


@click.command()
@click.argument('target', default='', required=False)
@click.option('--all', '-a', is_flag=True)
def build(target, all):
    """Automatically creates a zip file for each *.py file in src.
    Directories in source are considered shared libraries and will be included in each endpoint"""

    if target == '':
        if all:
            build_all()
        else:
            print("please specify target or use -all(-a) \nsyntax: build <target> | (-all -a)")
    elif target != '' and all:
        print("ignoring -all flag build specific")
        build_single(target)
    else:
        build_single(target)


def build_all():
    print("Building...")
    endpoints = get_code()
    path = ".tmp"
    dr = os.getcwd()
    dr = os.path.join(dr, "src")
    if os.path.exists(path):
        shutil.rmtree(".tmp")

    for endpoint in endpoints:
        if endpoint != "__init__.py":
            add_libraries(dr, path)
            if not os.path.exists(path):
                os.makedirs(path)
            shutil.copy2(os.path.join(dr, endpoint), path)
            archive_file(endpoint, path)
            shutil.rmtree(".tmp")
    print("...done")


def build_single(target):
    print("Building...")
    path = ".tmp"
    dr = os.getcwd()
    dr = os.path.join(dr, "src")
    if os.path.exists(path):
        shutil.rmtree(".tmp")

    add_libraries(dr, path)

    if not os.path.exists(path):
        os.makedirs(path)

    if ".py" not in target:
        target += ".py"

    shutil.copy2(os.path.join(dr, target), path)
    archive_file(target, path)
    shutil.rmtree(".tmp")
    print("...done")


def get_code():
    dr = os.getcwd()
    dr += "/src"
    items = os.listdir(dr)
    endpoints = []
    for item in items:
        if ".py" in item:
            endpoints.append(item)

    return endpoints


def archive_file(dir_name, folder_path):
    name = dir_name[:len(dir_name) - 3]
    output_filename = '.build/' + name
    shutil.make_archive(output_filename, 'zip', folder_path)
