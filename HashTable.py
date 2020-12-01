class HashTable:
    def __init__(self,size):
        self.data = [None] * size
         
    def hashFunction(self, key):
        hash = 0 
        for i in range(len(key)):
            hash = (hash + (i*len(key)) * i ) % len(self.data)
        
        return hash

    def set(self, key, value):
        address = self.hashFunction(key)
        if(self.data[address] is None):
            self.data[address] = []
            self.data[address].append([key,value])
            
        else:
            self.data[address].append([key,value])
            

    def get(self, key):
        address = self.hashFunction(key)
        for i in self.data[address]:
            if i[0] == key:
                return i[1]
    
        return None

    def keys(self):
        keysArray = []
        for i in range(len(self.data)):
            if(self.data[i]): 
                for j in range(len(self.data[i])):
                    keysArray.append(self.data[i][j][0])
        return keysArray


myHashTable = HashTable(10)
myHashTable.set('grapes', 10000)
myHashTable.set('apples', 3000)
myHashTable.set("oranges", 2)
print(myHashTable.get('grapes'))
print("my table is \n    " ,myHashTable.data)
print(myHashTable.keys())


'''
hashtables vs array 
hashtables : 
    search O(1)
    insert O(1)
    lookup O(1)
    delete O(1)

arrays: 
    search O(n)
    insert O(n)
    lookup O(1)
    push   O(1)
    delete O(1)
'''


def firstRecurringCharacter(input):
    foundOccurances = dict()
    for i in input:
        if i in foundOccurances:
            return i 
        foundOccurances[i] = i 

    return None


print(firstRecurringCharacter([2,5,1,2,3,5,1,2,4]))
#It should return 2

print(firstRecurringCharacter([2,1,1,2,3,5,1,2,4]))
#It should return 1

print(firstRecurringCharacter([2,3,4,5]))
#It should return undefined
