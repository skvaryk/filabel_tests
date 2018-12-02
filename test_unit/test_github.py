import pytest


def test_user(gh, username):
    user = gh.user()
    assert username == user['login']


@pytest.mark.parametrize('repo', ('filabel-testrepo1', 'filabel-testrepo2', 'filabel-testrepo4'))
def test_pull_requests(gh, username, repo):
    pr = gh.pull_requests(username, repo)
    assert repo in pr[0]['url']


@pytest.mark.parametrize('repo', ('filabel-testrepo1', 'filabel-testrepo2', 'filabel-testrepo4'))
def test_pr_files(gh, username, repo):
    files = gh.pr_files(username, repo, 1)
    assert files


@pytest.mark.parametrize('repo', ('filabel-testrepo1', 'filabel-testrepo2', 'filabel-testrepo4'))
def test_pr_filenames(gh, username, repo):
    filenames = gh.pr_filenames(username, repo, 1)
    print(filenames)
    assert filenames


@pytest.mark.parametrize('repo', ('filabel-testrepo1', 'filabel-testrepo2', 'filabel-testrepo4'))
def test_reset_labels(gh, username, repo):
    PR_INDEX = 1
    pr = gh.pull_requests(username, repo)[PR_INDEX]
    PR_NUMBER = pr['number']
    old_labels = set()
    for label in pr['labels']:
        old_labels.add(label['name'])

    set_labels = gh.reset_labels(username, repo, PR_NUMBER, list())
    assert not set_labels
