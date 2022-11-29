
import requests
import json

# API name
API = "Jobpost create"

# provide user id and header
user_id = 404
headers = {"Authorization": "Token 80d11ca4d153302cbaa8f578948ca4dc0fdf6948"}

# API url
Base_url = "http://ec2-3-17-167-77.us-east-2.compute.amazonaws.com:8000/api/v1/employers/"
urlend = "/jobs"
createjoburl = Base_url + str(user_id) + urlend
print("Create a job using the 'Job Create API'")
print(createjoburl)

# Read input JSON file
file1 = open('C:\\Users\\Administrator\\PycharmProjects\\APIs Json file\\job create.json', 'r')
j_input1 = file1.read()
r_jobcreate = json.loads(j_input1)

# Make POST request with Json input body

jobcreateresp1 = requests.post(createjoburl, headers=headers, json=r_jobcreate)
print("Create API status code is", jobcreateresp1.status_code)

# assigning the json response data or content to a variable
json_data = jobcreateresp1.json()
# print(json_data)

# assigning the data in the response content to a variable
data = json_data['data']

# assigning the job id in the data to a variable
id = data['id']
print("The created job's id is", id)
print("*******************************************************")

# Now we have to find the job is listing in search,

# API url and API name
API2 = "Job search"
url2 = "http://ec2-3-144-164-248.us-east-2.compute.amazonaws.com:8001/api/jobs"
print("Search the created job using the 'Job Search API'")
print(url2)

# Read input JSON file
file2 = open('C:\\Users\\Administrator\\PycharmProjects\\APIs Json file\\jobsyncsearch.json', 'r')
j_input2 = file2.read()
r_json2 = json.loads(j_input2)

# Make POST request with Json input body

response2 = requests.post(url2, headers=headers, json=r_json2)

# above 'response2' is the variable where we store the response of the post request
# now printing the response content

Jobsearchcode = response2.status_code
print("Jobs search API response code is ", Jobsearchcode)
# print(response2.content)

# assigning the json response data or content to a variable
json_data1 = response2.json()
# print(json_data1)

searchjobsidlist = [sub['id'] for sub in json_data1]
# for i,j in json_data1[0].items():
    #print(i)
    #print(j)

print("Search listed jobs ids list is")
print(searchjobsidlist)


# check whether the created job is available in the search list

slen = len(searchjobsidlist)

x = slen
for i in range(slen):
    if id == searchjobsidlist[i]:
        print("Job", id, "is available in the search list")
    else:
        x = x-1

if x==0:
    print("Job", id, "is unavailable in the search list")
print("*******************************************************")


# Now we can delete that job using Job delete API

Base_url2 = "http://ec2-3-17-167-77.us-east-2.compute.amazonaws.com:8000/api/v1/employers/"

url_part2 = "/jobs/"

jobdeleteurl = Base_url2 + str(user_id) + url_part2 + str(id)
print("Deleting the created job using 'Job Delete API'")
print(jobdeleteurl)

# Make DEL request

jobdeleteresp1 = requests.delete(jobdeleteurl, headers=headers)

jsondelete_data = jobdeleteresp1.json()
print(jsondelete_data)

# print("data is", jsondelete_data)
print("Delete job API status_code is", jobdeleteresp1.status_code)

if jobdeleteresp1.status_code == 202:
   print("job", id, "is deleted successfully")
print("*******************************************************")


# Now we can search that job again in the search list using the search API

# API url and API name
API4 = "Job search API"
url4 = "http://ec2-3-144-164-248.us-east-2.compute.amazonaws.com:8001/api/jobs"
print("Again search the job using 'Job Search API' to check the syncing")
print(url4)

# Read input JSON file
file4 = open('C:\\Users\\Administrator\\PycharmProjects\\APIs Json file\\jobsyncsearch.json','r')
j_input4 = file4.read()
r_json4 = json.loads(j_input4)

# Make POST request with Json input body

response4 = requests.post(url4, headers=headers, json=r_json4)

# above 'response2' is the variable where we store the response of the post request
# now printing the response content

Jobsearchcodefinal = response4.status_code
print("Jobs API response code is ", Jobsearchcodefinal)
# print(response4.content)

# assigning the json response data or content to a variable
json_data4 = response4.json()
searchjobsidlistfinal = [sub['id'] for sub in json_data4]


print("Now the search listed jobs ids list is")
print(searchjobsidlistfinal)

# check whether the created job is available in the search list

slenfinal = len(searchjobsidlistfinal)

y = slenfinal
for i in range(slenfinal):
    if id == searchjobsidlistfinal[i]:
        print("Job", id, "is available in the search list")
    else:
        y = y-1

if y==0:
    print("Job", id, "is unavailable in the search list")

print("*******************************************************")





