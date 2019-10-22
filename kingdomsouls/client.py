import click

from kingdomsouls.commands.character import character


@click.group()
def cli():
    pass


cli.add_command(character)
