import io
import base64
import os.path
import shutil
import tempfile
import zipfile
import sys
from ytmusicapi.freeze_help.locales import data

_tempdir = tempfile.TemporaryDirectory()


def freezer_log_print(*args, **kwargs):
    if '--freeze-log' in sys.argv:
        print(*args, **kwargs)


def decompress():
    decoded = base64.b64decode(data)
    with open('locales.zip', 'wb') as f:
        f.write(decoded)

    with zipfile.ZipFile('locales.zip', 'r') as zip_ref:
        zip_ref.extractall('.')


class BinaryExpander:
    def __init__(self):
        decoded = base64.b64decode(data)
        zip_file = zipfile.ZipFile(io.BytesIO(decoded))
        zip_file.extractall('.')
        shutil.move(zip_file.namelist()[0], _tempdir.name)

        self.path_of_locals = os.path.join(_tempdir.name, zip_file.namelist()[0])

        zip_file.close()



class LocalesHelper(BinaryExpander):
    def __init__(self):
        super().__init__()

