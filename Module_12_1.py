import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walker = runner.Runner('Пешеход')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        rn = runner.Runner('Бегун')
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    def test_challenge(self):
        walker = runner.Runner('Пешеход')
        rn = runner.Runner('Бегун')
        for i in range(10):
            walker.walk()
            rn.run()
        self.assertNotEqual(walker.distance, rn.distance)


if __name__ == '__main__':
    unittest.main()
