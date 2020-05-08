import flask_login
import pytest

from Register.register_db import db
from applications.login import User
from config import DevConfig
from factory import create_app


@pytest.fixture(scope='session')
def app():
    app = create_app(DevConfig)
    return app


@pytest.fixture(scope="session")
def db_connection(app):
    with app.app_context():
        db.create_all()
        """Returns session-wide initialized database"""
        yield db
        db.drop_all()


@pytest.fixture(autouse=True)
def _mock_db_connection(mocker, db_connection):
    """
    This will alter application database connection settings, once and for all the tests
    in unit tests module.
    :param mocker: pytest-mock plugin fixture
    :param db_connection: connection class
    :return: True upon successful monkey-patching
    """
    mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)
    mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)
    mocker.patch("Register.register_db.get_all", return_value={})
    return True


@pytest.fixture(autouse=True)
def _mock_file_save(mocker):
    mocker.patch("applications.mockfolder.save_file", return_value=("", "uuid_filename"))
    return True


@pytest.fixture(autouse=True)
def _setup_app_context_for_test(request, app):
    """
    Given app is session-wide, sets up a app context per test to ensure that
    app and request stack is not shared between tests.
    """
    ctx = app.app_context()
    ctx.push()
    yield  # tests will run here
    ctx.pop()


# @pytest.fixture
# def logged_in_user(request, test_user):
#     flask_login.login_user(test_user)
#     request.addfinalizer(flask_login.logout_user)


# @pytest.fixture
# def authenticated_request(app):
#     with app.test_request_context():
#         # Here we're not overloading the login manager, we're just directly logging in a user
#         # with whatever parameters we want. The user should only be logged in for the test,
#         # so you're not polluting the other tests.
#         yield flask_login.login_user(User())
