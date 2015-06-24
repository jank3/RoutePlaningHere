#Input:coordinates with priorities
#Output:
import urllib2
import json
from sys import stdin

def getTrafficTime(start,end):
	# insert your own app_id and app_code
	content = json.loads(urllib2.urlopen("http://route.cit.api.here.com/routing/7.2/calculateroute.json?app_id=xxx&app_code=xxx&waypoint0=geo!"+start+"&waypoint1=geo!"+end+"&mode=fastest;car;traffic:disabled").read())
	return content['response']['route'][0]['summary']['travelTime']

def Topten(where,Targets):
	topten=[]#Liste aus Tupeln aus Zeit und Koordinaten(String)
	for wo in coordinates:
		timediff=getTrafficTime(current,wo)
		if len(topten)<10:
			topten.append((wo,timediff))
		elif timediff<max(topten):
			topten.pop(max)
			topten.append((wo,timediff))
	return topten

def bestnextstep(where,Targets):	
	minimum=float("inf")#infinity
	out=""
	for target in Targets:
		temp=getTrafficTime(where,target)
		if temp<minimum:
			minimum=temp
			out=target
	return (minimum,out)
	'''
	out=""
	for j in range(0,deep):
		topten=Topten(where,Targets)
		for i in topten:
			Targets.remove(i)
			topten2 = Topten(i,Targets)
			Targets.append(i)
			for k in topten2:
				k[1] 
			#if rating<minimum:
			#	minimum=rating
			#	out=step
	return minimum,out
	'''
	
			
		
pfad=[]

cordinates=[]
for line in stdin:
	cordinates.append(line.strip("\r\n"))
current=cordinates.pop()
start = current
time=0
while time<8*60*60 and cordinates:
	a,b=bestnextstep(current,cordinates)
	current=b
	cordinates.remove(b)
	if time+a+getTrafficTime(b,start)>8*60*60:
		break
	else:
		pfad.append(b)
		time+=a
		#print time
for wp in pfad:
	print wp
print "our time"
print time
# insert your own app_id and app_code
url = "http://route.cit.api.here.com/routing/7.2/calculateroute.json?app_id=xxx&app_code=xxx"
for it in range(0,len(pfad)):
	url += "&waypoint"
	url += str(it)
	url += "=geo!"
	url += pfad[it]
url += "&mode=fastest;car;traffic:disabled"
content = json.loads(urllib2.urlopen(url).read())
print url
print "time after"
print content['response']['route'][0]['summary']['travelTime']
			
		
		
