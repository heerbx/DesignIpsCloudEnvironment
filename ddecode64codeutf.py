
import base64
#from rawweb import RawWeb
import urllib.parse
import xml.etree.ElementTree as ET
import csv

logtoparse='baddataset.log'
badwordshttprequest=['sleep','uid', 'eid','select','waitfor','from','system','select',
					 'union','order by','group by','where','alert','script','sleep','convert']

# Nsingle_q=0
# Ndouble_q=0
# Nbraces=0
# Ndashes=0
# Nspaces=0
# badwords_count=0
# classy=0
# badwords_count=0


def featureextraction(body,header):
	badwords_count=0
	classy='good'
	Nsingle_q=body.count("'")
	Ndouble_q=body.count("\"")
	Ndashes=body.count("--")
	Nbraces=body.count("(")
	Nspaces=body.count(' ')

	for i in badwordshttprequest:
		badwords_count+=body.count(i)

	st=str(header)
	
	for i in badwordshttprequest:
		# Nsingle_q=body.count("'")
		# Ndouble_q=body.count("\"")
		# Ndashes=body.count("--")
		# Nbraces=body.count("(")
		# Nspaces=body.count(' ')
		
		# for k,v in header.iterintems():
		# 	st=str()
		badwords_count+=st.count(i)
	# print (Nsingle_q,Ndouble_q,Ndashes,Nbraces,Nspaces,badwords_count,classy)
	return 0
def parse_log(log_path):
		'''
		This fucntion accepts burp log file path.
		and returns a dict. of request and response
		result = {'GET /page.php...':'200 OK HTTP / 1.1....','':'',.....}
		'''
		result = {}
		try:
			with open(log_path): pass
		except IOError:
			print ("[+] Error!!! ",log_path,"doesn't exist..")
			exit()
		try:
			tree = ET.parse(log_path)
		except :
			print ('[+] Opps..!Please make sure binary data is not present in Log, Like raw image dump,flash(.swf files) dump etc')
			exit()
		root = tree.getroot()
		for reqs in root.findall('item'):
			raw_req = reqs.find('request').text
			raw_req = urllib.parse.unquote(raw_req).encode('utf8')
			raw_resp = reqs.find('response').text
			result[raw_req] = raw_resp
		return result

result = parse_log(logtoparse)
# f=open('finaldataset161023.csv',"w")
# c=csv.writer(f)
# c.writerow(['method','header','body','path','Nsingle_q','Ndouble_q','Ndashes','Nbraces','Nspaces','badwords_count','class'])
# f.close()

for i in result:
	raaw = base64.b64decode(i)
	# print(raaw)
	stgraw =raaw.__str__()
	stx=stgraw.split("b'",1)
	# print(stx)
	try:
		methodx=stx[1].split(" ",1)
		method=methodx[0]
		# print(method)
		bodyx=methodx[1].split(" ",1)
		body=bodyx[0]
		# print(body)
		pathx=bodyx[1].split("\\r\\n",1)
		path=pathx[0]
		# print(path)
		headertab=pathx[1].split("\\r\\n",pathx[1].count('\\r\\n'))
		# print(headertab)
		header = {}

		for i in range(0, len(headertab)-2, 1):
			header[headertab[i].split(':',1)[0]] = headertab[i].split(':',1)[1]

		data=[]
		data.append(method)
		data.append(header) 
		data.append(body) 
		data.append(path)
		badwords_count=0
		classy='bad'
		Nsingle_q=body.count("'") +method.count("'")
		Ndouble_q=body.count("\"")+method.count("\"")+header.__str__().count("\"")
		Ndashes=body.count("--")+method.count("--")+header.__str__().count("--")
		Nbraces=body.count("(")+method.count("(")+header.__str__().count("(")
		Nspaces=body.count(' ')+method.count(' ')
		
		for i in badwordshttprequest:
			badwords_count+=body.count(i)+method.count(i)
			badwords_count+=header.__str__().count(i)
		
		st=str(header)
		
		for i in badwordshttprequest:
			# Nsingle_q=body.count("'")
			# Ndouble_q=body.count("\"")
			# Ndashes=body.count("--")
			# Nbraces=body.count("(")
			# Nspaces=body.count(' ')
			
			# for k,v in header.iterintems():
			# 	st=str()
			badwords_count+=st.count(i)
			
		data.append(Nsingle_q)
		data.append(Ndouble_q)
		data.append(Ndashes)
		data.append(Nbraces)
		data.append(Nspaces)
		data.append(badwords_count)
		data.append(classy)
		
		f=open('finaldataset161023.csv',"a")
		c=csv.writer(f) 
		c.writerow(data)

	except:
		pass
	
	# print(header,method,body,path)
f.close()