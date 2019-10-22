import click

import KingdomSouls.database


@click.group()
def character():
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
def create(name, attack, defense):
    con = KingdomSouls.database.connect()
    with con:
        con.execute(
            """
            INSERT INTO characters (name, attack, defense) 
            VALUES (?, ?, ?)
        """,
            (name, attack, defense),
        )


@character.command()
@click.option(
    "--name",
    prompt="Please enter the name of the character you want to delete",
    help="The character's name",
)
def delete(name):
    con = KingdomSouls.database.connect()
    with con:
        con.execute(
            """
            DELETE FROM characters 
            WHERE name = ?
        """,
            (name,),
        )


@character.command()
@click.option("--name", prompt="Who are you training?", help="The character's name")
def train_attack(name):
    con = KingdomSouls.database.connect()
    with con:
        con.execute(
            """
            UPDATE characters 
            SET attack = attack + 1
            WHERE name = ? 
        """,
            (name,),
        )


@character.command()
@click.option("--name", prompt="Who are you training?", help="The character's name")
def train_defense(name):
    con = KingdomSouls.database.connect()
    with con:
        con.execute(
            """
            UPDATE characters 
            SET defense = defense + 1
            WHERE name = ? 
        """,
            (name,),
        )


@character.command()
@click.option("--name1", prompt="Choose the first fighter", help="The character's name")
@click.option(
    "--name2", prompt="Choose the second fighter", help="The character's name"
)
def fight(name1, name2):
    con = KingdomSouls.database.connect()
    with con:
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
    if p1 > p2:
        click.echo(f"{name1} wins!")
    elif p1 < p2:
        click.echo(f"{name2} wins!")
    else:
        click.echo(f"Its a tie between {name1} and {name2}!")


@character.command()
def show():
    con = KingdomSouls.database.connect()
    with con:
        rows = con.execute(
            """
            SELECT name, attack, defense from characters
        """
        )
    for (name, attack, defense) in rows.fetchall():
        click.echo(f"Character name: {name}, Attack: {attack}, Defense: {defense}")
