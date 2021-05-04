from setuptools import setup
import sys
sys.setrecursionlimit(20000)
APP = ['maks_app.py']
DATA_FILES = ['violator.wav', 'non_violator.wav', 'facemask-model']
OPTIONS = {
	'argv_emulation': True, 
	'site_packages': True,
	'iconfile': 'maks-icon.icns',
	'packages': ['cv2', 'keras', 'numpy', 'PIL', 'tensorflow', 'mongo_upload'],
	'plist': {
		'CFBundleName': 'Maks',
	}
}
setup(
	app=APP,
	data_files=DATA_FILES,
	options={'py2app': OPTIONS},
	setup_requires=['py2app'],
)