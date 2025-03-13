#!/bin/bash

# Define the folder to check
PARENT_FOLDER="."

# Check if the folder exists
if [ ! -d "$PARENT_FOLDER" ]; then
    echo "Folder does not exist: $PARENT_FOLDER"
    exit 1
fi

# Search for newly committed solutions, inside the parent folder
for folder in "$PARENT_FOLDER"/[0-9]*/; do
    if [ -d "$folder" ]; then
	PROB_README=${folder}/README.md

	# Get the problem number
	counter=$(grep -oP '(?<=Total=)[0-9]+' ./README.md)
	new_counter=$((counter + 1))
	sed -i "s/Total=$counter/Total=$new_counter/" ./README.md

	# Extract the title from the <h2> tag
	TITLE=$(grep -oP '(?<=<h2>).*?(?=</h2>)' "$PROB_README")
	PROB=$(echo "$TITLE" | grep -oP '(?<=<a href=")[^"]+' | awk -F '/' '{if($NF == "") print $(NF - 1); else print $NF}')
	QUES=$(echo "$PROB" | sed 's/-/ /g')

	# Extract the difficulty from the <h3> tag
	DIFFICULTY=$(grep -oP '(?<=<h3>).*?(?=</h3>)' "$PROB_README")

	# Extract location
	LOC=$(echo "$folder" | sed 's/^..//')

	# Form column entry
	LINE="| $new_counter | [$QUES](/python/${LOC}) | $DIFFICULTY |"

	echo $LINE >> ./README.md

        mv ${folder} ./python/.
    fi
done

