#!/bin/bash

# Check if there are any changes to commit
if git diff --exit-code --quiet; then
    echo "No changes to commit."
else
    # Add all changes
    git add .

    # Commit changes with a default commit message
    git commit -m "Update: $(date '+%Y-%m-%d %H:%M:%S')"

    # Push changes to the origin repository
    git push
fi

