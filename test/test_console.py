import pytest
import click.testing

from chess_stats import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.mark.e2e
def test_main_succeeds(runner):
    result = runner.invoke(console.main, args=["jjjulio", "2020"], catch_exceptions=False)
    assert result.exit_code == 0
