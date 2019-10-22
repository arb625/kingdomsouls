import pytest
from click.testing import CliRunner

import kingdomsouls.commands.character
import kingdomsouls.database


@pytest.fixture(scope="session", autouse=True)
def _run_around_all_tests():
    kingdomsouls.database.prepare()


@pytest.fixture(autouse=True)
def _run_around_each_test():
    kingdomsouls.database.clear_table("characters")


@pytest.fixture()
def runner():
    return CliRunner()


def test_create(runner):
    name = "Sora"
    attack = 10
    defense = 5
    result = create_char(runner, name, attack, defense)

    assert result.exit_code == 0

    rows = select_char(name)
    assert len(rows) == 1
    assert rows[0]["attack"] == attack
    assert rows[0]["defense"] == defense


def test_delete(runner):
    name = "Sora"
    create_char(runner, name, 0, 0)
    result = delete_char(runner, name)

    assert result.exit_code == 0

    rows = select_char(name)
    assert len(rows) == 0


def test_train_attack(runner):
    name = "Sora"
    attack = 10
    defense = 5
    create_char(runner, name, attack, defense)
    result = train_attack(runner, name)

    assert result.exit_code == 0

    rows = select_char(name)
    assert len(rows) == 1
    assert rows[0]["attack"] == attack + 1


def test_train_defense(runner):
    name = "Sora"
    attack = 10
    defense = 5
    create_char(runner, name, attack, defense)
    result = train_defense(runner, name)

    assert result.exit_code == 0

    rows = select_char(name)
    assert len(rows) == 1
    assert rows[0]["defense"] == defense + 1


def test_fight(runner):
    create_char(runner, "Sora", 10, 5)
    create_char(runner, "Riku", 9, 7)

    result = fight(runner, "Sora", "Riku")
    assert result.exit_code == 0
    assert "Riku wins!" in result.output

    train_attack(runner, "Sora")
    result = fight(runner, "Sora", "Riku")
    assert result.exit_code == 0
    assert "Its a tie between Sora and Riku!" in result.output

    train_defense(runner, "Sora")
    result = fight(runner, "Sora", "Riku")
    assert result.exit_code == 0
    assert "Sora wins!" in result.output


def create_char(runner, name, attack, defense):
    return runner.invoke(
        kingdomsouls.commands.character.create, input=f"{name}\n{attack}\n{defense}"
    )


def delete_char(runner, name):
    return runner.invoke(kingdomsouls.commands.character.delete, input=f"{name}")


def train_attack(runner, name):
    return runner.invoke(kingdomsouls.commands.character.train_attack, input=f"{name}")


def train_defense(runner, name):
    return runner.invoke(kingdomsouls.commands.character.train_defense, input=f"{name}")


def fight(runner, name1, name2):
    return runner.invoke(
        kingdomsouls.commands.character.fight, input=f"{name1}\n{name2}"
    )


def select_char(name):
    con = kingdomsouls.database.connect()
    with con:
        rows = con.execute(
            """
            SELECT * FROM characters
            WHERE name = ?
        """,
            (name,),
        ).fetchall()
    return rows
