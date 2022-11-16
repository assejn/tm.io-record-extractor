import requests
import json
import csv

headers = {'User-Agent': 'describe what you are doing'}
offset = 0
seasonID = ''
mapID = ''


header = ['Player', 'PlayerID', 'Time', 'Timestamp']
with open('TA-data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    while True:
        offsetString = str(offset)
        url = 'https://trackmania.io/api/leaderboard/' + seasonID + '/' + mapID + '?offset=' + offsetString + '&length=100'
        rawData = requests.get(url, headers=headers).json()
        if 'tops' in rawData:
            tops = rawData['tops']
            if tops is not None and len(tops) > 0:
                for top in tops:
                    player = top['player']
                    playerName = player['name']
                    playerID = player['id']
                    recordTime = top['time']
                    recordTimestamp = top['timestamp']
                    playerData = [playerName, playerID, recordTime, recordTimestamp]
                    writer.writerow(playerData)

            if tops is None or len(tops) < 100:
                break
            else:
                offset = offset + 100
        else:
            break
