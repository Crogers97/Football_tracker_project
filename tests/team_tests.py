import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Celtic", 25)

    def test_team_has_name(self):
        self.assertEquals("Celtic", self.team.name)

    def test_team_has_points(self):
        self.assertEquals(25, self.team.points)