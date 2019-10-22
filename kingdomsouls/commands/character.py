import sqlite3

import click

import kingdomsouls.database


@click.group()
def character():
    """Click group for character-related commands."""
    pass


@character.command()
@click.option(
    "--name", prompt="Please enter your character's name", help="The character's name"
)
@click.option(
    "--attack",
    prompt="What is your character's attack",
    help="The character's attack",
    default=0,
)
@click.option(
    "--defense",
    prompt="What is your character's defense",
    help="The character's defense",
    default=0,
)
def create(name: str, attack: int, defense: int) -> None:
    """
    Create a new character.

    :param name: the character's name
    :param attack: the character's attack
    :param defense: the character's defense
    """
    con = kingdomsouls.database.connect()
    with con:
        try:
            con.execute(
                """
                INSERT INTO characters (name, attack, defense)
                VALUES (?, ?, ?)
            """,
                (name, attack, defense),
            )
            click.echo(f"{name} has been created.")
        except sqlite3.Error as e:
            click.echo(f"Database error: {e}")
        except Exception as e:
            click.echo(f"Exception in _query: {e}")


@character.command()
@click.option(
    "--name",
    prompt="Please enter the name of the character you want to delete",
    help="The character's name",
)
def delete(name: str) -> None:
    """
    Delete a character.

    :param name: the character's name
    """
    con = kingdomsouls.database.connect()
    with con:
        try:
            con.execute(
                """
                DELETE FROM characters
                WHERE name = ?
            """,
                (name,),
            )
        except sqlite3.Error as e:
            click.echo(f"Database error: {e}")
        except Exception as e:
            click.echo(f"Exception in _query: {e}")


@character.command()
@click.option("--name", prompt="Who are you training?", help="The character's name")
def train_attack(name: str) -> None:
    """
    Increase a character's attack by 1.

    :param name: the character's name
    """
    con = kingdomsouls.database.connect()
    with con:
        try:
            con.execute(
                """
                UPDATE characters
                SET attack = attack + 1
                WHERE name = ?
            """,
                (name,),
            )
        except sqlite3.Error as e:
            click.echo(f"Database error: {e}")
        except Exception as e:
            click.echo(f"Exception in _query: {e}")


@character.command()
@click.option("--name", prompt="Who are you training?", help="The character's name")
def train_defense(name: str) -> None:
    """
    Increase a character's defense by 1.

    :param name: the character's name
    """
    con = kingdomsouls.database.connect()
    with con:
        try:
            con.execute(
                """
                UPDATE characters
                SET defense = defense + 1
                WHERE name = ?
            """,
                (name,),
            )
        except sqlite3.Error as e:
            click.echo(f"Database error: {e}")
        except Exception as e:
            click.echo(f"Exception in _query: {e}")


@character.command()
@click.option("--name1", prompt="Choose the first fighter", help="The character's name")
@click.option(
    "--name2", prompt="Choose the second fighter", help="The character's name"
)
def fight(name1: str, name2: str) -> None:
    """
    Battle two characters. The character with higher power (attack + defense) wins.

    :param name1: the name of character 1
    :param name2: the name of character 2
    """
    con = kingdomsouls.database.connect()
    with con:
        try:
            p1 = con.execute(
                """
                SELECT attack + defense AS power
                FROM characters
                WHERE name = ?
            """,
                (name1,),
            ).fetchall()[0]["power"]
            p2 = con.execute(
                """
                SELECT attack + defense AS power
                FROM characters
                WHERE name = ?
            """,
                (name2,),
            ).fetchall()[0]["power"]
        except sqlite3.Error as e:
            click.echo(f"Database error: {e}")
        except Exception as e:
            click.echo(f"Exception in _query: {e}")
    if p1 > p2:
        click.echo(f"{name1} wins!")
    elif p1 < p2:
        click.echo(f"{name2} wins!")
    else:
        click.echo(f"Its a tie between {name1} and {name2}!")


@character.command()
def show() -> None:
    """Show all character details."""
    con = kingdomsouls.database.connect()
    with con:
        try:
            rows = con.execute(
                """
                SELECT name, attack, defense from characters
            """
            )
        except sqlite3.Error as e:
            click.echo(f"Database error: {e}")
        except Exception as e:
            click.echo(f"Exception in _query: {e}")
    for (name, attack, defense) in rows.fetchall():
        click.echo(f"Character name: {name}, Attack: {attack}, Defense: {defense}")
