#!/bin/sh

if [ "$DATABASE"="mysql" ]
then
#    echo $DATABASE
    echo "Waiting for mysql..."
#    while ! nc -z $SQL_HOST $SQL_PORT; 
#    while ! mysql --host='localhost' --user='root' --password='strolandia';
#    while ! (mysqladmin ping);
#    do
#        sleep 0.1
#        sleep 3
#        echo "aguardando o mysql..."
#    done
    echo "Mysql started"
fi
exec "$@"
