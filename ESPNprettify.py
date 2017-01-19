from bs4 import BeautifulSoup

#Prepare for parsing HCA with BeautifulSoup
fileHCA = open("espn.html",'r').read()
soupHCA = BeautifulSoup(fileHCA, 'lxml')
prettifyHCA = soupHCA.prettify()

#Write prettified HCA to html file
prettyFile = 'espnPrettified.html'
outfile = open(prettyFile, "w")
outfile.write(prettifyHCA)
outfile.close()
