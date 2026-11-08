# Pass-Crack

A small command line tool that builds candidate password and username lists from a few facts about a target.

For authorised testing and learning only. Use it on accounts and systems you own or have written permission to test.

You pick an option from the menu, type in a name, surname, nickname and birth date, and the script permutes those pieces into a wordlist. Option 1 writes password candidates to `pass.txt`. Option 2 combines the same inputs with common admin usernames (root, admin, administrator and so on) and writes to `username.txt`. It is one file, `pass.py`, and it was an early project for me to understand how weak, personal-info passwords get guessed.

## Running it

```
python3 pass.py
```

It expects a Linux environment: it calls `clear` and uses `figlet` for the banners, and tries to `apt-get install figlet` on start.

Status: learning project, 2021, not maintained.
