import ytmusicapi
api = ytmusicapi.YTMusic()
results = api.search("Take Care Drake")
assert len(results) > 0, "No results found for 'Take Care Drake'"
print("Successfully searched with {} results".format(len(results)))

def none():
    pass

