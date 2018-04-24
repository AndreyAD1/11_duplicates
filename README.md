# Anti-Duplicator

This script gets a directory path (relative or absolute) and returns names and paths of
duplicate files located in this directory.

# Quick start

The script requires Python v3.5. A directory path is the positional argument
of the script.

To run script on Linux:

```bash
$ python duplicates.py /home/folders
The directory contains these duplicate files:
somefile.txt
       folders/somefile.txt
       folders/new/somefile.txt
test.txt
       folders/test.txt
       folders/test/test.txt
```
Windows launch is the same.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
