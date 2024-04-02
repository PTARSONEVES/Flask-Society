#!/bin/bash
TT=$(pgrep mysql);
if [ $TT==0 ];
then
    echo "OK!";
    echo $teste;
else
    echo "Não!!!";
fi