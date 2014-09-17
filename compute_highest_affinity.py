# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo"). 

  #unique the site list and user list
  allSite = sorted(list(set(site_list)))
  nSite = len(allSite)
  allUser = list(set(user_list))
  #pre-process the dictory, where give the user visit site list
  listIndex = {}
  for user in allUser:
    listIndex[user] = []
    for i in range(len(user_list)):
      if user == user_list[i]:
        if site_list[i] not in listIndex[user]:
          listIndex[user].append(site_list[i])
    listIndex[user].sort()
  #initialize the affinity matrix
  affMatrix = {}
  for i in range(nSite):
    for j in range(i + 1, nSite):
      affMatrix[allSite[i], allSite[j]] = 0
  #calculate the affinity of each site pair
  for k in listIndex:
    for i in range(len(listIndex[k]) - 1):
      for j in range(i + 1, len(listIndex[k])):
        affMatrix[listIndex[k][i], listIndex[k][j]] += 1
  #get the highest affinity site pair
  max = 0
  for i in range(nSite):
    for j in range(i + 1, nSite):
      if affMatrix[allSite[i], allSite[j]] > max:
        max = affMatrix[allSite[i], allSite[j]]
        tmp1 = allSite[i]
        tmp2 = allSite[j]
  return tmp1, tmp2