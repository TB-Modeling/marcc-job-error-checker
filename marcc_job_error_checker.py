"""MARCC Job Error Checker

# Usage
1. Keep this file in same directory as SLURM arrayJob files
2. Run:

    python3 marcc_job_error_checker.py

# TODO's
- Get dir from calling command so can work as package.
- More: See test.py
"""
import os

from glob import glob


# Config
from typing import List

base_pattern = 'arrayJob'

# Constants
THIS_DIR: str = os.path.dirname(os.path.realpath(__file__))
TARGET_DIR: str = THIS_DIR


# Definitions
def main(target_dir=TARGET_DIR):
    """Main"""
    header_good = 'No errors were found.'
    header_bad = 'The following files were found which contain errors:\n'
    pattern = os.path.join(target_dir, base_pattern + '*.err')
    files: List[str] = glob(pattern)

    error_files_found = ''
    for path in files:
        with open(path, 'r') as file:
            text: str = file.read()
            if text:
                error_files_found += path + '\n'

    report: str = header_good if not error_files_found \
        else header_bad + error_files_found
    print(report)


# Test
def test():
    """Test"""
    test_dir: str = os.path.join(TARGET_DIR, 'test')
    main(target_dir=test_dir)


# Run
main()
# test()
