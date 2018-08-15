Quick Start Guide
=================


Download TaskBuster Django Project Boilerplate
----------------------------------------------

First, you need to download the BoilerPlate from GitHub.


Secret Django Key
-----------------

This boilerplate has the **DJANGO_KEY** setting variable hidden.

You can generate your DJANGO_KEY |django_key|.

.. |django_key| raw:: html

    <a href="http://www.miniwebtool.com/django-secret-key-generator"
    target="_blank">here</a>

Than you need to create secret_keys.py file in main project folder
(taskbuster_project). In the file include:

SECRET_KEY = 'your-secret-key-as-generated-above'

Project Name
------------

This project is named *TaskBuster*, so if you are using this
Boilerplate to create your own project, you'll have to change
the name in a few places:

 - *taskbuster_project* **folder** (your top project container)
 - *taskbuster_project/taskbuster* **folder** (your project name)
 - virtual environment names: **tb_dev** and **tb_test** (name them whatever you want)
 - in virtual environments **postactivate** files (see section below), you have to change **taskbuster.settings.development** for your **projectname.settings.development**. Same works for the testing environment.


Virtual environments and Settings Files
---------------------------------------
LINUX SETUP:

First, you must know your Python 3 path::

    $ which python3

which is something similar to /usr/local/bin/python3.

Next, create a Development virtual environment with Python 3 installed::

    $ mkvirtualenv --python=/usr/local/bin/python3 tb_dev

where you might need to change it with your python path.

Go to the virtual enviornment folder with::

    $ cd $VIRTUAL_ENV/bin

and edit the postactivate file.:

    $ vi postactivate

You must add the lines: ::

    export DJANGO_SETTINGS_MODULE="taskbuster.settings.development"
    export SECRET_KEY="your_secret_django_key"

with your project name and your own secret key.

Next, edit the **predeactivate** file and add the line::

    unset SECRET_KEY

Repeat the last steps for your testing environment::

    $ mkvirtualenv --python=/usr/local/bin/python3 tb_test
    $ cd $VIRTUAL_ENV/bin
    $ vi postactivate

where you have to add the lines::

    export DJANGO_SETTINGS_MODULE="taskbuster.settings.testing"
    export SECRET_KEY="your_secret_django_key"

and in the predeactivate file::

    unset SECRET_KEY

Next, install the packages in each environment::

    $ workon tb_dev
    $ pip install -r requirements/development.txt
    $ workon tb_test
    $ pip install -r requirements/testing.txt

WINDOWS SETUP:

First you need to install virtualenv::

    https://virtualenv.pypa.io/en/stable/userguide/

Than:

1. Create Developmet Virtual Environment::

    $ virtualenv tb_dev

2. Go to the virtual enviornment folder::

    $ cd tb_dev\Scripts

3. At the end of activate.bat file add::

    set "DJANGO_SETTINGS_MODULE=taskbuster.settings.development"

4. At the end of acivate.ps1 file but before # SIG # Begin signature block add::

    $env:DJANGO_SETTINGS_MODULE="taskbuster.settings.development"

5. In deactivate.bat, after set VIRTUAL_ENV=, on next row add::

    set DJANGO_SETTINGS_MODULE=

6. Do the same for tb_test::

    virtualenv tb_test
    cd tb_test\Scripts

Respectively use::

    set "DJANGO_SETTINGS_MODULE=taskbuster.settings.testing"
    $env:DJANGO_SETTINGS_MODULE="taskbuster.settings.testing"
    DJANGO_SETTINGS_MODULE=

for activate.bat, activate.ps1 and deactivate.bat

Internationalization and Localization
-------------------------------------

Settings
********

The default language for this Project is **English**, and we use internatinalization to translate the text into Catalan.

If you want to change the translation language, or include a new one, you just need to modify the **LANGUAGES** variable in the file *settings/base.py*. The language codes that define each language can be found |codes_link|.

.. |codes_link| raw:: html

    <a href="http://msdn.microsoft.com/en-us/library/ms533052(v=vs.85).aspx" target="_blank">here</a>

For example, if you want to use German you should include::

    LANGUAGES = (
        ...
        'de', _("German"),
        ...
    )

You can also specify a dialect, like Luxembourg's German with::

    LANGUAGES = (
        ...
        'de-lu', _("Luxemburg's German"),
        ...
    )

Note: the name inside the translation function _("") is the language name in the default language (English).

More information on the |internationalization_post|.

.. |internationalization_post| raw:: html

    <a href="http://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones" target="_blank">TaskBuster post</a>


Translation
***********

Go to the terminal, inside the taskbuster_project folder and create the files to translate with::

    $ python manage.py makemessages -l ca

To exclude virtual environment files you may use::

    $ python manage.py makemessages -i tb_dev\ -i tb_test\ -l ca

change the language "ca" for your selected language.

Next, go to the locale folder of your language::

    $ cd taskbuster/locale/ca/LC_MESSAGES

where taskbuster is your project folder. You have to edit the file *django.po* and translate the strings. You can find more information about how to translate the strings |translation_strings_post|.

.. |translation_strings_post| raw:: html

    <a href="http://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones#inter-translation" target="_blank">here</a>

Once the translation is done, compile your messages with::

    $ python manage.py compilemessages -l ca



Tests
*****

We need to update the languages in our Tests to make sure the translation works correclty. Open the file *functional_tests/test_all_users.py*:

- in **test_internationalization**, update your languages with the translation of title text, here "Welcome to TaskBuster!"
- in **test_localization**, update your languages.



Useful commands
---------------

A list of all the commands used to run this template

LINUX::

    $ workon tb_dev
    $ workon tb_test


WINDOWS::

    $ tb_dev\Scripts\activate
    $ tb_test\Scripts\activate
    $ deactivate

Languages::

    $ python manage.py makemessages -l ca
    $ python manage.py compilemessages -l ca

Docs management
---------------

After editing .rst files execute::

    $ make html

Postgres DB
-----------

Download from::

    https://www.openscg.com/bigsql/postgresql/installers.jsp/

Install

Configure::

    createdb -U postgres taskbuster_db
    psql -U postgres
    CREATE ROLE <your-user> WITH LOGIN PASSWORD '<your-password>';
    GRANT ALL PRIVILEGES ON DATABASE taskbuster_db TO <your-user>;
    ALTER USER <your-user> CREATEDB;

Install package for Python in tb_dev and tb_test::

    pip install psycopg2

Add to requirements/base.txt file.

Edit secret_keys.py by adding::

    DATABASE_NAME='taskbuster_db'
    DATABASE_USER='<your-user>'
    DATABASE_PASSWORD='<your-password>'

Edit taskbuster\settings\development.py and testing.py by adding::

    import secret_keys

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': secret_keys.DATABASE_NAME,
          'USER': secret_keys.DATABASE_USER,
          'PASSWORD': secret_keys.DATABASE_PASSWORD,
          'HOST': '',
          'PORT': '',
      }
    }

Google authentication
---------------------

Django administration site was not working, may be because of Django 1.8.5 version,
so I migrated to Django 2.1.

On top of this and the instructions on http://www.marinamele.com/user-authentication-with-google-using-django-allauth,
it was nessesary to:

1. to change django.core.urlresolvers with::

    django.urls

2. Change::

    # Required by allauth template tags
    "django.core.context_processors.request",

With::

    'django.template.context_processors.request',

3. Replace::

    $ python manage.py dumpdata --indent 2 --natural -e contenttypes -e auth.Permission > taskbuster/fixtures/allauth_fixture.json

with::

    python manage.py dumpdata --indent 2 --natural-primary -e contenttypes -e auth.Permission > taskbuster/fixtures/allauth_fixture.json

4. Edit the taskbuster/fixtures/allauth_fixture.json file with Sublime text or othe software and save it as UTF-8 encoding
