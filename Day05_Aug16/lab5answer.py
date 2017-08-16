import googlemaps
import responses

api_key = 'Insert your api key here!'
gmaps = googlemaps.Client(api_key)
dir(gmaps)

# Define White House
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

# Which embassy is closest to the White House in meters? how far?
# Define embassies
embassies = [[38.917228,-77.0522365],
	[38.9076502, -77.0370427],
	[38.916944, -77.048739]]

print "Let's find the closest embassy to the WH."
def closest(depart, destines):
    dis = []
    for i in range(0, len(destines)):
        dis.append(gmaps.distance_matrix(depart, destines)['rows'][0]['elements'][i]['distance']['text'].split(" ")[0])
    return """This is the index of the closest place: %s
and this is the distance from the WH %skm""" % (dis.index(min(dis)), dis[dis.index(min(dis))])

print closest(whitehouse, embassies)

print "So the second one is the clostest embassy to the WH. Let's find its address"
closest_add = gmaps.reverse_geocode((embassies[1]))[0]['formatted_address']
print closest_add

print "This is the Embassy of Australia"

print """We have to find a place to have breakfast. People are normally
starving in the mornings. So, I want the closest cafe to
the embassy."""
breakfastpalce = gmaps.places_nearby(embassies[1], keyword = 'breakfast',
                min_price = 2, max_price = 5, type = 'cafe',
                rank_by = "distance")
print "Get the name of the place:"
print breakfastpalce['results'][0]['name']
print "Get the rating of the place:"
print breakfastpalce['results'][0]['rating']
print "Get the address of the place:"
print breakfastpalce['results'][0]['vicinity']

print """Now, people normally want to have some fun in the evenings.
What about going to a Nationals' game and then have a drink?
So, let's find a good place close to the Nationals' Stadium """
Nationals_Park = "1500 S Capitol St SE, Washington, DC"
bars = gmaps.places('bars near ' + Nationals_Park)
rates = []
for i in range(0, len(bars)):
    rates.append(bars['results'][i]['rating'])
print "This is the best bar: %s." % bars['results'][rates.index(max(rates))]['name']
print "And it is located at: %s" % bars['results'][rates.index(max(rates))]['formatted_address']
print "So, let's go there when we visit DC!"
