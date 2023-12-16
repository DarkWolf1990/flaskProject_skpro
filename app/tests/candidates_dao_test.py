from app.candidates.dao.candidates_dao import CandidateDAO

import pytest


@pytest.fixture()
def candidates_dao():
    candidates_dao_instance = CandidateDAO("./data/candidates.json")
    return candidates_dao_instance


# Задаём, какие ключи ожидаем получать у кандидата
keys_should_be = {"pk", "name", "position"}


class TestCandidateDao:

    def test_get_all(self, candidates_dao):
        """Проверяем, верный ли список кандидатов возвращается"""
        candidate = candidates_dao.get_by_pk(1)
        assert (candidate["pk"] == 1), "Возвращается неправильный кандидат"
        assert set(candidate.keys()) == keys_should_be, "Неверный список"
