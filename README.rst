Important
=========

This app has been discontinued and is no longer maintained.

cmsplugin-blog Language Publish
===============================

An extension for `cmsplugin-blog <https://github.com/fivethreeo/cmsplugin-blog/>`_
which allows to publish only certain languages of a blog entry.


Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django
    pip install django-cms
    pip install cmsplugin-blog
    pip install simple-translation

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-blog-language-publish  (not available by now)

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-blog-language-publish.git#egg=cmsplugin_blog_language_publish

Add ``cmsplugin_blog_language_publish`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'cmsplugin_blog_language_publish',
    )


TODO: Add additional installation steps.


Usage
-----

TODO: Describe usage


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 cmsplugin-blog-language-publish
    $ pip install -r requirements.txt
    $ ./logger/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
