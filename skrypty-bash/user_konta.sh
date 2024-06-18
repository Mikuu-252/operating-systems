#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Musisz podac minimum 1 parametr."
    echo "Przyklad: $0 [uzytkownik1] [uzytkownik2] [uzytkownik3] ..."
    exit 1
fi

for user in $@; do
    if id "$user" &>/dev/null; then
        echo "$user juz istnieje."
    else
        useradd -m -s /bin/bash "$user"
        echo "$user:$user" | chpasswd $user
        passwd -e "$user" &>/dev/null

        echo "Konto "$user" zostalo utworzone."
    fi
done

exit 0