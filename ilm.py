import urllib2

url_sputnik = 'http://meteo.physic.ut.ee/et/frontmain.php'

response = str(urllib2.urlopen(url_sputnik).read())

print response.replace('/webcam/uus/pisike.jpg', 'http://sputnik.aai.ee/uvi/uvgraph.php')
