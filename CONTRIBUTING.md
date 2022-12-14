# Step 1: Fork the project repository

Fork the repository to you GitHub
[Fork - Click Here](https://github.com/TheInspiredConjurer/Online-Questionnaire-System/fork)

# Step 2: Clone your fork

While still in your repository, click on the code drop down menu. Now you can either download the zip file and extract it on your local system or copy the https url and use the command git clone <https url> to clone it to a local directory/folder. 
  
```bash
git clone <https url or .git url>
```

# Step 3: Navigate to your local repository

Since the clone was downloaded into a subdirectory of your working directory, you can navigate to it using: cd NAME_OF_REPOSITORY.

For example,

```bash
cd Online-Questionnaire-System
```

# Step 4: Pull the latest changes from upstream into your local repository

Before you start making any changes to your local files, it's a good practice to first synchronize your local repository with the project repository. Use git pull upstream main to "pull" any changes from the "main" branch of the "upstream" into your local repository. 
  
  ```bash
git pull upstream main
```

If you forked and cloned the project repository just a few minutes ago, it's very unlikely there will be any changes, in which case Git will report that your local repository is "already up to date". But if there are any changes, they will automatically be merged into your local repository.

# Step 5: Create a new branch

Rather than making changes to the project's "main" branch, it's a good practice to instead create your own branch. This creates an environment for your work that is isolated from the master branch.

Use git checkout -b BRANCH_NAME to create a new branch and then immediately switch to it. The name of the branch should briefly describe what you are working on, and should not contain any spaces.

For example,

```bash
git checkout -b documentation
```

Use git branch to show your local branches. You should see your new branch as well as "main", and your new branch should have an asterisk next to it to indicate that it's "checked out" (meaning that you're working in it).
  
```bash
git branch
```

# Step 6: Make changes in your local repository

Use a text editor or IDE to make the changes you planned to the files in your local repository. Because you checked out a branch in the previous step, any edits you make will only affect that branch.

# Step 7: Git Add and Commit your changes

After you make a set of changes, use git add -A or git add . to stage your changes and `git commit -m "DESCRIPTION OF CHANGES"` to commit them.

For example, `commit -m "create base for svelte game version"` for one of my commits.
  
 ```bash
git add .
git commit -m "<Description of changes>"
```

If you are making multiple sets of changes, it's a good practice to make a commit after each set.

# Step 8: Push your changes to your fork

When you are done making all of your changes, upload these changes to your fork using git push origin BRANCH_NAME. This "pushes" your changes to the "BRANCH_NAME" branch of the "origin" (which is your fork on GitHub).

For example: `git push origin documentation`
  
  ```bash
git push origin <BRANCH_NAME>
```

# Step 9: Begin the pull request

Return to your fork on GitHub, and refresh the page. You may see a highlighted area that displays your recently pushed branch:

Click the green Compare & pull request button to begin the pull request.
  

# Step 10: Create the pull request
  
Pull Request Message Format: -
  
  ```
  [Front-End / Back-End / Miscellaneous] [Type of Issue] - (Title Message)
  
  ```
  
  
  ```
   - Detail 1 about Pull Request.
   - Detail 2 about Pull Request.
   - Detail 3 about Pull Request.
               .
               .
               .
  ```
  
  - Use the `Miscellaneous` tag if you are making any non-code contributions, such as documentation, design changes, etc.
  - `Type of Issue` must be one of the following: -
     1. FEAT / ENHANCEMENT - Adding a new feature.
     2. FIX - A bug fix.
     3. DOCS - Making any type of changes (add / delete / update) to the documentation.
     4. STYLE - Everything related to styling.
     5. REFACTOR - Code changes that neither fixes a bug nor adds a feature.
     6. SUGGESTION - Suggestion or new ideas
     7. CHORE - Updating build tasks, package manager configs, etc.
  - The `Title Message` must be written in the imperative eg. 'Add' instead of 'Added' or 'Adds'.

   
  
  examples:
  <br><br>
  `[Front-End] [BUG] - Fix bug in Vue routing`
  <br>
  ` - Add routing component that fixes issue #21`
  (Note: If you are submitting a Pull Request that solves an issue, then when you type the #(issue number) in the message, Github will automatically show you the issue, which you can then link by simply clicking on it).
  
  <br><br>
  `[Miscellaneous] [DOCS] - Add icons to documentation`
  <br>
  ` - Edit README.md to include icons of programming languages`
  

Before submitting the pull request, you first need to describe the changes you made (rather than asking the project maintainers to figure them out on their own). You should write a descriptive title for your pull request, and then include more details in the body of the pull request. If there are any related GitHub issues, make sure to mention those by number. The body can include Markdown formatting, and you can click the Preview tab to see how it will look.

Below the pull request form, you will see a list of the commits you made in your branch, as well as the "diffs" for all of the files you changed.!

If everything looks good, click the green Create pull request button!
