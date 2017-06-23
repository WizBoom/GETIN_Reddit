import praw
import time

SLEEP_TIME = 7200
while True:
	print('\nRunning script...')
	r = praw.Reddit('getin_forum')
	sr = r.subreddit('GETIN_Eve')

	contributorUsernames = []
	for cont in sr.contributor():
		contributorUsernames.append(cont)

	modUsernames = []
	for mod in sr.moderator():
		modUsernames.append(mod)

	users = [ ['WizBoom', 'Alex Kommorov'] ]

	whitelistUsernames = ['GETINBot']

	redditUsers	= [i[0] for i in users]
	newUsernames = []
	removeUsernames = []

	#Check who needs to be removed
	for name in contributorUsernames:
		if name not in redditUsers and name not in whitelistUsernames:
			removeUsernames.append(name)

	#Check who needs to get added
	for name in redditUsers:
		if name not in contributorUsernames:
			newUsernames.append(name)

	#Add people
	for index in range(len(newUsernames)):
		userIndex = redditUsers.index(newUsernames[index])
		#Add
		sr.contributor.add(users[userIndex][0])
		#Give flair
		sr.flair.set(users[userIndex][0], users[userIndex][1])

	#Remove people
	for redditor in removeUsernames:
		sr.contributor.remove(redditor)
		#Check if its a mod
		if redditor in modUsernames:
			sr.moderator.remove(redditor)

	print('\nADDED')
	if len(newUsernames) == 0:
		print('No new entries')
	else:
		for name in newUsernames:
			print(name)

	print('\nREMOVED')
	if len(removeUsernames) == 0:
		print('No new entries')
	else:
		for name in removeUsernames:
			print(name)

	time.sleep(SLEEP_TIME)

