import os
import re
import unittest

import tntfl.test.test_achievements as test_achievements
import tntfl.test.test_game_store as test_game_store
import tntfl.test.test_ladder as test_ladder
import tntfl.test.test_pundit as test_pundit
import tntfl.test.test_scripts as test_scripts
import tntfl.test.test_deployment as test_deployment
import tntfl.test.transforms as transforms


def clearCache():
    print 'Clearing cache'
    cacheFile = '.cache.*'
    for f in os.listdir('.'):
        if re.search(cacheFile, f):
            os.remove(f)


def unitTestSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.findTestCases(test_achievements))
    test_suite.addTest(unittest.findTestCases(test_game_store))
    test_suite.addTest(unittest.findTestCases(test_ladder))
    test_suite.addTest(unittest.findTestCases(test_pundit))
    test_suite.addTest(unittest.findTestCases(transforms))
    return test_suite


def functionalTestSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.findTestCases(test_scripts))
    return test_suite


def integrationTestSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.findTestCases(test_deployment))
    return test_suite


if __name__ == "__main__":
    clearCache()
    runner = unittest.TextTestRunner()

    print 'Running unit tests:'
    result = runner.run(unitTestSuite())

    if len(result.errors) == 0 and len(result.failures) == 0:
        print 'Running functional tests:'
        result = runner.run(functionalTestSuite())

    if len(result.errors) == 0 and len(result.failures) == 0:
        print 'Running integration tests:'
        result = runner.run(integrationTestSuite())
