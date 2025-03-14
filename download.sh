#!/bin/bash
# Download the entire data for the project
# (hosted on Zenodo). This allows large data
# files to be downloaded without hosting too
# much on the GitHub repo

cd data

# Downloading main data
wget https://zenodo.org/records/15025644/files/2025-quests-data.tar.gz

tar -zxf 2025-quests-data.tar.gz

cd ..
