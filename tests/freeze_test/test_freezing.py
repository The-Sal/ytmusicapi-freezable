import os
import random
import shutil
import subprocess
import unittest



def _create_containers_and_assign_attributes(cls):
    tempDir = random.randint(0, 1000).__str__()
    cls.tempDir = tempDir
    cls.cwd = os.getcwd()
    os.mkdir(tempDir)
    os.chdir(tempDir)


def _remove_containers(cls):
    os.chdir(cls.cwd)
    shutil.rmtree(cls.tempDir)



PYINSTALLER_INSTALL_CMD = [
    'pyinstaller', '--onefile', '--clean', __file__.replace('test_freezing.py', 'test_script.py')
]


def _regular_import_and_check():
    from test_script import none
    none()



class TestTestScript(unittest.TestCase):
   def test_test_script(self):
       _regular_import_and_check()


class TestFreezingWithPyInstaller(unittest.TestCase):
    """Test that ytmusicapi can be frozen with PyInstaller."""

    @classmethod
    def setUpClass(cls):
        _create_containers_and_assign_attributes(cls)
        subprocess.check_call(PYINSTALLER_INSTALL_CMD)
        cls.executable = os.path.join(os.getcwd(), 'dist/test_script')


    @classmethod
    def tearDownClass(cls):
        _remove_containers(cls)


    def test_pyinstaller(self):
        """Test that ytmusicapi can be frozen with PyInstaller."""
        subprocess.check_call([self.executable])


class TestFreezingWithNuitka(unittest.TestCase):
    """Test that ytmusicapi can be frozen with Nuitka."""

    @classmethod
    def setUpClass(cls):
        _create_containers_and_assign_attributes(cls)
        subprocess.check_call([
            'python3', '-m', 'nuitka', '--standalone',
            '--remove-output',  '--onefile', __file__.replace('test_freezing.py', 'test_script.py')
        ])
        cls.executable = os.path.join(os.getcwd(), 'test_script.bin')


    @classmethod
    def tearDownClass(cls):
        _remove_containers(cls)


    def test_nuitka(self):
        """Test that ytmusicapi can be frozen with Nuitka."""
        subprocess.check_call([self.executable])



if __name__ == '__main__':
    unittest.main()