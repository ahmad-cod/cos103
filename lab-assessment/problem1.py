#  write a python program that finds the common elements between two lists

def common_elements(list1, list2):
  common_els = []

  for el in list1:
    if list2.count(el):
      common_els.append(el)


  print(common_els)


common_elements([1, 2, 3,], [3, 2, 5])
common_elements(["ahmad", "adewale", "aroyehun",], ["wahab", "ahmad", "aroyehun"])