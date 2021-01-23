#!/bin/bash
source /home/www/mobile-repair-cloud/env/bin/activate
exec gunicorn -c "/home/www/mobile-repair-cloud/gunicorn_config.py" project.wsgi
