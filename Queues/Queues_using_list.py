
'''
Queues can be implement in two ways:
1. We can do insertion from front and deletion from back 
2. Either we can do insertion from  back and deletion from front
'''

# Insertion from back and deletion from front !
queues =[]

queues.append(1)
queues.append(2)
queues.append(3)
queues.append(4)
# ------ Deletion -------
queues.pop(0) # --- humlog always pop krenge front element
queues.pop(0)

#---isEmpty---
print(not queues)
#----- To check the head element/ front element
print(queues[0])
#----- To check the back/Rear element
print(queues[-1])

print(queues)

# ------------------------------------------------------



