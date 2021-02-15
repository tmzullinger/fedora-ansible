#
# This is the config file for FAS Changes as intended to be used in OpenShift
#

ACCESS_KEY = "only-for-fas2ipa"

DB_NAME = "fas2"
DB_HOST = "db-fas{{ env_suffix }}"
DB_USER = "fasreadonly"
DB_PASSWORD = "{{ fas_db_readonly_password }}"