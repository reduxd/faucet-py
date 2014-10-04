import os
import sys
import getopt
import collections
import requests
import json

api = 'https://drip.fm/api/'

def args(args):
	if len(args) != 3:
		print('[!] Usage: faucet.py <drip url> <format> <output>')
		sys.exit(1)

	arguments = collections.namedtuple('Args', ['url', 'format', 'output'])

	url = args[0]
	format = args[1]
	output = args[2]

	thisArgs = arguments(url, format, output)

	return thisArgs

# attempt to do auth
def auth(email, passw):
	data = {"email": email, "password": passw}
	auth = drip.post(api + 'users/login', data=json.dumps(data))
	authJson = auth.json()

	if not authJson['firstname']:
		print('[!] Invalid credentials, exiting...')
		sys.exit(1)

	name = authJson['firstname'] + ' ' + authJson['lastname']
	print('[!] Logged in as ' + name)

# parse link
def parse(link):
	parsed = link[16:]

	parse = drip.get(api + 'creatives/' + parsed);
	parseJson = parse.json()

	if parseJson['unlocked']:
		release = collections.namedtuple('Release', ['artist', 'title', 'label', 'creativeId', 'releaseId'])

		artist = parseJson['artist']
		title = parseJson['title']
		label = parseJson['label_name']
		creativeId = parseJson['creative_id']
		releaseId = parseJson['id']

		thisRelease = release(artist, title, label, creativeId, releaseId)
		return thisRelease

	print('')
	print('[!] Release not unlocked, exiting...')
	sys.exit(1)

# print subscriptions
def listsMems():
	auth = drip.post(api + 'users/login', data=json.dumps({'email': '', 'password': ''}))
	authJson = auth.json()
	
	print('    - Subscriptions:')
	for membership in authJson['memberships']:
		name = membership['creative']['name']

		print('      - ' + name)

# handle release download
def downloadZip(cId, rId, format, output):
	with open(str(output), 'wb') as handle:
		response = drip.get(api + 'creatives/' + str(cId) + '/releases/' + str(rId) + '/download?release_format=' + format, stream=True)

		if not response.ok:
			print('[!] Something went wrong, exiting...')
			sys.exit(1)

		for block in response.iter_content(1024):
			if not block:
				break

			handle.write(block)

		print('')
		print('[!] Download successful!')

# main code
if __name__ == "__main__":
	# script info
	print('[!] faucet.py by reduxd')
	print('[!] drip.fm download client')
	print('[!] http://github.com/reduxd/faucet-py')
	print('')

	processedArgs = args(sys.argv[1:])

	url = processedArgs.url
	format = processedArgs.format
	output = processedArgs.output

	# this is the user session
	drip = requests.session()

	# make sure we have credentials
	if 'FUSER' and 'FPASS' in os.environ:
		email = os.environ.get('FUSER', 'email')
		passw = os.environ.get('FPASS', 'pass')
		auth(email, passw)
	else:
		print('[!] No credentials found, exiting...')
		sys.exit(1)

	listsMems()

	release = parse(url)

	print('')
	print('[!] Processing release:')
	print('      - ' + release.title + ' by ' + release.artist)
	print('      - ' + release.label)

	downloadZip(release.creativeId, release.releaseId, format, output)
