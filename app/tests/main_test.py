class TestMain:
    def test_root_status(self, test_client):
        """
        Проверяем, получается ли нужный статус-код / Checking to see if the required status code
        :param test_client:
        :return:
        """
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус код всех постов неверен"

    def test_root_content(self, test_client):
        reponse = test_client.get('/', follow_redirects=True)
        assert "Это главная страничка" in reponse.data.decode("utf-8")

