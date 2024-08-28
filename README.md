# Clyde - Command Line Yielded Data Extraction and Transformation

Clyde is an ETL tool designed for efficient data extraction and transformation, leveraging local AI processing with Ollama 3.1 for advanced data handling capabilities.

## Prerequisites

Before you begin, ensure you meet the following requirements:
- Python 3.8 or higher
- pip (Python package installer)
- Strong CPU or compatible GPU for running Ollama 3.1 locally
- Access to the Internet for currency conversion API

## Installation

### Clone the repository
```bash
git clone git@github.com:Guilherme-Denarde/Clyde-ETL.git
cd Clyde-ETL
```

### Set up a Python virtual environment (Optional but recommended)
```bash
python -m venv venv
# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

### Install required Python libraries
```bash
pip install -r requirements.txt
```

### Set up environment variables
- Copy the `.env.example` file to `.env`.
- Fill in the required details in the `.env` file.
```plaintext
API_KEY=your_currency_api_key_here
```

### Install Ollama Python Library
Ensure you have the Ollama library installed for local processing.
```bash
pip install ollama
```

## Usage

To run Clyde, execute the following command:
```bash
python main.py
```

## Contributing

To contribute to Clyde, follow these steps:
1. Fork the repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <branch_name>`.
5. Create the pull request.

For more information on creating a pull request, see the [GitHub documentation on creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License

Clyde is available under the MIT License, which allows for modification, distribution, private and commercial use. See the LICENSE file for more details.