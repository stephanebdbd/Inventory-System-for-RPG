import csv
import xml
import sys

def importXML(file: str):
    print(file)
    pass

def importCSV(file: str):
    print(file)
    pass

def importJSON(file: str):
    print(file)
    pass

def main():
    while True:
        sys.clear()
        print("** Enter [q] to leave **\n")
        file = input("Enter file name: ")
        if "csv" in file:
            importCSV(file)
        if "xlm" in file:
            importXML(file)
        if "json" in file:
            importJSON(file)


if __name__ == "main":
    main()