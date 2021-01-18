# Create & activate virtual env
mkdir genie
cd genie
python3 -m venv .
source bin/activate

# Get pyATS library
pip install pyATS[library]

# Get pyATS examples
git clone https://github.com/CiscoTestAutomation/examples

# Tests
pyats run job examples/basic/basic_example_job.py