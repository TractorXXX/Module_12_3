import unittest
import module_12_2_Tur as tour

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):

        """ Тест метода walk. Создаем объект класса Runner. Вызываем метод walk 10 раз.
        Сравниваем аттрибут distance этого со значением 50 """

        runner_1 = tour.Runner('Ivan')

        for i in range(10):
            runner_1.walk()

        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):

        """ Тест метода run. Вызываем метод run 10 раз. Создаем объект класса Runner.
        Сравниваем аттрибут distance этого со значением 100 """

        runner_2 = tour.Runner('Elena')

        for i in range(10):
            runner_2.run()

        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):

        """ Тест методов run и walk. Создаем два объекта класса Runner. Вызываем метод run для первого объекта 10 раз.
        Вызываем метод walk для второго объекта 10 раз. Сравниваем аттрибуты distance этих методов.
        Они не должны совпадать """

        runner_3 = tour.Runner('Petr')
        runner_4 = tour.Runner('Anna')

        for i in range(10):
            runner_3.walk()
            runner_4.run()

        self.assertNotEqual(runner_3.distance, runner_4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = tour.Runner('Усэйн', 10)
        self.run_2 = tour.Runner('Андрей', 9)
        self.run_3 = tour.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print()
            print(f'Забег {i}:')
            for key, value in j.items():
                print(f'{key}: {value.name}')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_zabeg_1(self):
        tour_90 = tour.Tournament(90, self.run_1, self.run_3)
        all_results = tour_90.start()
        self.all_results[1] = all_results
        self.assertTrue(all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_zabeg_2(self):
        tour_90 = tour.Tournament(90, self.run_2, self.run_3)
        all_results = tour_90.start()
        self.all_results[2] = all_results
        self.assertTrue(all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_zabeg_3(self):
        tour_90 = tour.Tournament(90, self.run_1, self.run_2, self.run_3)
        all_results = tour_90.start()
        self.all_results[3] = all_results
        self.assertTrue(all_results[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()