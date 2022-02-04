import pytest
import app_secretary
from app_secretary import *

class TestSecretary:
    def setup(self):
        print('method setUp')

    @pytest.mark.parametrize('a, b, expected_result', [(documents, '11-2', "Геннадий Покемонов"), (documents, '10006', "Аристарх Павлов"), (documents, '111', 'Нет такого номера документа')])
    def test_app_secretary(self, a, b, expected_result):
        assert app_secretary(a, b) == expected_result

    def teardown(self):
        print('method tearDown')
