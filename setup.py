from setuptools import setup
APP = ['login.py']
DATA_FILES = []
OPTIONS = {
	'argv_emulation': True, 
	'site_packages': True,
	'iconfile': 'maks-login-icon.icns',
	'packages': ['requests', 'dotenv', 'mongodb_tools', 'PIL', 'mongo_auth', 'pymongo', 'dns'],
	'plist': {
		'CFBundleName': 'Login to Maks',
	}
}
setup(
	app=APP,
	data_files=DATA_FILES,
	options={'py2app': OPTIONS},
	setup_requires=['py2app'],
)