import unittest
from runner_and_tournament import Tournament, Runner
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'')
    def test_walk(self):
        walker = runner.Runner('Пешеход')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        rn = runner.Runner('Бегун')
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        walker = runner.Runner('Пешеход')
        rn = runner.Runner('Бегун')
        for i in range(10):
            walker.walk()
            rn.run()
        self.assertNotEqual(walker.distance, rn.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_us_nik(self):
        t1 = Tournament(90, self.us, self.nik)
        res_t1 = t1.start()
        self.assertTrue(res_t1[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_an_nik(self):
        t2 = Tournament(90, self.an, self.nik)
        res_t2 = t2.start()
        self.assertTrue(res_t2[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_us_an_nik(self):
        t3 = Tournament(90, self.us, self.an, self.nik)
        res_t3 = t3.start()
        self.assertTrue(res_t3[3], 'Ник')


if __name__ == '__main__':
    unittest.main()
