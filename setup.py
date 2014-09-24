from distutils.core import setup


setup(
    name='jwt.py',
    version='0.1.0',
    author='iPlant Collaborative',
    author_email='atmodevs@gmail.com',
    description='jwt.py',
    url='https://github.com/iPlantCollaborativeOpenSource/jwt.py',
    py_modules=['jwt'],
    install_requires=[
        'pycrypto >= 2.6'
    ]
)
