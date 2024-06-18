#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Musisz podac minimum 2 parametr."
    echo "Przyklad: $0 [prawa_numerycznie] [plik1] [plik2] [plik3] ..."
    exit 1
fi

if ! [[ "$1" =~ ^[0-7]{3}$ ]]; then
    echo "Musisz podac poprawne prawa numeryczne skladajace sie z 3 cyfr 0-7."
    echo "Przyklad: $0 [prawa_numerycznie] [plik1] [plik2] [plik3] ..."
    exit 1
fi

for file in "${@:2}"; do
    if [ ! -w "$file" ]; then
        echo "Nie masz praw do modyfikacji pliku ($file) lub on nie istnieje"
        continue
    fi

    chmod "$1" "$file"
    echo "Plik $file dostal prawa $1"
done

exit 0