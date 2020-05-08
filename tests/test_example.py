import io

import flask_login
import pytest
from flask import json
from flask import url_for

# def test_app(client):
#     res = client.get(url_for('foo.hello_world'))
#     assert res.status_code == 200
from applications.login import User


def test_program():
    # this test is using mocked database connection.
    assert True


class TestCase:
    def test_create(self, client):
        res = client.post(url_for('cat.create_cat'))
        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == {'msg': 'create success'}
        res = client.post(url_for('cat.create_cat'))
        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == {'msg': 'create success'}
        res = client.get(url_for('cat.get_cats'))
        data = json.loads(res.data)
        assert data == {'count': 2}

    def test_upload(self, client):
        data = {'file': (io.BytesIO(b"abcdef"), 'test.jpg')}
        res = client.post(
            url_for('file.upload'), data=data, follow_redirects=True,
            content_type='multipart/form-data')
        data = json.loads(res.data)
        assert data == {'fn': 'uuid_filename'}
