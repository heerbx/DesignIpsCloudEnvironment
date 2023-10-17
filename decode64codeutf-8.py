import base64
#from rawweb import RawWeb
import urllib.parse
import xml.etree.ElementTree as ET
# import csv

logtoparse='burp3.log'
badwordshttprequest=['sleep','uid','select','waitfor','from','system','select',
					 'union','order by','group by','where','alert','script']

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

# def parsehttprequet(rawreq):
			
# 		raw = rawreq
# 		global headers,method,body,path
# 		headers = {}

# 		sp = raw.split('\n\n',1)

# 		if len(sp) > 1:
# 			head = sp[0]
# 			body = sp[1]
# 		else :
# 			head = sp[0]
# 			body = ""
# 		c1 = head.split('\n',head.count('\n'))
# 		method = c1[0].split(' ',2)[0]
# 		path = c1[0].split(' ',2)[1]
# 		for i in range(1, head.count('\n')+1):
# 			slice1 = c1[i].split(': ',1)
# 			if slice1[0] != "":
# 				try:
# 					headers[slice1[0]] = slice1[1]
# 				except IndexError:
# 					pass
# 		return headers,method,body,path


# def tobase64(log):
# 	allparsedi=''
# 	for i in log:
# 		allparsedi=allparsedi+i
# 	return allparsedi



#test the parse to utf-8
result = parse_log(logtoparse)
for i in result:
	raaw = base64.b64decode(i)
	# print(raaw)
	break
	
	# parsehttprequet(raaw)
#first test withr raaw
stgraw =raaw.__str__()
stx=stgraw.split("b'",1)
# print(stx)

methodx=stx[1].split(" ",1)
method=methodx[0]
# # print(method)

bodyx=methodx[1].split(" ",1)
body=bodyx[0]
# # print(body)

pathx=bodyx[1].split("\\r\\n",1)
path=pathx[0]
# # print(path)

headertab=pathx[1].split("\\r\\n",pathx[1].count('\\r\\n'))
# # print(headertab)

# #rescue

header = {}
for i in range(0, len(headertab)-2, 1):
       header[headertab[i].split(':',1)[0]] = headertab[i].split(':',1)[1]





# #reserved for saving purposes
print(header,method,body,path)

def featureextraction(body,header):
	badwords_count=0
	classy=1
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
	print (Nsingle_q,Ndouble_q,Ndashes,Nbraces,Nspaces,badwords_count,classy)
	return 0
	 

featureextraction(body,header)

# data=[]
# data.append(method)
# data.append(header)
# data.append(body)
# data.append(path)

# f=open('httplogtest.csv',"w")
# c=csv.writer(f)
# c.writerow(['method','header','body','path'])
# f.close()
# f=open('httplogtest.csv',"a")
# c=csv.writer(f)
# c.writerow(data)
# f.close()

	






#using 2 table
# tab1=[]
# for i in headertab:
# 	for j in range(0,)
# 	tab1[]=i[0].split(':',1)[0]
# hearder={}
# for i in range(0,headertab.__len__()-3,1):
# 	part1=headertab[i].split(':',1)[0]
# 	part2=headertab[i].split(':',1)[1]
# 	headertab={part1:part2}

	

# print(headertab[0].split(':',1)[0])
# print(headertab[0].split(':',1)[1])

# print(hearder)
# print(method,body,path)

	


# print(k)
# finalcar=''
# count=0
# for i in k:
# 	if i.find('\\n'):
# 		count=count+1
# print(count)

# tobase64(result)


# print (base64.b64decode(parse_log(logtoparse)))
# restr=result.__str__()
# print(restr)