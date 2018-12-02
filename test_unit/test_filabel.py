import pytest


def test_defined_labels(filabel):
    assert filabel.defined_labels != None


@pytest.mark.parametrize('repo', ('filabel-testrepo1', 'filabel-testrepo2', 'filabel-testrepo4'))
def test_run_pr(gh, filabel, username, repo):
    prs = gh.pull_requests(username, repo, filabel.state, filabel.base)
    res = filabel.run_pr(username, repo, prs[1])
    assert res != None


@pytest.mark.parametrize('repo', ('filabel-testrepo1', 'filabel-testrepo3', 'filabel-testrepo4'))
def test_run_repo(gh, filabel, username, repo):
    prs = filabel.run_repo(username + "/" + repo)
    assert prs
