import click

from KingdomSouls.commands.character import character


@click.group()
def cli():
    pass


cli.add_command(character)
