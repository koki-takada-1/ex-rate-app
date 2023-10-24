import unittest
import tested

class TestSidebar(unittest.TestCase):
    def test_1(self):
        leap_normal = ['うるう年', '平年', '平年', '平年', 'うるう年', '平年', '平年', '平年', 'うるう年', '平年', '平年', '平年', 'うるう年', '平年', '平年', '平年', 'うるう年', 
         '平年', '平年', '平年', 'うるう年', '平年', '平年', '平年', 'うるう年', '平年', '平年', '平年', 'うるう年', '平年', '平年', '平年', 'うるう年', 
         '平年', '平年', '平年', 'うるう年', '平年', '平年', '平年', 'うるう年', '平年', '平年', '平年', 'うるう年', '平年', '平年', '平年', 'うるう年']
        leap_normal = [i == 'うるう年' for i in leap_normal]
        years = [i for i in range(2000,2049)]
        for i in range(len(years)):
            self.assertEqual(tested.leep_year(i),leap_normal[i],'失敗')

if __name__ == '__main__':
    unittest.main()