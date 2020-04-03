import re

funny_url = "https://play.google.com/store/apps/details?id=com.microsoft.teams&hl=en_US%fake " \
            "https://play.google.com/store/apps/details?id=com.spotify.music&hl=en_US%hi " \
            "https://play.google.com/store/apps/details?id=com.yelp.android&hl=en_US$shell"

m = re.search(r"(https.*)(%fake)", funny_url)
print(m.groups()[0])
