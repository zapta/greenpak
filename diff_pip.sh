#!/bin/bash

# A script to diff the pip installed serial_packets against the local git repo

#pip_pkg="/c/Users/user/AppData/Local/Programs/Python/Python312/Lib/site-packages/greenpak"
#pip_pkg="/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/greenpak"
pip_pkg="/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/greenpak.original"

#araxis="/c/Program Files/Araxis/Araxis Merge/Compare.exe"
araxis="/Applications/Araxis Merge.app/Contents/Utilities/compare"


git_pkg="./src/greenpak"

#ls $pip_pkg
#ls $git_pkg

"${araxis}" "$pip_pkg" "$git_pkg" 

