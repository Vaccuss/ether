import os
import shutil


def add_libraries(src_path, destination_path):
    # files = glob.glob(os.path.join(src_path, '*'))
    # destination_path = os.path.join(destination_path, "lib")
    files = next(os.walk(src_path))[1]
    for file in files:
        from_path = os.path.join(src_path, file)
        to_path = os.path.join(destination_path, file)
        shutil.copytree(from_path, to_path)
