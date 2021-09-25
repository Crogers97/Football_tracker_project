import pdb
from models.team import Team

import repositories.team_repositories as team_repository 

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
team8= Team("MotherWell", 8)
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

pdb.set_trace()

