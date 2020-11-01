#.............program to build tree(NAVANEETHA).....................
import csv

training_data = []
testing_data = []

with open("/content/test_Set.csv") as tsv:
    for line in csv.reader(tsv, delimiter=","):
                
        testing_data.append(list(line))

with open("/content/xss.csv") as tsv:
            for line in csv.reader(tsv, delimiter=","):
                
                training_data.append(list(line))


attributes = ['url_length','Keywords','Encoded','spcl_char','Domain','Label']

#.............Returns the Unique value in the dataset..........
def get_unique_val(row,col):
  return set([r[col] for r in row])

#.........COunts no of type of data in dataset.......
def count_Class(row):

  count = {}
  for r in row:

    attribute = r[-1]
    if attribute not in count:
      count[attribute] = 0

    count[attribute] += 1
  return count

#...................Class defines the rules in the node...........

class Node_Rules:
  #............for numeric data..............
  def __init__(self,col,val):
    self.col = col
    self.val = val

  def comp(self,row):
    values = row[self.col]
    return values >= self.val

  def __repr__(self):
    contn = '>='
    return "Is %s %s %s?" % (attributes[self.col],contn,str(self.val))

def partition(rows,qtn):
    
  t_row,f_row = [],[]
  for r in rows:

    if qtn.comp(r):
      t_row.append(r)
    else:
      f_row.append(r)

  return t_row,f_row

class Calculate:
  #.............Calculates Gini Impurity.................
  def gini_idx(self,rows):
    count = count_Class(rows)
    impurity = 1
    for target in count:
      prob = count[target]/float(len(rows))
      impurity -= prob**2

    return impurity

  #...........Calculates Information-gain............
  def information_gain(self,left_set,right_set,uncertianity):

    total_length = len(left_set)+len(right_set)
    prob = float(len(left_set))/ total_length
    gain = uncertianity -prob * gini_idx(left_set)-(1-prob)*gini_idx(right_set)

    return gain
