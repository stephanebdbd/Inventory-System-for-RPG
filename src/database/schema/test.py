import sqlparse
from sqlparse.tokens import Comment
import sys

def main():
    path = "queries.sql"
    with open(path, 'r', encoding='utf-8') as f:
        key = None
        query = []
        for line in f:
            if line.startswith('--'):
                if key:
                    print(key)
                    querys = ' '.join(query)
                    print(querys)
                key = line.strip("--").strip()
            else:
                query.append(line.strip())
    

if __name__ == "__main__":
    main()