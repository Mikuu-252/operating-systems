#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Musisz podac 3 parametry."
    echo "Przyklad: $0 [plik1] [plik2] [plik3]"
    exit 1
fi

if [ ! -f "$1" ] || [ ! -r "$1" ]; then
    echo "Nie masz praw do odczytu pliku ($1) lub on nie istnieje"
    exit 1
fi

if { [ ! -f "$2" ] || [ ! -w "$2" ]; } || { [ ! -f "$3" ] || [ ! -w "$3" ]; }; then
    echo "Nie masz praw do modyfikacji przynajmniej jednego pliku lub on nie istnieje"
    exit 1
fi


line_number=1
for line in `cat "$1"`; do

    if (($line_number % 2 == 0)); then
        echo "$line_number $line" >> $2
    else
        echo "$line_number $line" >> $3
    fi
    line_number=$((line_number+1))

done