import click

from kingdomsouls.commands.character import character


@click.group()
def cli():
    """Umbrella group for all commands in kingdomsouls."""
    pass


cli.add_command(character)
