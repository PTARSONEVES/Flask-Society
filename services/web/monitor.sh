#!/bin/bash
UP=$(pgrep manage | wc -l );
echo $UP;
if [ $UP -ne 0 ];
then
        echo  " MySQL está fora do ar. " ;
        service sudo mysql start

else
        echo  "Está tudo bem.";
        echo $UP;
fi
exec "$@"