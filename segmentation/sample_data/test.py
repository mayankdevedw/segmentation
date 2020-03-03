import os

test_params = dict()
f = open(os.getenv('TTE_CONFIG_FILE', 'annotations'))
for line in f.readlines():
    key, value = line.strip().split('=')
    test_params[key] = value
f.close()

if 'test_group' in test_params:
    if test_params['test_group'] != '\"CLOUD\"':
		print("Success")
    else:
        	print("No Tests to Run With Cloud Marker in this Split")
else:
    print("Success")
