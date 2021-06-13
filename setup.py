from distutils.core import setup
setup(
  name = 'flaskstart',
  packages = ['flaskstart'],
  version = '0.1',
  license='apache-2.0',
  description = 'A Flask project start-up CLI to create a modular ready projects.',
  author = 'Felipe Bastos Nunes',
  author_email = 'felipe.bastosn@gmail.com',
  url = 'https://github.com/felipebasnun/flaskstart',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['flask', 'cli', 'project'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'click',
          'venv',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache license 2.0',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)