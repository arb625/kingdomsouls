import kingdomsouls.client
import kingdomsouls.database

if __name__ == "__main__":
    kingdomsouls.database.prepare()
    kingdomsouls.client.cli()
