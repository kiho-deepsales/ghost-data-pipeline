from scripts.table_creator import create_table
from scripts.fetcher import fetch
from scripts.preprocessor import preprocess
from scripts.uploader import upload


def main():
    create_table()
    fetch()
    preprocess()
    upload()


if __name__ == "__main__":
    main()