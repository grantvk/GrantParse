import requests

urlDict = {  # 'StackOverflow' : 'http://stackoverflow.com/jobs?location=Nashville%2C+TN&range=50&distanceUnits=Miles',
    # 'HCA' : 'http://careersathca.com/careers/search.dot?jobClass=InformationTechnology&state=Tennessee&perPage=100',
    # 'Faculty_Directory' : 'https://mycampusapps.belmont.edu/teleDirectory/index.cfm?dept=630&mode=listPeople',
    # 'Vandy' : 'https://vanderuniv.taleo.net/careersection/.vu_cs/jobsearch.ftl?lang=en&portal=2140492874' ,
    # 'HCA_Taleo' : 'https://hca.taleo.net/careersection/newparallonkeywordssvcscorp/jobsearch.ftl' ,
    # 'StThomas' : 'http://careers.sthealth.com/' ,
    # 'Dice20' : 'https://www.dice.com/jobs/sort-date-limit-30-l-Nashville%2C_TN-radius-30-startPage-20-limit-30-jobs?searchid=2666944509358'
    # 'Your Choice' : 'http://www.what_ever_you_want.com'
    # 'iHCA' : 'http://careersathca.com/careers/search.dot?jobId=08942-125118&src=CWS-10230',
    #'NFLqb': 'http://www.footballdb.com/stats/qb-records.html?type=&alltime=1',
    'espn': 'http://www.espn.com/nfl/player/stats/_/id/10447/',
}

for name, link in urlDict.items():
    response = requests.get(link)
    html = response.content

    fileName = name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()