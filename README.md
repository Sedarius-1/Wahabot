# Wahabot
Patchnotes for alpha 0.0.2
1. Added briefs and descriptions to every command
2. Added option to track, list, add, and mark goals as finished
3. Fixed removing from list (now displays a proper message)
4. Fixed creating database (main.txt now is generated properly)
5. Removed unnecessary args in some commands

Fix #1
1. check_user_database and checklist now display proper commands in error messages

Fix #2
1. Forced lowercase(user might input uppercase, but they will be converted anyway) and alphanumeric symbols-only in paths (creating, copying and removing lists)