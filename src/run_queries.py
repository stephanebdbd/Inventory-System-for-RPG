from bin.database import Database
import os

def run_queries_from_file(cursor, file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            queries = content.split(';')
            for idx, query in enumerate(queries):
                query = query.strip()
                if query:
                    print(f"\n🔎 Query {idx + 1}:\n{query}")
                    try:
                        cursor.execute(query)
                        results = cursor.fetchall()
                        print("✅ Results:")
                        for row in results:
                            print(row)
                    except Exception as e:
                        print(f"❌ Error while executing query: {e}")
    except FileNotFoundError:
        print(f"❌ Could not find file: {file_path}")

def main():
    # Your database config
    db = Database(
        host="localhost",
        user="root",
        password="",  
        database="rpg"
    )

    cursor = db.get_cursor()

    # Adjusted path to where the file actually is:
    query_file_path = os.path.join("database","schema", "queries.sql")
    run_queries_from_file(cursor, query_file_path)

if __name__ == "__main__":
    main()
