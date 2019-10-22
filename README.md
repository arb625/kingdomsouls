Game where you can create, train, and battle with characters.
Inspired by Kingdom Hearts.

Installation:
---

`pip install kingdomsouls`

Or download the latest binary in releases.

Usage:
---

Running just `kingdomsouls` will give a list of available commands.

#### Create a character

Specify the characters name, attack, and defense:
```
kingdomsouls character create Sora 10 5
```

#### Delete a character

Specify the name of the character to delete.
```
kingdomsouls character delete Sora
```

#### Train a character's attack strength 

Specify the characters name to increase his/her attack strength by 1.
```
kingdomsouls character train-attack Sora
```

#### Train a character's defense strength 

Specify the characters name to increase his/her defense strength by 1.
```
kingdomsouls character train-defense Sora
```

#### Battle two characters

Specify the names of the two characters who will battle. The winner will be the one with more power (attack + defense).
```
kingdomsouls character fight Sora Riku
```

Notes
---
I'm using this fairly simple project as a way for me to practice writing, testing, and deploying a project in Python.
The hope is that the boilerplate I set up here will be useful for my future Python projects.
In that vein and for my own documentation, here are the configuration tools I'm using and what they do.

* pytest: testing 
* pytest-cov: test coverage
* docker: testing on multiple platforms
* travis ci: continuous integration
* mypy: static type checker
* isort: organize imports
* black: python formatter
* flake8: python linter
