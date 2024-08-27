import json

with open('fingerprints.json', 'r') as file:
    fingerprints = json.load(file)

real = []

for x in fingerprints:
    if x['cname'] == [] and x['nxdomain'] == False and x['fingerprint'] == '':
        pass
    else:
        real.append(x)

with open('data.json', 'w') as json_file:
    json.dump(real, json_file, indent=5)