import json

with open("suburbs.json") as json_file:
    data = json.load(json_file)
data
result = {}
for key in data['data']:
    if key['state'] not in result:
        result[str(key['state'])] = []
    else:
        result[key['state']].append(str(key['suburb']))

for key in result:
    result[key].sort()
result

with open("suburb_list.json", 'w') as outfile:
    json.dump(result,outfile)
