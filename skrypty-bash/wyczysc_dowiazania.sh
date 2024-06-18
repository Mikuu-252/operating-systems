if [ "$#" -ne 2 ]; then
    echo "Musisz podac 2 parametry."
    echo "Przyklad: $0 [katalog] [plik]"
    exit 1
fi

if [ ! -f "$2" ] || [ ! -r "$2" ] || [ ! -w "$2" ]; then
    echo "Nie masz praw do odczytu lub zapisu pliku ($1) lub on nie istnieje"
    exit 1
fi

if [ ! -d "$1" ] || [ ! -r "$1" ] || [ ! -w "$1" ] || [ ! -x "$1" ]; then
    echo "Nie masz praw do odczytu lub zapisu w katalogu ($1) lub on nie istnieje"
    exit 1
fi

for link in `find "$1" -type l`; do

    if [ ! -L "$link" ] || [ ! -w "$link" ]; then
        echo "Nie masz praw do usuniecia dowiazania ($link)"
        continue
    fi

    echo "Czy usunac dowiazanie symboliczne: $link? [y/t]"
    read reply

    if [ "$reply" = 'y' ] || [ "$reply" = 't' ]; then
        rm "$link"
        echo "Usunieto dowiazanie: $link" >> "$2"
    fi
done