command = '/home/www/mobile-repair-cloud/env/bin/gunicorn'
pythonpath = '/home/www/mobile-repair-cloud/project/'
bind = 'unix:/home/www/mobile-repair-cloud/cloud.sock'
workers = 5
user = 'www'
uid = 'www-data'
gid = 'www-data'
# group = 'www-data'
# error-logfile = '-'
limit_request_fields = 32000
limit_request_field_size = 0
chmod_socket = 777
raw_env = 'DJANGO_SETTINGS_MODULE=project.settings-prod'
