### creating general node for linked list:
class Node :
    def __init__(self,data):
        self.Data = data
        self.next = None
        self.prev = None

#############################################


#### creating linked list class:
class linkedList:
    ### constructor create an empty linkedlist
    def __init__(self):
        self.Head = None
        self.Tail = None
    
    ### constructor for one node in the linkedlist:
    # def __init__(self,data):
    #     nd = Node(data)
    #     self.Head = nd
    #     self.Tail = nd        
    
    ## add function : creating new node and add it at the end of the list
    def Add(self,data):
        nd = Node(data)

        ##frist case empty linkedlist:which mean that head & tail are none
        if (self.Head == None):
            self.Head = nd
            self.Tail = nd
        
        ## second case: linkedlist not empty
        else:
            self.Tail.next = nd
            nd.prev = self.Tail
            self.Tail = nd
        


    ### insert node in a specific location if the location is out of the range insert at the end 
    def insert(self , data , loc):
        nd = Node(data)
        
        if (loc < 0):   ## if the location is negative
            raise ValueError("The location can't be negative")
            
        else:
            ### not empty linkedList:
            if (self.Head != None):
                if (loc == 0):
                    self.Head.prev = nd
                    nd.next = self.Head
                    self.Head = nd
                    

                else:
                    ## will use a counter to go through from head till the loc & current node to switch nodes
                    i = 0
                    curr = self.Head
                    while (i < loc and curr != None):
                        curr = curr.next
                        i += 1

                    ### insert at the end
                    if (curr == None):
                        self.Tail.next = nd
                        nd.prev = self.Tail
                        self.Tail = nd
                    ### insert at the middle
                    else:
                        curr.prev.next = nd
                        nd.prev = curr.prev
                        nd.next = curr
                        curr.prev = nd

                #### insert into empty linkedList
            else:
                self.Head = nd
                self.Tail = nd

    ## search function using the data
    def search(self,data):

       ## frist need to check if the list is not empty
       if (self.Head == None):
           raise ValueError("The linkedList is empty")
       
       else:
           curr = self.Head
           i = 0

           while (curr != None):
                if (curr.Data == data):
                    return curr.Data , i
                else:    
                    curr = curr.next
                    i += 1
           
           return 'NotFound'


     ### delete fucntion using location
     ## delete mean disconnect the node from any other node to refer to it .
    def delete(self,loc):
        deleted = False

         ## check if list is empty
        if (self.Head == None):
            raise ValueError("The linkedList is empty")

        else:

           ## delete the first node and make the second one be the head
           if (loc == 0):
                ## there is only one node  
                if (self.Head == self.Tail):
                    self.Head = None
                    self.Tail = None
                else:
                    ## there are more than one node in the list
                    self.Head = self.Head.next
                    self.Head.prev = None
                deleted = True

             ## delete node for a specific location which is not the first one .
           else:
                i = 0
                curr = self.Head
                while (i < loc and curr != None):
                    curr = curr.next
                    i += 1
              
                if (curr != None):
                    ## delete the last node
                    if (curr == self.Tail):
                        self.Tail = self.Tail.prev
                        self.Tail.next = None

                    else:
                        ## delete the node in middle
                        curr.next.prev = curr.prev
                        curr.prev.next = curr.next

                    deleted = True

                else:
                    raise ValueError("location out of the length of the list")

        return deleted



#### to check
ll = linkedList()
ll.Add(5)
ll.Add(15)
ll.insert(7,0)
ll.insert(10,4)
print(ll.delete(1))
print(ll.search(10))
print(ll.Head.Data)