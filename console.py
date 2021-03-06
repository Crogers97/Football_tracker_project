import pdb
from models.team import Team
from models.fixture import Fixture
import repositories.team_repositories as team_repository 
import repositories.fixture_repositories as fixture_repositories 

team1= Team("Aberdeen", 8)
team_repository.save(team1)
team2= Team("Celtic", 10)
team_repository.save(team2)
team3= Team("Dundee", 3)
team_repository.save(team3)
team4= Team("Dundee United", 11)
team_repository.save(team4)
team5= Team("Hearts", 15)
team_repository.save(team5)
team6= Team("Hibs", 15)
team_repository.save(team6)
team7= Team("Livingston", 4)
team_repository.save(team7)
team8= Team("Motherwell", 14)
team_repository.save(team8)
team9= Team("Rangers", 16)
team_repository.save(team9)
team10= Team("Ross County", 3)
team_repository.save(team10)
team11= Team("St Johnstone", 6)
team_repository.save(team11)
team12= Team("St Mirren", 7)
team_repository.save(team12)

team_repository.select_all()

fixture1= Fixture(team9, team7,"3-0","Home Win")
fixture_repositories.save(fixture1)
fixture2= Fixture(team3,team12,"2-2", "Draw")
fixture_repositories.save(fixture2)
fixture3= Fixture(team10, team11,"0-0", "Draw")
fixture_repositories.save(fixture3)
fixture4= Fixture(team5, team2, "2-1", "Home Win")
fixture_repositories.save(fixture4)

fixture5= Fixture(team8, team6, "2-3", "Away Win")
fixture_repositories.save(fixture5)
fixture6= Fixture(team1, team4, "2-0", "Home Win")
fixture_repositories.save(fixture6)

fixture7= Fixture(team12, team5, "1-2", "Away Win")
fixture_repositories.save(fixture7)
fixture8= Fixture(team4, team9, "1-0", "Home Win")
fixture_repositories.save(fixture8)

fixture9= Fixture(team11, team8, "1-1", "Draw")
fixture_repositories.save(fixture9)
fixture10= Fixture(team7, team1, "1-2", "Away Win")
fixture_repositories.save(fixture10)
fixture11= Fixture(team6, team10, "3-0", "Home Win")
fixture_repositories.save(fixture11)
fixture12= Fixture(team2, team3, "6-0", "Home Win")
fixture_repositories.save(fixture12)

fixture13= Fixture(team7, team8, "1-2", "Away Win")
fixture_repositories.save(fixture13)
fixture14= Fixture(team2, team12, "6-0", "Home Win")
fixture_repositories.save(fixture14)

fixture15= Fixture(team11, team4, "0-1", "Away Win")
fixture_repositories.save(fixture15)
fixture16= Fixture(team10, team9, "2-4", "Away Win")
fixture_repositories.save(fixture16)
fixture17= Fixture(team5, team1, "1-1", "Draw")
fixture_repositories.save(fixture17)
fixture18= Fixture(team3, team6, "2-2", "Draw")
fixture_repositories.save(fixture18)

fixture19= Fixture(team8, team3, "1-0", "Home Win")
fixture_repositories.save(fixture19)
fixture20= Fixture(team6, team7, "2-0", "Home Win")
fixture_repositories.save(fixture20)
fixture21= Fixture(team4, team5, "0-2", "Away Win")
fixture_repositories.save(fixture21)

fixture22= Fixture(team12, team11, "0-0", "Draw")
fixture_repositories.save(fixture22)
fixture23= Fixture(team1, team10, "1-1", "Draw")
fixture_repositories.save(fixture23)
fixture24= Fixture(team9, team2, "1-0", "Home Win")
fixture_repositories.save(fixture24)

fixture25= Fixture(team12, team4, "0-0", "Draw")
fixture_repositories.save(fixture25)
fixture26= Fixture(team8, team1, "2-0", "Home Win")
fixture_repositories.save(fixture26)
fixture27= Fixture(team3, team7, "0-0", "Draw")
fixture_repositories.save(fixture27)
fixture28= Fixture(team2, team10, "3-0", "Home Win")
fixture_repositories.save(fixture28)
fixture29= Fixture(team11, team9, "1-2", "Away Win")
fixture_repositories.save(fixture29)

fixture30= Fixture(team5, team6, "0-0", "Draw")
fixture_repositories.save(fixture30)

fixture31= Fixture(team10, team5, "2-2", "Draw")
fixture_repositories.save(fixture31)
fixture32= Fixture(team6, team12, "2-2", "Draw")
fixture_repositories.save(fixture32)
fixture33= Fixture(team1, team11, "0-1", "Away Win")
fixture_repositories.save(fixture33)

fixture34= Fixture(team9, team8, "1-1", "Draw")
fixture_repositories.save(fixture34)
fixture35= Fixture(team7, team2, "1-0", "Home Win")
fixture_repositories.save(fixture35)
fixture36= Fixture(team4, team3, "1-0", "Home Win")
fixture_repositories.save(fixture36)

fixture37= Fixture(team8, team10, "2-1", "Home Win")
fixture_repositories.save(fixture37)
fixture38= Fixture(team5, team7, "3-0", "Home Win")
fixture_repositories.save(fixture38)
fixture39= Fixture(team3, team9, "0-1", "Away Win")
fixture_repositories.save(fixture39)

fixture40= Fixture(team6, team11, "1-0", "Home Win")
fixture_repositories.save(fixture40)
fixture41= Fixture(team2, team4, "1-1", "Draw")
fixture_repositories.save(fixture41)
fixture42= Fixture(team12, team1, "3-2", "Home Win")
fixture_repositories.save(fixture42)


fixture_repositories.select_all()


pdb.set_trace()

