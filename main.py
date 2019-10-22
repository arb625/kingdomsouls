import KingdomSouls.client
import KingdomSouls.database

if __name__ == "__main__":
    KingdomSouls.database.prepare()
    KingdomSouls.client.cli()
