import json


class CandidateDAO:
    def __init__(self, path):
        """При создании экземпляра DAO нужно указать путь к файлу с данными / When you create a DAO instance,
        you must specify the path to the data file"""
        self.path = path

    def load_data(self):
        """Загружает данные из файла и возвращает обычный лист / Downloads data from a file and returns a normal
        sheet"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def get_all(self):
        """Возвращает список со всеми данными / Returns a list with all data"""
        candidates = self.load_data()
        return candidates

    def get_by_pk(self):
        """Возвращает одного кандидата по его номеру / Returns one candidate to his or her number"""
        candidates = self.load_data()
        for candidate in candidates:
            if candidate == "pk":
                return candidate
