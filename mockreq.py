import json
import unittest
import unittest.mock
from unittest.mock import patch
from unittest import mock
from unittest.mock import Mock
from urllib import response
from github_req import gapi

class Testgapi(unittest.TestCase):
    @patch("github_req.gapi", return_value=[any])
    def test_mockapi(self , mock_repo):
        response_file = open('./response.json')
        repo_response = json.load(response_file)
        mock_repo.return_value = Mock(status_code = 200)
        mock_repo.return_value.json = repo_response
        response = gapi('Diya1201')
        self.assertEqual(response.json[0]['name'],"Rayft")
        response_file.close()

if __name__ == '__main__':
    print('The tests are running')
    unittest.main(exit=False)


