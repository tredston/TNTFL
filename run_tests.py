import argparse
import os
import re
import sys
import unittest

import tntfl.test.test_achievements as test_achievements
import tntfl.test.test_game_store as test_game_store
import tntfl.test.test_ladder as test_ladder
import tntfl.test.test_pundit as test_pundit
import tntfl.test.test_json as test_json
import tntfl.test.test_deployment as test_deployment
import tntfl.test.transforms.test_achievement as test_achievement
import tntfl.test.transforms.test_belt as test_belt
import tntfl.test.transforms.test_elo as test_elo
import tntfl.test.transforms.test_rank as test_rank


def clearCache():
    print('Clearing cache')
    cacheFile = '^\.cache\.'
    for f in os.listdir('.'):
        if re.search(cacheFile, f):
            os.remove(f)


def unitTestSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.findTestCases(test_achievements))
    test_suite.addTest(unittest.findTestCases(test_game_store))
    test_suite.addTest(unittest.findTestCases(test_ladder))
    test_suite.addTest(unittest.findTestCases(test_pundit))
    test_suite.addTest(unittest.findTestCases(test_json))
    test_suite.addTest(unittest.findTestCases(test_achievement))
    test_suite.addTest(unittest.findTestCases(test_belt))
    test_suite.addTest(unittest.findTestCases(test_elo))
    test_suite.addTest(unittest.findTestCases(test_rank))
    return test_suite


def integrationTestSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.findTestCases(test_deployment))
    return test_suite


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--integration', dest='runIntegration', action='store_true')
    parser.set_defaults(runIntegration=False)
    args = parser.parse_args()

    runner = unittest.TextTestRunner()

    clearCache()
    print('Running unit tests:')
    result = runner.run(unitTestSuite())

    if len(result.errors) == 0 and len(result.failures) == 0 and args.runIntegration:
        clearCache()
        print('Running integration tests:')
        result = runner.run(integrationTestSuite())

    clearCache()

    ok = len(result.errors) == 0 and len(result.failures) == 0
    sys.exit(not ok)
