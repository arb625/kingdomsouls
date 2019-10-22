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
    """Click runner to invoke commands."""
    return CliRunner()


def test_create(runner):
    """Test that creating a character works."""
    name = "Sora"
    attack = 10
    defense = 5
    result = _create_char(runner, name, attack, defense)

    assert result.exit_code == 0

    rows = _select_char(name)
    assert len(rows) == 1
    assert rows[0]["attack"] == attack
    assert rows[0]["defense"] == defense


def test_delete(runner):
    """Test that deleting a character works."""
    name = "Sora"
    _create_char(runner, name, 0, 0)
    result = _delete_char(runner, name)

    assert result.exit_code == 0

    rows = _select_char(name)
    assert len(rows) == 0


def test_train_attack(runner):
    """Test that training a character's attack works."""
    name = "Sora"
    attack = 10
    defense = 5
    _create_char(runner, name, attack, defense)
    result = _train_attack(runner, name)

    assert result.exit_code == 0

    rows = _select_char(name)
    assert len(rows) == 1
    assert rows[0]["attack"] == attack + 1


def test_train_defense(runner):
    """Test that training a character's defense works."""
    name = "Sora"
    attack = 10
    defense = 5
    _create_char(runner, name, attack, defense)
    result = _train_defense(runner, name)

    assert result.exit_code == 0

    rows = _select_char(name)
    assert len(rows) == 1
    assert rows[0]["defense"] == defense + 1


def test_fight(runner):
    """Test that battling two characters works."""
    _create_char(runner, "Sora", 10, 5)
    _create_char(runner, "Riku", 9, 7)

    result = _fight(runner, "Sora", "Riku")
    assert result.exit_code == 0
    assert "Riku wins!" in result.output

    _train_attack(runner, "Sora")
    result = _fight(runner, "Sora", "Riku")
    assert result.exit_code == 0
    assert "Its a tie between Sora and Riku!" in result.output

    _train_defense(runner, "Sora")
    result = _fight(runner, "Sora", "Riku")
    assert result.exit_code == 0
    assert "Sora wins!" in result.output


def _create_char(runner, name, attack, defense):
    return runner.invoke(
        kingdomsouls.commands.character.create, input=f"{name}\n{attack}\n{defense}"
    )


def _delete_char(runner, name):
    return runner.invoke(kingdomsouls.commands.character.delete, input=f"{name}")


def _train_attack(runner, name):
    return runner.invoke(kingdomsouls.commands.character.train_attack, input=f"{name}")


def _train_defense(runner, name):
    return runner.invoke(kingdomsouls.commands.character.train_defense, input=f"{name}")


def _fight(runner, name1, name2):
    return runner.invoke(
        kingdomsouls.commands.character.fight, input=f"{name1}\n{name2}"
    )


def _select_char(name):
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
