from distutils.core import setup
setup(
    name='jwt.py',
    version='0.1',
    author='David Knapp',
    author_email='dknapp@iplantcollaborative.org',
    py_modules=['jwt'],
    install_requires=[
        'pycrypto >= 2.6.1, < 2.7'
    ]
)
