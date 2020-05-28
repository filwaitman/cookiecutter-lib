{%- if cookiecutter.use_django.lower() == 'y' -%}
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

if not settings.configured:
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',

            '{{cookiecutter.package_name}}',
            'tests',
        ),
    )

    django.setup()
    test_runner = DiscoverRunner(verbosity=1)

    failures = test_runner.run_tests(['tests'])
    if failures:
        sys.exit(failures)
{% else -%}
import nose

nose.main()
{% endif -%}