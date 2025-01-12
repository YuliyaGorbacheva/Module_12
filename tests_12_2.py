import unittest
from runner_and_tournament import Tournament, Runner


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.us = Runner('Усэйн', 10)
        self.an = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}:{value}')

    def test_us_nik(self):
        t1 = Tournament(90, self.us, self.nik)
        res_t1 = t1.start()
        self.assertTrue(res_t1[2], 'Ник')

    def test_an_nik(self):
        t2 = Tournament(90, self.an, self.nik)
        res_t2 = t2.start()
        self.assertTrue(res_t2[2], 'Ник')

    def test_us_an_nik(self):
        t3 = Tournament(90, self.us, self.an, self.nik)
        res_t3 = t3.start()
        self.assertTrue(res_t3[3], 'Ник')


if __name__ == '__main__':
    unittest.main()
