#!/usr/bin/env python3
# @Author:	Leeroy P. Williams
# @Date:	21/06/19
# @Desc:	Use the following script in order to get a github users email address.
#			The only requirement is that you will need to know the [users] user-name.
#			Should you want to contant them.

import requests
import argparse, os

help_message = """
	This program is used for finding the email address belonging to a github user's account.
	Provided that the user name provided is valid and the github user enabled their email,
	address to be publicly visible.
"""

parser = argparse.ArgumentParser(description=help_message)
parser.add_argument("--username", "-u", help="provide the github users username")
args = parser.parse_args()
url = "https://api.github.com/users/{}/events".format(args.username)

def main():

    getEmail(args.username)

def getEmail(name):
	"""
		This function is responsible for traversing the API to find the user email address.
	"""
	res = requests.get(url)
	data = res.json()			# The data found within the github API is stored as JSON content, so we need to decode it

	for i in data:
		if "payload" in i:
			for j in i["payload"]:
				if j == "commits":
					user_email = i["payload"][j][0]["author"]["email"]	# Print  the email address located in the dictionary

	email_file = open("email_address.txt", mode='a')
	email_file.write(user_email)
	email_file.write('\n')

if __name__ == "__main__":
	main()