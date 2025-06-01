## 1. Make the DB script executable
chmod +x db_script.sh

## 2. Run the DB script
./db_script.sh

## 3. Connect to MySQL
mysql -u pietro -p rpgg
# When prompted for the password, enter:
YildizMyGoat1!

## 4. Load the schema into MySQL
# Option A: From your project root
SOURCE /your/path/to/project/project2/src/database/schema/all.sql;

# Option B: Navigate into the schema folder first
cd /your/path/to/project/project2/src/database/schema   or   navigate to /schema
mysql -u pietro -p rpgg
# then, inside the MySQL prompt:
SOURCE all.sql;

## 5. Import initial data
navigate to /database
python3 importData.py data

## 6. Run the RPGG application
navigate to /src
python3 rpgg.py
