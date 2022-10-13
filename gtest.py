import unittest
from unittest.mock import Mock , patch
from nose.tools import assert_is_not_none
from github_req import gapi

@patch('github_req.requests.get')
#class Testgapi(unittest.TestCase):
    #def Testgapi(self):
       # self.assertEqual(gapi('!'), False)
    #def Testgapi(self):
        #self.assertEqual(gapi('diyas'),False)
    
#if __name__ == '__main__':
    #print("All the test cases are wroking properly")
    #unittest.main()
def test_gapi(mock_get):
    mock_get.return_value.ok = True
    response = gapi()
    assert_is_not_none(response)
    
