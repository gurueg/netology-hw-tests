import unittest
from unittest import mock
import documents as docs


class TestDocuments(unittest.TestCase):

    def create_side_function(self, array):

        def new_func(*args, **kwargs):
            value = array[self._calls_count]
            self._calls_count += 1
            return value

        return new_func

    def setUp(self):
        self._documents = [
            {
                "type": "passport",
                "number": "2207 876234",
                "name": "Василий Гупкин"
            }
        ]
        self._directories = {
            '1': ['2207 876234'],
        }
        self._calls_count = 0

    def tearDown(self):
        pass

    def test_get_doc_owner(self):
        result = docs.get_document_owner_name(self._documents, "2207 876234")
        self.assertEqual(result, "Василий Гупкин")

    def test_get_doc_owner_wrong(self):
        result = docs.get_document_owner_name(self._documents, "224")
        self.assertEqual(result, None)

    def test_get_doc_shelf(self):
        result = docs.get_document_shelf(self._directories, "2207 876234")
        self.assertEqual(result, '1')

    def test_get_doc_shelf_wrong(self):
        result = docs.get_document_shelf(self._directories, "asd")
        self.assertEqual(result, None)

    def test_add_new_shelf(self):
        side_function = self.create_side_function([
            '3'
        ])
        with mock.patch("builtins.input", side_effect=side_function) as mock1:
            result = docs.add_new_shelf(self._directories)
            self.assertEqual(result, '3')

    def test_add_document_new_shelf(self):
        side_function = self.create_side_function([
            '1234 5678',
            'passport',
            'Andrey Andreev',
            '4',
            'y'
        ])

        with mock.patch("builtins.input", side_effect=side_function) as mock1:
            self.assertEqual(
                docs.add_document(self._documents, self._directories),
                True
            )
            self.assertEqual(docs.get_document_owner_name(
                self._documents, '1234 5678'),
                'Andrey Andreev'
            )
            self.assertEqual(
                docs.get_document_shelf(self._directories, '1234 5678'),
                '4'
            )

    def test_add_document_old_shelf(self):
        side_function = self.create_side_function([
            '1234 5678',
            'passport',
            'Andrey Andreev',
            '1'
        ])

        with mock.patch("builtins.input", side_effect=side_function) as mock1:
            self.assertEqual(
                docs.add_document(self._documents, self._directories),
                True
            )
            self.assertEqual(docs.get_document_owner_name(
                self._documents, '1234 5678'),
                'Andrey Andreev'
            )
            self.assertEqual(
                docs.get_document_shelf(self._directories, '1234 5678'),
                '1'
            )

    def test_delete_document(self):
        side_function = self.create_side_function([
            '2207 876234'
        ])

        with mock.patch("builtins.input", side_effect=side_function) as mock1:
            self.assertEqual(
                docs.delete_document(self._documents, self._directories),
                True
            )
            self.assertEqual(
                docs.get_document_owner_name(self._documents, '2207 876234'),
                None
            )
            self.assertEqual(
                docs.get_document_shelf(self._directories, '2207 876234'),
                None
            )

    def test_move_document(self):
        side_function = self.create_side_function([
            '2207 876234',
            '2',
            'y'
        ])

        with mock.patch("builtins.input", side_effect=side_function) as mock1:
            self.assertEqual(docs.move_document(self._directories), True)
            self.assertEqual(
                docs.get_document_shelf(self._directories, '2207 876234'),
                '2'
            )


if __name__ == '__main__':
    unittest.main()
