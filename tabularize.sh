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
    total_counter=$(grep -oP '(?<=Total Problems: )[0-9]+' ./README.md)
    new_total_counter=$((total_counter + 1))
    sed -i "s/Total Problems: $total_counter/Total Problems: $new_total_counter/" ./README.md

    # Get the difficulty counters
    easy_counter=$(grep -oP '(?<=Easy: )[0-9]+' ./README.md)
    medium_counter=$(grep -oP '(?<=Medium: )[0-9]+' ./README.md)
    hard_counter=$(grep -oP '(?<=Hard: )[0-9]+' ./README.md)

    # Extract the title from the <h2> tag
    TITLE=$(grep -oP '(?<=<h2>).*?(?=</h2>)' "$PROB_README")
    PROB=$(echo "$TITLE" | grep -oP '(?<=<a href=")[^"]+' | awk -F '/' '{if($NF == "") print $(NF - 1); else print $NF}')
    QUES=$(echo "$PROB" | sed 's/-/ /g')

    # Extract the difficulty from the <h3> tag
    DIFFICULTY=$(grep -oP '(?<=<h3>).*?(?=</h3>)' "$PROB_README")

    # Increment difficulty counters
    if [ "$DIFFICULTY" = "Easy" ]; then 
      new_easy_counter=$((easy_counter + 1))
      sed -i "s/Easy: $easy_counter/Easy: $new_easy_counter/" ./README.md
    elif [ "$DIFFICULTY" = "Medium" ]; then 
      new_medium_counter=$((medium_counter + 1))
      sed -i "s/Medium: $medium_counter/Medium: $new_medium_counter/" ./README.md
    else
      new_hard_counter=$((hard_counter + 1))
      sed -i "s/Hard: $hard_counter/Hard: $new_hard_counter/" ./README.md
    fi

    # Extract location
    LOC=$(echo "$folder" | sed 's/^..//')

    # Form table entry
    LINE="| $new_total_counter | [$QUES](/python/${LOC}) | $DIFFICULTY |"
    #echo $LINE >> ./README.md

    # Move solution to python dir
    #mv ${folder} ./python/.
  fi
done

