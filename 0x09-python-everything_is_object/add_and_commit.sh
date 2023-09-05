#!/bin/bash

# Loop through each file in the folder
for file in *; do
  # Check if the file is a regular file (i.e. not a directory)
  if [[ -f "$file" ]]; then
    # Add the file to Git and commit it with a message "add: file {number}"
    git add "$file"
    git commit -m "add: file ${file%%-*}"
  fi
done
