import praw
import time
import logging

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

	# logging setup
	handler = logging.StreamHandler()
	handler.setLevel(logging.INFO)
	logger = logging.getLogger('prawcore')
	logger.setLevel(logging.INFO)
	logger.addHandler(handler)
	logging.basicConfig(filename='log.log',level=logging.INFO)

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
		#Log
		logger.info(users[userIndex][0] + ", " + users[userIndex][1] + " added!")


	#Remove people
	for redditor in removeUsernames:
		sr.contributor.remove(redditor)
		#Check if its a mod
		if redditor in modUsernames:
			sr.moderator.remove(redditor)
		logger.info(str(redditor) + " removed!")

	time.sleep(SLEEP_TIME)

