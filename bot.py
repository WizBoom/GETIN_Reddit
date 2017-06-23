import praw
import time

SLEEP_TIME = 7200
while True:
	r = praw.Reddit('getin_forum')
	sr = r.subreddit('GETIN_Eve')

	contributorUsernames = []
	for cont in sr.contributor():
		contributorUsernames.append(cont)

	modUsernames = []
	for mod in sr.moderator():
		modUsernames.append(mod)

	redditUsernames = ['KwG_TwiTCh','WizBoom','TheDreadfulSagittary']
	whitelistUsernames = ['GETINBot']
	newUsernames = []
	removeUsernames = []

	#Check who needs to be added
	for name in contributorUsernames:
		if name not in redditUsernames and name not in whitelistUsernames:
			removeUsernames.append(name)

	#Check who needs to get removed
	for name in redditUsernames:
		if name not in contributorUsernames:
			newUsernames.append(name)

	#Add people
	for redditor in newUsernames:
		sr.contributor.add(redditor)

	#Remove people
	for redditor in removeUsernames:
		sr.contributor.remove(redditor)
		#Check if its a mod
		if redditor in modUsernames:
			sr.moderator.remove(redditor)

	print('ADDED')
	for name in newUsernames:
		print(name)

	print('\nREMOVED')
	for name in removeUsernames:
		print(name)

	time.sleep(SLEEP_TIME)

