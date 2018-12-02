from filabel.web import webhook_verify_signature
import hashlib
import hmac


def test_webhook_verify_signature():
    encoding = 'utf-8'
    payload = "{payload: payload}".encode(encoding)
    secret = "secret"
    signature = 'sha1=' + hmac.new(secret.encode(encoding), payload, hashlib.sha1).hexdigest()
    assert webhook_verify_signature(payload, signature, secret, encoding=encoding)

    bad_secret = "bad secret"
    failing_signature = hmac.new(bad_secret.encode(encoding), payload, hashlib.sha1).hexdigest()
    assert not webhook_verify_signature(payload, failing_signature, secret, encoding=encoding)


def test_main_page(webapp, username):
    assert username in webapp.get('/').get_data(as_text=True)


def test_proccess_webhook_ping(webapp):
    encoding = 'utf-8'
    payload = '{ "repository":{ "full_name":"name" }, "hook_id": "123" }' \
        .encode(encoding)
    secret = "secret"
    signature = hmac.new(secret.encode(encoding), payload,
                         hashlib.sha1).hexdigest()

    res = webapp.post('/',
                      headers={'X-Hub-Signature': signature,
                               'X-GitHub-Event': 'ping'},
                      data=payload,
                      content_type='application/json')
    assert res.status_code == 200

    bad_payload = '{}'
    res = webapp.post('/',
                      headers={'X-Hub-Signature': signature,
                               'X-GitHub-Event': 'ping'},
                      data=bad_payload,
                      content_type='application/json')
    assert res.status_code == 422


def test_proccess_webhook_pr(webapp, username):
    test_repo = '{}/filabel-testrepo1/custom/url'.format(username)
    encoding = 'utf-8'
    payload = "{payload: payload}".encode(encoding)
    secret = "secret"
    signature = hmac.new(secret.encode(encoding), payload,
                         hashlib.sha1).hexdigest()
    payload = '{ "action": "unknown", ' \
              '"pull_request": { "url": "' + test_repo + '"' \
              ', "number":"1", "label":"{}"},' + \
              ' "number": "1" }'

    res = webapp.post('/',
                      headers={'X-Hub-Signature': signature,
                               'X-GitHub-Event': 'pull_request'},
                      data=payload,
                      content_type='application/json')
    assert res.status_code == 202
