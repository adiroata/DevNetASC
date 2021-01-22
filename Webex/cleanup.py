from webexteamssdk import WebexTeamsAPI
import os

api = WebexTeamsAPI(
    access_token=os.environ.get("WEBEX_TOKEN"))
# print(os.environ.get("WEBEX_TOKEN"))

# BEFORE
print("-"*40 + " BEFORE " + "-"*40)

### GET TEAM INFO ###
print("-"*40 + " Teams " + "-"*40)
teams = api.teams.list()
for team in teams:
    print(team.name)

#### ROOMS #####
print("-"*40 + " Rooms " + "-"*40)
rooms = api.rooms.list()
for room in rooms:
    print(room.title)


# CLEANUP
for room in rooms:
    if getattr(room, "title") == "DevNet Dungeon":
        api.rooms.delete(getattr(room, "id"))

for team in teams:
    if getattr(team, "name") == "DevNet Champs":
        api.teams.delete(getattr(team, "id"))


# AFTER
print("-"*40 + " AFTER " + "-"*40)

### GET TEAM INFO ###
print("-"*40 + " Teams " + "-"*40)
teams = api.teams.list()
for team in teams:
    print(team.name)

#### ROOMS #####
print("-"*40 + " Rooms " + "-"*40)
rooms = api.rooms.list()
for room in rooms:
    #print(room.title)
    print(room)

