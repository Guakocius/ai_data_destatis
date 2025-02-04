# Statistisches Bundesamt Data Fetcher and Analyzer

## Overview

This project is a Python-based AI application designed to fetch data from the database of the Statistisches Bundesamt (Federal Statistical Office of Germany). The fetched data is stored in a local database, where it is subsequently analyzed to provide trend analysis.

## Features

- Fetches data from the Statistisches Bundesamt database
- Stores data in a local database
- Analyzes data to provide trend analysis

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Guakocius/ai_data_destatis.git

    ```

2. Navigate to the project directory:

    ```sh
    cd destatis_db
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the data fetcher script to retrieve data from the Statistisches Bundesamt database:

    ```sh
    python fetch_data.py
    ```

2. Run the analysis script to analyze the fetched data and get trend analysis:

    ```sh
    python analyze_data.py
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
