import pdb
from models.team import Team
from models.fixture import Fixture
import repositories.team_repositories as team_repository 
import repositories.fixture_repositories as fixture_repositories 

team1= Team("Aberdeen", 1)
team_repository.save(team1)
team2= Team("Celtic", 2)
team_repository.save(team2)
team3= Team("Dundee", 3)
team_repository.save(team3)
team4= Team("Dundee United", 4)
team_repository.save(team4)
team5= Team("Hearts", 5)
team_repository.save(team5)
team6= Team("Hibs", 6)
team_repository.save(team6)
team7= Team("Livingston", 7)
team_repository.save(team7)
team8= Team("Motherwell", 8)
team_repository.save(team8)
team9= Team("Rangers", 9)
team_repository.save(team9)
team10= Team("Ross County", 10)
team_repository.save(team10)
team11= Team("St Johnstone", 11)
team_repository.save(team11)
team12= Team("St Mirren", 12)
team_repository.save(team12)

team_repository.select_all()

fixture1= Fixture(team1, team2,"2-0","H Win")
fixture_repositories.save(fixture1)
fixture2= Fixture(team9,team11,"0-2", "A Win")
fixture_repositories.save(fixture2)
fixture3= Fixture(team8, team5,"0-0", "Draw")
fixture_repositories.save(fixture3)

fixture_repositories.select_all()


pdb.set_trace()

