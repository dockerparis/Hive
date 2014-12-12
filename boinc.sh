#!/bin/bash

if [ $# -eq 0 ]
then
    echo "No url supplied"
    exit 0
fi

read -p "Name: " name
read -p "Mail: " mail
read -s -p "Enter password: " password

result="`boinccmd --create_account $1 $mail $password $name`"
key="`echo $result| grep 'account key' | rev | cut -d':' -f1 | rev`"
echo "url: " $1
echo "key: " $key
boinc --attach_project $1 $key

