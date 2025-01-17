''' This converts each folder in packages/ into a zip, saving the zips into zips/. This way it's easy to edit them.'''
import os
import os.path
from zipfile import ZipFile, ZIP_LZMA

# Skip these files, if they exist in the source folders.
# Users won't need them.
SKIPPED_EXTENSIONS = ('vmx', 'log', 'bsp', 'prt', 'lin')

def do_folder(path):
    for package in os.listdir(path):
        package_path = os.path.join(path, package)
        if os.path.isdir(package_path):
            if 'info.txt' in os.listdir(package_path):
                print('| ' + package + '.zip')
                pack_zip_path = os.path.join(zip_path, package)
                zip = ZipFile(pack_zip_path + '.zip', 'w', compression=ZIP_LZMA)
                for base, dirs, files in os.walk(package_path):
                    for file in files:
                        full_path = os.path.normpath(os.path.join(base, file))
                        rel_path = os.path.relpath(full_path, package_path)
                        if file[-3:] in SKIPPED_EXTENSIONS:
                            print('X   \\' + rel_path)
                            continue
                        print('    \\' +rel_path)

                        zip.write(full_path, rel_path)
                print('')
            else:
                do_folder(package_path)

zip_path = os.path.join(os.getcwd(), 'zips/')
if os.path.isdir(zip_path):
    for file in os.listdir(zip_path):
        print('Deleting', file)
        os.remove(os.path.join(zip_path, file))
else:
    os.makedirs(zip_path)

path = os.path.join(os.getcwd(), 'packages\\')
do_folder(path)
