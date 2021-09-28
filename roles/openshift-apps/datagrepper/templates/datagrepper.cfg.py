#
# This is the config file for Datagrepper as intended to be used in OpenShift
#

APP_PATH = "https://apps{{ env_suffix }}.fedoraproject.org/datagrepper2"
DEFAULT_QUERY_DELTA = 3600
DATANOMMER_SQLALCHEMY_URL = "postgresql://{{ datanommerDBUser }}:{{ (env == 'production')|ternary(datanommerDBPassword, datanommer_stg_db_password) }}@db-datanommer01{{ env_suffix }}.iad2.fedoraproject.org/datanommer2"

# Only allow ajax/websockets connections back to our domains.
# https://github.com/fedora-infra/datagrepper/pull/192
CONTENT_SECURITY_POLICY = "connect-src https://*.fedoraproject.org wss://*.fedoraproject.org"
