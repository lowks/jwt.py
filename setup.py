from distutils.core import setup


setup(
    name='jwt.py',
    version='0.1.0',
    author='iPlant Collaborative',
    author_email='atmodevs@gmail.com',
    py_modules=['jwt'],
    install_requires=[
        'pycrypto >= 2.6'
    ]
)
