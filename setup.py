from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name='flaskstarter',
  version='0.2.1',
  license='apache-2.0',
  description='A Flask project start-up CLI to create a modular ready projects.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author='Felipe Bastos Nunes',
  author_email='felipe.bastosn@gmail.com',
  url='https://github.com/felipebastos/flaskstart',
  download_url='https://github.com/felipebastos/flaskstart/archive/refs/tags/v0.2.1.tar.gz',
  keywords=['flask', 'cli', 'project'],
  install_requires=['click','Jinja2', 'MarkupSafe'],
  entry_points={
        'console_scripts': [
            'flaskstarter = flaskstarter.flaskstart_cli:flaskstarter',
        ],
    },
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
  package_dir={"": "src"},
  packages=find_packages(where="src"),
  package_data={
        "flaskstarter": ["templates/*t"],
  }
)
