import os

from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_handlers',
    'pyramid_debugtoolbar',
    'waitress',
    ]

setup(name='mugglecorner',
      version='0.0.1',
      description='Get in the corner!',
      long_description='',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Lukas Kubis',
      author_email='contact@lukaskubis.com',
      url='mugglecorner.com',
      keywords='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = app:main
      """,
      )
