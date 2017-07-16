from setuptools import setup, find_packages
import codecs, os.path

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='tallinja-balance',
      version='1.0.0',
      description='Balance check for Tallinja (Malta) public transport cards',
      long_description=long_description,
      url='https://github.com/dottedmag/tallinja-balance',
      author='Mikhail Gusarov',
      author_email='dottedmag@dottedmag.net',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Utilities',
      ],
      keywords='malta tallinja transport',
      packages=find_packages(),
      install_requires=['requests'],
      entry_points={
          'console_scripts': ['tallinja-balance=tallinja.balance_cli:main']
      })
