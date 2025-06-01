DB_ROOT_PASS="metTonVraiPw"
DB_PASSWORD="YildizMyGoat1!"
DB_NAME="pietro"
DB_USER="rpgg"

echo "Setting up local database..."

mysql -u root -p"${DB_ROOT_PASS}" <<_EOF_
CREATE DATABASE IF NOT EXISTS \`${DB_NAME}\`;
CREATE USER IF NOT EXISTS '${DB_USER}'@'localhost' IDENTIFIED BY '${DB_PASSWORD}';
GRANT ALL PRIVILEGES ON \`${DB_NAME}\`.* TO '${DB_USER}'@'localhost';
FLUSH PRIVILEGES;
_EOF_