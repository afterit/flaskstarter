from distutils.core import setup
setup(
  name = 'flaskstarter',
  packages = ['flaskstarter'],
  version = '0.1',
  license='apache-2.0',
  description = 'A Flask project start-up CLI to create a modular ready projects.',
  author = 'Felipe Bastos Nunes',
  author_email = 'felipe.bastosn@gmail.com',
  url = 'https://github.com/felipebastos/flaskstart',
  download_url = 'https://github.com/felipebastos/flaskstart/archive/refs/tags/v0.1.tar.gz',
  keywords = ['flask', 'cli', 'project'],
  install_requires=[
          'click',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      #"3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)