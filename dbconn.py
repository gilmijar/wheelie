"""
create user wheelie@localhost identified by 'passw0rd;
grant create on wheelie_test.* to wheelie@localhost;  -- this allows to create the chema itself
"""

from os import environ
from tomllib import load as toml_load
import pymysql

db_conf = toml_load(open("config.toml", "rb"))['database']
env_var_name = db_conf['password_env_var']
if not environ.get(env_var_name):
    raise RuntimeError(f"\nEnvironment variable {env_var_name} is not set.\n"
                       "Please set it to the database password.\n"
                       f"linux command for that is `export {env_var_name}=your_passwOrd`")


def connection(db_name:str = db_conf['db_name'])->pymysql.Connection:
    db = pymysql.connect(
        host=db_conf['host'],
        port=db_conf['port'],
        user=db_conf['user'],
        password=environ[env_var_name],
        database=db_name,
        autocommit=False
    )
    return db