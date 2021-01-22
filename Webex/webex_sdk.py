from webexteamssdk import WebexTeamsAPI
import os

api = WebexTeamsAPI(
    access_token=os.environ.get("WEBEX_TOKEN"))
# print(os.environ.get("WEBEX_TOKEN"))

### GET TEAM INFO ###

teams = api.teams.list()

for team in teams:
    print(team)
    if getattr(team, "name") != "DevNet Champs":
        create_team = api.teams.create("DevNet Champs")
        teamId = getattr(create_team, "id")
    else:
        teamId = team.id


###### PEOPLE #####
# print(api.people.me())
# print(api.people.list())
# api.people.create(emails=["John.Doe@company.com"], displayName="John Doe", firstName="John",
#                   lastName="Doe", roles=['Y2lzY29zcGFyazovL3VzL1JPTEUvaWRfZnVsbF9hZG1pbg'])

# #### ROLES #####
# roles = api.roles.list()
# # print(roles)
# for role in roles:
#     print(role)


#### ROOMS #####
rooms = api.rooms.list()
evaluator = False
for room in rooms:
    if room.title == "DevNet Dungeon":
        evaluator = True
        roomId = room.id

if evaluator == False:
    new_room = api.rooms.create("DevNet Dungeon", teamId=teamId)
    roomId = new_room.id


#### MESSAGES ####
api.messages.create(roomId, text="Welcome to the DevNet Dungeon")

# CLEANUP
# for room in rooms:
#     if getattr(room, "title") == "DevNet Dungeon":
#         api.rooms.delete(getattr(room, "id"))

# for team in teams:
#     if getattr(team, "name") == "DevNet Champs":
#         api.teams.delete(getattr(team, "id"))