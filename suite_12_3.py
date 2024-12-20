import unittest
import module_12_3 as mod


tour_ST = unittest.TestSuite()
tour_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(mod.RunnerTest))
tour_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(mod.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tour_ST)