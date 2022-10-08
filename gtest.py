import unittest
from github_req import gapi

class Testgapi(unittest.TestCase):
    def Testgapi(self):
        self.assertEqual(gapi('!'), False)
    def Testgapi(self):
        self.assertEqual(gapi('diyas'),False)
    
if __name__ == '__main__':
    print("All the test cases are wroking properly")
    unittest.main()