## 1. Install
install mysql
install mysql connector
install rich
install getkey


## 2. Make the DB script executable
navigate to /src
chmod +x db_script.sh

## 3. Run the DB script
update the mdp in the script
./db_script.sh

## 4. Connect to MySQL
mysql -u pietro -p rpgg
# When prompted for the password, enter:
YildizMyGoat1!

## 5. Load the schema into MySQL
# Option A: From your project root
SOURCE /your/path/to/project/project2/src/database/schema/all.sql;

# Option B: Navigate into the schema folder first
cd /your/path/to/project/project2/src/database/schema   or   navigate to /schema
mysql -u pietro -p rpgg
# then, inside the MySQL prompt:
SOURCE all.sql;

## 6. Import initial data
navigate to /database
python3 importData.py data

## 7. Run the RPGG application
navigate to /src
python3 rpgg.py