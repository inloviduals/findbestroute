import urllib2
import simplejson
all = {}

mydict = {
'origins': '21.107528,78.853211', 
'destinations': '21.116370,78.909128',
'waypoints':'via:21.116528,78.855420|via:21.117771,78.863625|via:21.129976,78.876392|via:21.124785,78.894180|via:21.118645,78.905107', 
'departure_time':'now',
'traffic_model':'best_guess',
'key':'AIzaSyAz-mDQafUjU2Sdfr1WFlS2bLwbWuytrew'
}

baseurl = "https://maps.googleapis.com/maps/api/distancematrix/json?";
params = "&".join("=".join(_) for _ in mydict.items());
url = (baseurl + params);
print(url);
response = urllib2.urlopen(url)
data = simplejson.load(response)
all['h2w'] = data['rows'][0]['elements'][0]['duration_in_traffic']

for key, value in sorted(all.items(), key=lambda x: x[1]['value']):
    print(key, value)