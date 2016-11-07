## PS 11

## Please put your name here!
# Kendra Repo
# import statements
import requests
import json


# This is a function we've provided for you so you can print stuff in a pretty,
# easy-to-read way.
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


#####

## Making a tag recommender, using the Flickr API!

# In this problem, we'll walk you through steps you need to take to make a tag
# recommender, but we won't be providing you code. You'll use the documentation
# we'll copy in here, and the code you've seen in lecture to deal with Flickr
# and other API requests, to translate the English into Python and make your
# program work.
# Go through step by step. You may want to look back at Problem Set 9
# to remind yourself of the steps to go through when dealing with APIs
# and making requests for data, and Problem Set 6 and Hackpad exercises
# can remind you of how to deal with nested data.

###
flickr_key = "0f1b69b4cf2cfed70a7300a461e7003d" #paste you flickr key here

if not flickr_key:
    flickr_key = raw_input("Enter your flickr API key, or paste it in the .py file to avoid this prompt in the future: \n>>")

# Useful function definitions

def flickrREST(baseurl = 'https://api.flickr.com/services/rest/',
    method = 'flickr.photos.search',
    api_key = flickr_key,
    format = 'json',
    extra_params={}):
    d = {}
    d['method'] = method
    d['api_key'] = api_key
    d['format'] = format
    for k in extra_params:
        d[k] = extra_params[k]
    return requests.get(baseurl, params = d)


## Here's another example call to flickrREST below -- note that you have to pass in
## a new params dictionary to get the parameters/param values you want in your request!
## uncomment the following line to try it out, or edit it, to think about how you
## can make a call to this function like you've done already, and how/why you might
## make a different call to this function.

#print flickrREST(extra_params = {'tags':'mountains', 'per_page':10}).url

## Remember that for the Flickr API, you have to remove the bit at the beginning and end
## that isn't json: "jsonFlickrApi("" at the beginning, and ")" at the end.
## So once you get a response string, use this function to do that, to get a response string that
## you can pass to json.loads():
def fix_flickr_resp(response_string):
	return response_string[len("jsonFlickrApi("):-1]

## Let's start making the tag recommender! This has several steps.
## HINT: Thinking about the process from PS 9, the Flickr examples, and
##       the structure we went through in section last week, will help!

# [PROBLEM 1] Ask the user to input a tag.
tag = raw_input('Give me a tag to look for')

# [PROBLEM 2] From flickr, search on that tag, getting back at least 50 photos that have that tag. 
# Extract the contents of the response as a python dictionary, using json.loads
s = flickrREST(extra_params = {'tags': tag, 'per_page': 50})
w = fix_flickr_resp(s.text)
final = json.loads(w)

# [PROBLEM 3] Extract each of the photo ids from that response, making a list of all of them.
ids = []
for a in final['photos']['photo']:
    ids.append(a['id'])

# [PROBLEM 4] For each of the photo ids, make a request to the flickr API
#    method flickr.photos.getInfo (this is like the flickr.photos.search in flickrREST)
#    -- it describes the place to go to get the data within the flickr service.
#    See documentation at https://www.flickr.com/services/api/flickr.photos.getInfo.html.
r = {}
for c in ids:
    y = flickrREST(method = 'flickr.photos.getInfo', extra_params = {'photo_id': c})
    time = fix_flickr_resp(y.text)
    itstime = json.loads(time)
    r[c] = itstime
print pretty(r)
# Extract the tags used on each photo, and accumulate frequencies
#    with which each tag occurs across all those photos you found when you searched.

# [PROBLEM 5] Sort the tags based on how often they were used on the photos
tags = []
for f in r:
    taginfo = r[f]['photo']['tags']['tag']
    for h in taginfo:
        tags.append(h['_content'])

new_freq = {}
for freq in tags:
    if freq not in new_freq:
        new_freq[freq] = 1
    else:
        new_freq[freq] += 1
print pretty(new_freq)

# [PROBLEM 6] Output (print, for the user to see) the five tags (other than the searched on tag)
#    that were used most frequently. HINT 1: take a slice of the sorted list.
#    HINT 2: skip the first element in the sorted list. That will be the tag
#    the user typed in, since all the photos have that tag.
l = sorted(new_freq, key = lambda x: new_freq[x], reverse = True)
output = l[1:6]
print "done"
