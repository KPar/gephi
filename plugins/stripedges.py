import json
import os


#########################################
# Parameters

FILE_NAME = 'police.json'

with open(FILE_NAME) as f:
	json_dict = json.load(f)

count = 0	
for i, node in enumerate(json_dict['nodes']):
	if node['size'] < 100.:
		# print('deleting ', node)
		del json_dict['nodes'][i]
		count += 1
	
del json_dict['edges']

print('Deleted %d / %d nodes' % (count, len(json_dict['nodes']) + count))

base, ext = os.path.splitext(FILE_NAME)
output_filename = base + '_stripped' + ext

with open(output_filename, 'w') as f:
	f.write(json.dumps(json_dict, indent = 4))