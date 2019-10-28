import kingdomsouls.client
import kingdomsouls.database


def initialize():
    kingdomsouls.database.prepare()
    kingdomsouls.client.cli()
