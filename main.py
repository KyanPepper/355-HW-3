
def quicksort(list, key=lambda x: x, reverse=False):
    if len(list) <= 1:
        return list #Base case: arrays with 0 or 1 element are already "sorted"
    else:
        pivot = list[0]
        if reverse:
            less = [i for i in list[1:] if key(i) >= key(pivot)] #Sub-array of all the elements less than the pivot
            greater = [i for i in list[1:] if key(i) < key(pivot)] #Sub-array of all the elements greater than the pivot
        else:
            less = [i for i in list[1:] if key(i) <= key(pivot)] #Sub-array of all the elements less than the pivot
            greater = [i for i in list[1:] if key(i) > key(pivot)] #Sub-array of all the elements greater than the pivot
        return quicksort(less, key, reverse) + [pivot] + quicksort(greater, key, reverse) #Recursively sort the sub-arrays and combine them with the pivot
    #Quicksort Decending

print(quicksort([3,6,8,10,1,2,1], reverse=True)) #Output: [10, 8, 6, 3, 2, 1, 1]
#Quicksort Ascending
print(quicksort([3,6,8,10,1,2,1])) #Output: [1, 1, 2, 3, 6, 8, 10]



def group_names_by_initial(names):
    groups = {} 
    for name in names: 
        name = name.lower() #Convert the name to lowercase
        char1 = name[0]
        if char1 in groups and name not in groups[char1]: #If the character is already a key in the dictionary and the name is not already in the list of names for that character
            groups[char1].append(name) #Add the name to the list of names for that character
        else:
            groups[char1] = [name]  #
    return groups

print(group_names_by_initial(["Adam", "adam", "Charlie", "Alex", "Bob", "David", "Alice"])) #Output: {'A': ['Adam', 'Alex', 'Alice'], 'C': ['Charlie'], 'B': ['Bob'], 'D': ['David']}

def foldl(function, list, initial):
    result = initial #Set the initial value of the result to the initial value passed in
    for i in list: 
        result = function(result, i) #Apply the function to the result and the current element in the list
    return result


def foldr(function, list, initial):
    result = initial #Set the initial value of the result to the initial value passed in
    for i in reversed(list): #Iterate over the list in reverse order
        result = function(i, result)  #Apply the function to the current element in the list and the result
    return result   

def zip_with(function, list1, list2):
    if(len(list1) != len(list2)):
        raise ValueError("The lists must have the same length")
    return [function(x, y) for x, y in zip(list1, list2)] 


class NoDupeStack:
    def __init__(self): #Initialize the stack and set
        self.stack = []
        self.set = set()
    
    def push(self, item): #Add an item to the stack
        if item not in self.set:
            self.stack.append(item)
            self.set.add(item)
    
    def pop(self): #Remove and return the top item in the stack
        if len(self.stack) == 0:
            return None
        item = self.stack.pop()
        self.set.remove(item)
        return item
    
    def peek(self): #Return the top item in the stack
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    
class NoDupeQueue:
    def __init__(self):
        self.queue = []
        self.set = set()
    
    def enqueue(self, item): #Add an item to the queue
        if item not in self.set:
            self.queue.append(item)
            self.set.add(item)
    
    def dequeue(self): #Remove and return the first item in the queue
        if len(self.queue) == 0:
            return None
        item = self.queue.pop(0)
        self.set.remove(item)
        return item
    
    def peek(self): 
        if len(self.queue) == 0: #If the queue is empty 
            return None
        return self.queue[0] #Return the first element in the queue