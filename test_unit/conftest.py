import configparser
import os
import sys

import betamax
import pytest
from click.testing import CliRunner

from filabel.logic import GitHub, Filabel

DEFAULT_USERNAME = 'skvaryk'
ABS_PATH = os.path.abspath(os.path.dirname(__file__))
FIXTURES_PATH = ABS_PATH + '/fixtures'
CASSETTES_PATH = FIXTURES_PATH + '/cassettes'
CONFIGS_PATH = FIXTURES_PATH + '/configs'
sys.path.insert(0, ABS_PATH + '/../')
os.environ['FILABEL_CONFIG'] = CONFIGS_PATH + '/' + 'testConfig.txt'

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = CASSETTES_PATH
    config.default_cassette_options['match_requests_on'] = [
        'method',
        'uri',
    ]
    gh_token = os.environ.get('GH_TOKEN', '<TOKEN>')
    if 'GH_TOKEN' in os.environ:
        config.default_cassette_options['record_mode'] = 'all'
    else:
        config.default_cassette_options['record_mode'] = 'none'
    config.define_cassette_placeholder('<TOKEN>', gh_token)
    config.preserve_exact_body_bytes = True


@pytest.fixture
def gh(betamax_parametrized_session, token):
    gh = GitHub(token, betamax_parametrized_session)
    return gh


@pytest.fixture
def username():
    username = os.environ.get('GH_USER')
    if not username:
        return DEFAULT_USERNAME
    return username


@pytest.fixture
def token():
    return os.environ.get('GH_TOKEN', '<TOKEN>')


@pytest.fixture(params={'/labels.abc.cfg', '/labels.eraser.cfg'})
def filabel(betamax_parametrized_session, token, request):
    cfg_labels = configparser.ConfigParser()
    file_path = CONFIGS_PATH + request.param
    with open(file_path, 'r') as f:
        cfg_labels.read_file(f)
        yield Filabel(token, cfg_labels['labels'], session=betamax_parametrized_session)


@pytest.fixture
def webapp(gh):
    from filabel.web import create_app
    app = create_app(gitHub=gh)
    app.config['TESTING'] = True
    return app.test_client()


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def configs_path():
    return CONFIGS_PATH
