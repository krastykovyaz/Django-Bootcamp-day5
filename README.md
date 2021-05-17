pg_ctl -D /usr/local/var/postgres start
export PGDATA=/Users/bpole/.brew/var/postgres
pg_ctl start / stop - запуск сервера
psql -d postgres - перейти в postgres
psql -U name_user -d name_db - перейти в db

CREATE DATABASE name_db; - создать базу
CREATE USER name_user WITH PASSWORD 'secret';
ALTER DATABASE name_db OWNER TO name_user;
