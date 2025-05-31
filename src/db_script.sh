# faut faire cette comande avant pr pouvoir exec le script             chmod +x setup.sh
# pr linux donc windows = fucked, mais c pas bien diff en sah

DB_PASSWORD="YildizMyGoat1!"
DB_NAME="pietro"
DB_USER="rpgg"

echo " Setting up local database..."

sudo mysql <<_EOF_
CREATE DATABASE ${DB_NAME};
CREATE USER '${DB_USER}'@'localhost' IDENTIFIED BY '${DB_PASSWORD}';
GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'localhost';
FLUSH PRIVILEGES;
_EOF_