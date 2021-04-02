import requests
import unittest
import random


class TestDisk(unittest.TestCase):
    _url = 'https://cloud-api.yandex.net/v1/disk/resources'
    _token = ''  # put yoyr token here

    def setUp(self):
        self._foldername = 'Test Folder ' + str(random.randrange(1000, 2000))

    def tearDown(self):
        response = requests.delete(
            self._url,
            params={
                'path': self._foldername,
                'permanently': True
            },
            headers={
                'Authorization': f'OAuth {self._token}'
            }
        )
        pass

    def test_yadisk_api(self):
        response = requests.put(
            self._url,
            params={
                'path': self._foldername
            },
            headers={
                'Authorization': f'OAuth {self._token}'
            }
        )
        self.assertEqual(response.status_code, 201)

        response = requests.get(
            self._url,
            params={
                'path': self._foldername
            },
            headers={
                'Authorization': f'OAuth {self._token}'
            }
        )
        self.assertEqual(response.status_code, 200)

        response = requests.put(
            self._url,
            params={
                'path': self._foldername
            },
            headers={
                'Authorization': f'OAuth {self._token}'
            }
        )
        self.assertEqual(response.status_code, 409)


if __name__ == '__main__':
    unittest.main()
