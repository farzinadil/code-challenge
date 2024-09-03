# Extract Van Gogh Paintings Code Challenge

## Prerequisites

- Python 3.7+
- Make

### Checking Prerequisites

1. Check Python version:
<code>python3 --version</code>
This should return a version number 3.7 or higher.
2. Check if Make is installed:
<code>make --version</code>
This should display the version of Make installed on your system.

### Installing Prerequisites

- Python: If not installed, download and install from [python.org](https://www.python.org/downloads/)
- Make: If not installed: 
- On Ubuntu/Debian: <code>sudo apt-get install make</code>
- On macOS: Install Xcode Command Line Tools by running <code>xcode-select --install</code>

## Installation

To set up the project, run:
<code>make install</code>

This command creates a virtual environment and installs all necessary dependencies.

## Usage

### Running the Script

To generate the search array:
<code>make run</code>

This command will:
1. Parse van-gogh-paintings.html
2. Process the data
3. Generate a JSON array named `generated_array.json` in the files directory

### Running Tests

To run the test suite:

<code>make test</code>

This command runs all tests in the `tests` directory.

### Cleaning Up

To remove generated files, cached Python files, and the virtual environment:

<code>make clean</code>

## Running Without Make

If you prefer not to use Make, or if it's not available on your system, you can run the project directly using Python commands. Here's how:

1. Create a virtual environment:

<code>python3 -m venv venv</code>

2. Activate the virtual environment:

<code>source venv/bin/activate</code>

3. Install dependencies:

<code>pip install -r requirements.txt</code>

### Running the Script

4. Run the main script:

<code>python3 src/scrape.py</code>

### Running Tests

To run the test suite:

<code>python3 -m unittest discover tests</code>


## Project Structure

- `src/`: Main script for parsing html and generating json output
- `files/`: Supporting files including html and generated files
- `tests/`: Directory containing test files
- `Makefile`: Contains commands for installing dependencies, running the script, running tests, and cleaning up
- `.env`: (Not in repository) Contains API URL and API key

## Other HTML files

To use other HTML files, change file to 49ers-players.html or warriors.html in file/config.ini