"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://setuptools.readthedocs.io/en/latest/setuptools.html
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

from os import path

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
def readme():
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
# https://setuptools.readthedocs.io/en/latest/setuptools.html#options
config = {

    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    'name': 'python-boilerplate', # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    'version': '0.1.0', # Required

    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    'url': 'https://github.com/Akman/python-boilerplate', # Optional

    # A string containing the URL from which this version of the distribution
    # can be downloaded. This means that the URL can't be something like
    # .../BeagleVote-latest.tgz, but instead must be .../BeagleVote-0.45.tgz.
    'download_url': 'https://github.com/Akman/python-boilerplate/archive/master.zip', # Optional

    # List additional URLs that are relevant to your project as a dict.
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    'project_urls': { # Optional
        'Bug Reports': 'https://github.com/Akman/python-boilerplate/issues',
        'Source': 'https://github.com/Akman/python-boilerplate',
    },

    # This should be your name or the name of the organization which owns the
    # project.
    'author': 'Alexander Kapitman', # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    'author_email': 'akman.ru@gmail.com', # Optional

    # This should be a maintainer name or the name of the organization which
    # maintain the project.
    # 'maintainer': '', # Optional

    # This should be a valid email address corresponding to the maintainer
    # listed above.
    # 'maintainer_email': '', # Optional

    # Classifiers help users find your project by categorizing it.
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    'classifiers': [ # Optional

        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # Text indicating the license covering the distribution where the license
    # is not a selection from the "License" Trove classifiers.
    # This field may also be used to specify a particular version of a license
    # which is named via the Classifier field, or to indicate a variation or
    # exception to such a license.
    'license': 'MIT', # Optional

    # This includes the license file.
    'license_file': 'LICENSE.txt', # Optional

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    'description': 'Python Boilerplate Project', # Optional

    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    'long_description': readme(), # Optional

    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    'long_description_content_type': 'text/markdown', # Optional

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    # Note that this is a string of words separated by whitespace, not a list.
    'keywords': 'boilerplate setuptools development', # Optional

    # TODO: ?
    # 'platforms': '', # Optional

    # TODO: ?
    # 'provides': '', # Optional

    # TODO: ?
    # 'requires': '', # Optional

    # TODO: ?
    # 'obsoletes': '', # Optional

    # A boolean (True or False) flag specifying whether the project can be
    # safely installed and run from a zip file. If this argument is not
    # supplied, the bdist_egg command will have to analyze all of your
    # project's contents for possible problems each time it builds an egg.
    'zip_safe': False,  # Optional

    # A string or list of strings specifying what other distributions need
    # to be present in order for the setup script to run. setuptools will
    # attempt to obtain these (even going so far as to download them
    # using EasyInstall) before processing the rest of the setup script or
    # commands. This argument is needed if you are using distutils extensions
    # as part of your build process; for example, extensions that
    # process setup() arguments and turn them into EGG-INFO metadata files.
    #
    # Projects listed in setup_requires will NOT be automatically installed
    # on the system where the setup script is being run. They are simply
    # downloaded to the ./.eggs directory if they're not locally available
    # already. If you want them to be installed, as well as being available
    # when the setup script is run, you should add them to install_requires
    # and setup_requires.
    # 'setup_requires': [], # Optional

    # A string or list of strings specifying what other distributions need to be
    # installed when this one is.
    #
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    'install_requires': [ # Optional
        'matplotlib',
        'numpy'
    ],

    # A dictionary mapping names of "extras" (optional features of your project)
    # to strings or lists of strings specifying what other distributions must be
    # installed to support those features. See the section below on Declaring
    # Dependencies for details and examples of the format of this argument.
    #
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    'extras_require': { # Optional
        'dev': ['check-manifest'],
        'test': ['nose'],
    },

    # A string corresponding to a version specifier (as defined in PEP 440) for
    # the Python version, used to specify the Requires-Python
    # defined in PEP 345.
    #
    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers, 'pip install' will check this
    # and refuse to install the project if the version does not match. If you
    # do not support Python 2, you can simplify this to '>=3.5' or similar, see
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4', # Optional

    # A dictionary mapping entry point group names to strings or lists of
    # strings defining the entry points. Entry points are used to support
    # dynamic discovery of services or plugins provided by a project.
    # See Dynamic Discovery of Services and Plugins for details and examples
    # of the format of this argument. In addition, this keyword is used to
    # support Automatic Script Creation.
    #
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    'entry_points': { # Optional
        'console_scripts': [
            'start=akman.sample.command_line:main',
        ],
        # 'gui_scripts': [
        #    akman.sample.gui:main',
        # ]
    },

    # Convert the source code from Python 2 to Python 3 with 2to3 during
    # the build process. See Supporting both Python 2 and Python 3 with
    # Setuptools for more details.
    # 'use_2to3': False, # Optional

    # A list of modules to search for additional fixers to be used during
    # the 2to3 conversion. See Supporting both Python 2 and Python 3 with
    # Setuptools for more details.
    # 'use_2to3_fixers': [], # Optional

    # TODO: ?
    # 'use_2to3_exclude_fixers': [], # Optional

    # List of doctest source files that need to be converted with 2to3.
    # See Supporting both Python 2 and Python 3 with Setuptools
    # for more details.
    # 'convert_2to3_doctests': [], # Optional

    # List of binary scripts that need to be included in distribution.
    # 'scripts': [ # Optional
    #     'bin/sample'
    # ],

    # A list of strings naming resources that should be extracted together,
    # if any of them is needed, or if any C extensions included in the project
    # are imported. This argument is only useful if the project will be
    # installed as a zipfile, and there is a need to have all of the listed
    # resources be extracted to the filesystem as a unit. Resources listed here
    # should be ‘/'-separated paths, relative to the source root, so to list
    # a resource foo.png in package bar.baz, you would include the string
    # bar/baz/foo.png in this argument.
    #
    # If you only need to obtain resources one at a time, or you don't have
    # any C extensions that access other files in the project (such as data
    # files or shared libraries), you probably do NOT need this argument and
    # shouldn't mess with it. For more details on how this argument works, see
    # the section below on Automatic Resource Extraction.
    # 'eager_resources': [], # Optional

    # A list of strings naming URLs to be searched when satisfying dependencies.
    # These links will be used if needed to install packages specified by
    # setup_requires or tests_require. They will also be written into
    # the egg's metadata for use by tools like EasyInstall to use when
    # installing an .egg file.
    # 'dependency_links': [ # Optional
    # ],

    # If your project's tests need one or more additional packages besides
    # those needed to install it, you can use this option to specify them.
    # It should be a string or list of strings specifying what other
    # distributions need to be present for the package's tests to run.
    # When you run the test command, setuptools will attempt to obtain
    # these (even going so far as to download them using EasyInstall). Note
    # that these required projects will not be installed on the system where
    # the tests are run, but only downloaded to the project's setup directory
    # if they're not already installed locally.
    # 'tests_require': [ # Optional
    #     'nose',
    # ],

    # If set to True, this tells setuptools to automatically include any data
    # files it finds inside your package directories that are specified by
    # your MANIFEST.in file. For more information, see the section below on
    # Including Data Files.
    'include_package_data': True, # Optional

    # You can just specify package directories manually here if your project is
    # simple.
    #
    # You can use find_packages(), then see:
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#id10
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    'packages': find_packages(exclude=['docs']), # Required

    # TODO: ?
    # 'package_dir': {}, # Optional

    # A dictionary mapping package names to lists of glob patterns.
    # You do not need to use this option if you are
    # using include_package_data, unless you need to add e.g. files that are
    # generated by your setup script and build process. And are therefore
    # not in source control or are files that you don't want to include
    # in your source distribution.
    #
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    'package_data': { # Optional
        'akman.sample': ['sample.dat'],
    },

    # A dictionary mapping package names to lists of glob patterns that
    # should be excluded from your package directories. You can use this
    # to trim back any excess files included by include_package_data.
    # For a complete description and examples, see the section below
    # on Including Data Files.
    # 'exclude_package_data': False, # Optional

    # A list of strings naming the project's "namespace packages". A namespace
    # package is a package that may be split across multiple project
    # distributions. For example, Zope 3's zope package is a namespace package,
    # because subpackages like zope.interface and zope.publisher may be
    # distributed separately. The egg runtime system can automatically merge
    # such subpackages into a single parent package at runtime, as long as you
    # declare them in each project that contains any subpackages of
    # the namespace package, and as long as the namespace package's __init__.py
    # does not contain any code other than a namespace declaration.
    # See the section below on Namespace Packages for more information.
    'namespace_packages': [ # Optional
        'akman'
    ],

    # TODO: ?
    # 'py_modules': '', # Optional

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # 'data_files': [
    #     ('my_data', [
    #         'data/data_file'
    #     ])
    # ], # Optional

    # If you would like to use a different way of finding tests to run than
    # what setuptools normally uses, you can specify a module name and class
    # name in this argument. The named class must be instantiable with no
    # arguments, and its instances must support the loadTestsFromNames() method
    # as defined in the Python unittest module's TestLoader class. Setuptools
    # will pass only one test "name" in the names argument: the value supplied
    # for the test_suite argument. The loader you specify may interpret this
    # string in any way it likes, as there are no restrictions on what may be
    # contained in a test_suite string.
    #
    # The module name and class name must be separated by a :. The default value
    # of this argument is "setuptools.command.test:ScanningLoader". If you want
    # to use the default unittest behavior, you can specify
    # "unittest:TestLoader" as your test_loader argument instead. This will
    # prevent automatic scanning of submodules and subpackages.
    #
    # The module and class you specify here may be contained in another package,
    # as long as you use the tests_require option to ensure that the package
    # containing the loader class is available when the test command is run.
    # 'test_loader': '', # Optional

    # A string naming a unittest.TestCase subclass (or a package or module
    # containing one or more of them, or a method of such a subclass), or
    # naming a function that can be called with no arguments and returns
    # a unittest.TestSuite. If the named suite is a module, and the module
    # has an additional_tests() function, it is called and the results are
    # added to the tests to be run. If the named suite is a package, any
    # submodules and subpackages are recursively added to the overall
    # test suite.
    #
    # Specifying this argument enables use of the test command to run
    # the specified test suite, e.g. via setup.py test. See the section on
    # the test command below for more details.
    # 'test_suite': 'nose.collector', # Optional
}

setup(**config)
