# PingPongProject

## Misc 
[Link to the game protocol](https://gitlab.lrz.de/LKN_IK_Games/GameProtocol/blob/master/lobby/README.md)
`

## Basic Git Commands

`git clone *link_of_the_repository*`

This will create the directory PingPongProject, in which you will find our files.



`git branch` 

Lists the locally available branches. E.g. selver



`git branch -a`

Also lists branches that are available on the remote server.



`git branch *name_of_branch*` 

Creates a branch with the specified name. This command is **only** for creating a branch 



`git checkout *name_of_branch*` 

Lets you switch to the spcified branch.



`git status` 

View status of files.



`git add *name_of_file*`

Stages the specified file for a commit. You can see the files that will be committed with `git status`



`git commit -m *commit_message*`

Commits your changes that have been staged for the commit.
Changes are only recorded locally.

`git rebase -i *branch_name*`

Takes the commits from "*branch_name*" and applies them to the currently active branch. Typically used to pull in latestest changes from master e.g. `git rebase -i origin/master`

