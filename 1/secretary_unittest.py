import app_secretary
import unittest
from unittest.mock import patch


class TestSecretary(unittest.TestCase):
    def setUp(self):
        print('Testing secretary functions..')

    def test_check_document_existance(self):
        self.assertEqual(app_secretary.check_document_existance('11-2'), True)
        self.assertEqual(app_secretary.check_document_existance('x'), False)

    @patch('builtins.input')
    def test_get_doc_owner_name(self, user_input):
        user_input.side_effect = ['2207 876234']
        self.assertEqual(app_secretary.get_doc_owner_name(), 'Василий Гупкин')

    def test_get_all_doc_owners_names(self):
        self.assertEqual(app_secretary.get_all_doc_owners_names(),
                         {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"})

    def test_remove_doc_from_shelf(self):
        app_secretary.remove_doc_from_shelf('10006')
        self.assertEqual(app_secretary.directories['2'], [])

    @patch('builtins.input')
    def test_delete_doc(self, user_input):
        user_input.side_effect = ['11-2']
        self.assertEqual(app_secretary.delete_doc(), ('11-2', True))

    @patch('builtins.input')
    def test_move_doc_to_shelf(self, user_input):
        user_input.side_effect = ['11-2', '3']
        app_secretary.move_doc_to_shelf()
        self.assertEqual(app_secretary.directories['3'], ['11-2'])

    def test_show_document_info(self):
        self.assertEqual(app_secretary.show_document_info('10006'), 'insurance "10006" "Аристарх Павлов"')

    def tearDown(self):
        print('Testing complete!')