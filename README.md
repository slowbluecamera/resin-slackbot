# resin-slackbot

`resin-slackbot`, on the whole, likes you.

(TODO: intro)

(DRAFTY MCDRAFTFACE NOTES BELOW)

## how it works

## initial deployment

get raspberry pi set up as a resin.io management

1. get a raspberry pi
2. creat a resin account
3. load the os image onto your raspberry pi
4. confirm that resin is managing your pi

get a bot token for your slack instance
1.
2.
3

deploy slackbot to you raspberry pi
5. set the SLACK_API_TOKEN fo token
4. set a remote for your git repo
5. push to the new remote

talk to your new robot friend

## customizing your slackbot

## testing & deploying with travis.ci

1. set up the build to be build by travis
2. encrypt a deploy key (?) to your raspberry pi (?)

Now when you push to any branch, travis will run test and lint checks.
And when you push to master, it will deploy to the raspberry pi

