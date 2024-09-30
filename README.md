README  
This expense Jupyter notebook work over bank accounts and credit cards extracts.
Three csv files are processed:
    TD chequing account 
    TD VISA Aeroplan
    BMO chequing account
    CIBC Costco credit card

Create a new repository on the command line
echo "# expenses" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sergiofaro/expenses.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/sergiofaro/expenses.git
git branch -M main
git push -u origin main

Rebasing your changes. It rewrites the history.
    Fetch the latest changes:
        git fetch origin
Rebase your local branch:
        git rebase origin/<branch-name>
Push your rebased changes:
    git push origin <branch-name>
List of commands to update GitHub after processing changes locally
cd path/to/your/repository
git status
git add .
git commit -m "Describe your changes here"
git pull origin main
git push origin main

Conventions and Symbols:
?? (Untracked files):
The file is not staged or tracked by Git. It exists in the working directory but hasn't been added to the index.
A (Staged, Added):
The file has been added to the staging area (index) and is a new file ready to be committed.
M (Staged, Modified):
The file has been modified and the changes have been staged (ready to commit).
M (Unstaged, Modified):
The file has been modified in the working directory but the changes are not staged yet.
AM (Staged, Added and Modified):
A new file was added and then modified before committing.
D (Unstaged, Deleted):
The file was deleted in the working directory but the change hasn't been staged yet.
D (Staged, Deleted):
The file has been deleted and the change has been staged for the next commit.
R (Staged, Renamed):
The file has been renamed and this change is staged for commit.
C (Staged, Copied):
A copy of the file is staged.
UU (Unmerged, Both Modified):
The file is in a conflict state after a merge, with changes in both versions that need to be resolved.

