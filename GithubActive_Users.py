# Generate active and suspended users from private github account

import requests
import json

githubUser = "xxxxxx"
githubPw = "xxxxxxxxx"
githubCred = (githubUser, githubPw)

usersUrl = 'https://ghdp1.devops.iconectiv.com/api/v3/users?per_page=100'
usersResp = requests.get(usersUrl, auth=githubCred)
usersJson = usersResp.json()

ctActive = 0
ctSuspended = 0
usersActive = []
usersSuspended = []

for user in usersJson:
    if user["type"] == "User":
        userResp = requests.get(user["url"], auth=githubCred)
        userJson = userResp.json()

        if userJson["suspended_at"] is None:
            usersActive.append(user["login"])
            ctActive += 1
        else:
            usersSuspended.append(user["login"])
            ctSuspended += 1

print("Total Active:    %d" % ctActive)
for u in sorted(usersActive):
    print("   %s" % u)

print("Total Suspended: %d" % ctSuspended)
for u in sorted(usersSuspended):
    print("   %s" % u)