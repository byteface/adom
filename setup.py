from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

from dom import __version__ as version

setup(
  name='adom',
  version=version,
  author="@byteface",
  author_email="byteface@gmail.com",
  license="MIT",
  url='https://github.com/byteface/adom',
  download_url='https://github.com/byteface/adom/archive/' + version + ' .tar.gz',
  description='A domonic-like wrapper around selectolax',
  long_description=long_description,
  long_description_content_type="text/markdown",
  keywords=['html', 'generate', 'templating', 'dom', 'vdom', 'web', 'template', 'DOM', 'GUI', 'website', 'html5',],
  python_requires='>=3.6',
  classifiers=[
      "Programming Language :: Python :: 3",
      "Programming Language :: JavaScript",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Intended Audience :: Developers",
      "Intended Audience :: Other Audience",
      "License :: OSI Approved :: MIT License",
      "Natural Language :: English",
      "Operating System :: OS Independent",
      "Topic :: Internet",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Multimedia :: Graphics :: Presentation",
      "Topic :: Software Development",
      "Topic :: Software Development :: Code Generators",
      "Topic :: Terminals",
      "Topic :: Utilities",
      'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Text Processing :: Markup :: HTML',
  ],
  install_requires=[
      'httpx==0.22.0', 'selectolax==0.3.6'
  ],
  packages=find_packages(),
  include_package_data=True,
  entry_points={
      'console_scripts': [
          'adom = dom.__main__:run',
      ],
  },
)
