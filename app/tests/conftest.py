import pytest
import run


#  создаём фикстуру для тестирования всех вьюшек (main, candidates, vacancies) /
#  create a fixture for testing all the vests (main, candidates, vacancies)
@pytest.fixture()
def test_client():
    app = run.app
    return app.test_cient()