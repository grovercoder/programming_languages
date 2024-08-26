# Programming Languages

This code provides a list of current programming languages.

This information is found via https://www.tiobe.com/tiobe-index/programminglanguages_definition and then presented in as plain text and JSON.

## Usage:

Easy Method:

- Download the `languages.txt` or `languages.json` file to your project.

Less easy method, for when you need the latest list:

1. clone this project
1. create a virtual environment (substitute your method of choice, but I'm using the VENV module)

    ```
    cd project
    python3 -m venv .venv
    source .venv/bin/activate
    ```

1. install dependencies:

    ```
    pip install beautifulsoup4 requests
    ```

1. run the code:

    ```
    python3 programming_languages.py
    ```

1. Copy the generated `languages.txt` or `languages.json` file to your project.


## Why this code?

It is rare, but occasionally I need a relatively current list of programming languages.  Now instead of generating this list manually for each project, I have a starting file already pre-built and easily updated.
