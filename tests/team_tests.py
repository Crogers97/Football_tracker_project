import unittest
from models.team import Team
from models.fixture import Fixture
import repositories.fixture_repositories as fixture_repositories

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Celtic", 25)

    def test_team_has_name(self):
        self.assertEquals("Celtic", self.team.name)

    def test_team_has_points(self):
        self.assertEquals(25, self.team.points)
    

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.fixture = Fixture(team9, team7,"3-0","Home Win")
    
    