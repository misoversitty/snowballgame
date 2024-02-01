import unittest
from Project.Globals import NUMBER_OF_PLAYERS
from Project.Settings import Settings


class ControlSettingsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Settings.Settings()

    def test_screenSettingsLoaded(self):
        self.assertIsNotNone(self.obj.screenSettings)

    def test_controlSettingsLoaded(self):
        self.assertIsNotNone(self.obj.controlSettings)

    def test_allPlayersHaveControls(self):
        numControls = len(self.obj.controlSettings.dict)
        self.assertEqual(numControls, NUMBER_OF_PLAYERS)

if __name__ == '__main__':
    unittest.main()
