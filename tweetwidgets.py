import twitter



all_accounts = twitter.get_all_accounts()
if len(all_accounts) >= 1:
    account = all_accounts[0]
    tweets = twitter.get_home_timeline(account)
    for t in tweets:
        print(t.get('text'))
        print('=' * 0)
else:
    print('You don\'t have any Twitter accounts (or haven\'t given permission to access them).')