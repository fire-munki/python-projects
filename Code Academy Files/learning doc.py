start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print square_list



# Write your function below!
def fizz_count(x):
	count = 0
  	for item in x:
    		if x == "fizz":
 					count = count + 1
  	return count



# Write your function below!
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count




  def compute_bill (food):
  total = 0
	for item in prices:
  		total += prices[item]
  #print total
	return total




def compute_bill(food):
  sum_price = 0
  for key in food:
    if stock[key] > 0:
      sum_price += prices[key]
      stock[key] -= 1

def compute_bill (food):
  total = 0
  
  for fruit in food:
    if stock[fruit] > 0:
      total += prices[fruit]
      stock[fruit] -= 1
      return total


 n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
	for i in range(len(words)):
    result += words[i]
	return result

print join_strings(n)




n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for each_number in lists:
  	for number in each_number:
    		results.append(lists)
	return results



print flatten(n)


list_of_lists = [ [1, 2, 3], [4, 5, 6] ]

def reset_list_items(nested_list):
  zeros_result = []
  for each_list in nested_list:
    for item in each_list:
      zeros_result.append(0)
  return zeros_result

print reset_list_items(list_of_lists)





