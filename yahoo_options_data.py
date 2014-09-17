import json
import sys
import re
import urllib
from bs4 import BeautifulSoup

def contractAsJson(filename):
  jsonQuoteData = "[]"

  fsoup = open(filename)
  text = fsoup.read()
  soup = BeautifulSoup(text)
  
  dateUrls = list()
  optionQuotes = list()
  website = "http://finance.yahoo.com"
  
  tags = soup.find_all(True)
  sequence = len(tags)
  for tag in tags:
  	
  	if tag.has_attr('class'):
  		stockName = str(tag.get('class')[0])
  		if (stockName == 'time_rtq_ticker'):
  			currPrice = float(tag.string)
  	if tag.has_attr('href'):
  		sequence = sequence - 1
  		href = str(tag.get('href',None))
  		if re.search('.*&m=[0-9]+-[0-9]+.*', href):
  			href = href.replace('&', '&amp;')
  			dateUrls.append(website + href)
  		if re.search('/q/op\?s=\S+k=', href):
  			tmp = dict()
  			tmp['Strike'] = str(tag.string)
  			tmpPointer = tag.find_next('td')
  			tmpString = re.findall('[A-Z]+[0-9]+', tmpPointer.string)
  			s1 = str(tmpString[0])
  			tmp['Symbol'] = s1[:len(s1)-6]
  			tmp['Type'] = str(tmpString[1][0])
  			tmp['Date'] = str(re.findall('1[0-9]+', tmpPointer.string)[0])
  			tmpPointer = tmpPointer.find_next('td')
  			tmp['Last'] = str(tmpPointer.string)
  			tmpPointer = tmpPointer.find_next('td').b
  			tmp['Change'] = " " + str(tmpPointer.string)
  			tmpPointer = tmpPointer.find_next('td')
  			tmp['Bid'] = str(tmpPointer.string)
  			tmpPointer = tmpPointer.find_next('td')
  			tmp['Ask'] = str(tmpPointer.string)
  			tmpPointer = tmpPointer.find_next('td')
  			tmp['Vol'] = str(tmpPointer.string)
  			tmpPointer = tmpPointer.find_next('td')
  			tmp['Open'] = str(tmpPointer.string)
  			openValue = tmp['Open'].replace(",", "")
  			tmp['A'] = int(openValue)
  			tmp['Aa'] = sequence
			optionQuotes.append(tmp)
  			
  optionQuotes.sort(reverse = True)
  for optionQuote in optionQuotes:
    del optionQuote["A"]
    del optionQuote["Aa"]  
  jsonQuoteData = json.dumps({"currPrice":currPrice, "dateUrls":dateUrls, "optionQuotes":optionQuotes}, sort_keys=True, indent=4, separators=(',', ': '))

  return jsonQuoteData