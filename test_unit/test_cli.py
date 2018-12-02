import os
import pytest
import filabel



def test_cli_help(runner):
    res = runner.invoke(filabel.cli, ['--help'])
    assert 'help' in res.output


def test_cli_config_not_supplied(runner, configs_path):
    config_auth = configs_path + '/auth.fff.cfg'
    res = runner.invoke(filabel.cli, ['--config-auth', config_auth])
    assert 'Labels configuration not supplied' in res.output


def test_cli_invalid_value(runner):
    res = runner.invoke(filabel.cli, ['--config-labels', 'test'])
    assert 'Invalid value' in res.output


def test_cli_reposlug_not_valid(runner, configs_path):
    config_labels = configs_path + '/labels.abc.cfg'
    config_auth = configs_path + '/auth.fff.cfg'
    slug = 'foobar'

    res = runner.invoke(filabel.cli, ['--config-labels', config_labels,
                                      '--config-auth', config_auth, slug])
    assert 'Reposlug {} not valid'.format(slug) in res.output
