import utils

class BadNetworkException(Exception):
    """
    You can raise this exception if the network is invalid in some way (e.g.,
    the network matrix is not square.)
    """
    pass

class Network:

    def shortestPath(self, origin):
        """
        This method finds the shortest path from origin to all other nodes
        in the network.  You should use the lists already created for backnode
        and cost labels, and fill them with the correct values.  You can use
        any of the shortest path algorithms taught in class.
        
        Use the constants utils.NO_PATH_EXISTS in place of '-1' when the
        backnode is undefined (i.e. for the origin or if there is no path to
        that node), and utils.INFINITY for the initial values of cost labels.
        """
        
        # Set up backnode and cost lists to return
        backnode = [utils.NO_PATH_EXISTS] * self.numNodes
        costlabel = [utils.INFINITY] * self.numNodes
        
        ### YOUR CODE HERE ###
        #  Replace this with your shortest path code, ending with
        #  
        #  return (backnode, costlabel)
        #
        
        SEL = [origin];
        #print('The length of SEL is {}'.format(len(SEL)))
        costlabel[origin] = 0;
        

        while len(SEL) > 0: #Continue until the SEL is emptied
          #print("SEL used is node {}".format(SEL[0]))
          change = 0;
          for row in range(self.numNodes):
            #By setting the column to the node we want to go to, we can cycle through the backnodes by going down the rows in the same column
            if (self.matrix[row][SEL[0]] == 1) and (costlabel[row]+self.cost[row][SEL[0]] < costlabel[SEL[0]]):
              #If the cost to get to the node from the backnode we're checking is less than what we currently have, change the cost and backnode
              change = 1;
              backnode[SEL[0]] = row;
              costlabel[SEL[0]] = costlabel[row]+self.cost[row][SEL[0]];
              #print('The backnode was changed to {} and the costlabel was changed to {}'.format(backnode[SEL[0]],costlabel[SEL[0]]))

          if (change == 1) or (SEL[0] == origin): #If a value was changed or it starts at the origin
            for col in range(self.numNodes):
              #Add everything downstream of the current node to the SEL
              if (self.matrix[SEL[0]][col] == 1) and col not in SEL:
                SEL.append(col)
            
          del SEL[0] #Delete the node that was being used
        
        addlink = 1;
        finalNode = self.numNodes - 1;
        shortest_path = [finalNode];
        pathcost = 0;
        while addlink > 0: 
          #Keep going until there are no more links to add
          addlink = 0;
          index = shortest_path[0]; 
          #What is the node you want to look back from?
          if index != origin:
            #If the node is not 1
            shortest_path.insert(0, backnode[index])
            pathcost += self.cost[shortest_path[0]][shortest_path[1]];
            #Add the backnode to the front
            addlink = 1;
        print('You can get from node {} to node {} by using this path: {}'.format(shortest_path[0],finalNode,shortest_path))
        print('The cost to do so is',pathcost)
        print(backnode, costlabel)
        return(backnode, costlabel)

        raise utils.NotYetAttemptedException
                        

        
    def maxFlow(self, source, sink):
        """
        This method finds a maximum flow in the network.  Return a tuple 
        containing the total amount of flow shipped, and the flow on each link
        in a list-of-lists (which takes the same form as the adjacency matrix).
        These are already created for you at the start of the method, fill them
        in with your implementation of minimum cost flow.
        """
        
        # Set up network flows matrix; flow[i][j] should have the
        # value of x_ij in the max-flow algorithm.
        #total flow is b in notes
        totalFlow = 0;
        flow = list();
        
        for i in range(self.numNodes):
          flow.append([0] * self.numNodes)
        #self.capacity[i][j] is the capacity on the link ij

        #flow is a matrix where m = n = number of nodes
        #flow[row][col] = flow from a node to another node it's linked to
        
        ### YOUR CODE HERE ###
        #  Replace this with your max flow code, ending with
        #
        #  return (totalFlow, flow)
        #
        
        #Find an undirected path connecting the start and end with a positive residual capacity`
        
        #Stop if you can't find a path like that
        #Find the residual capacity
        #Increase forward flows and decrease backwards flows until you minimize the residual capacity
        #Increase the total flow by the same amount you changed the flow to minimize the residual capacity

        #The residual capacity is the smallest difference between the flow and capacity in the forward direction and the difference between the flow and 0 for the reverse direction

            # Find the residual capacity of u^* of pi 
            # for each forward arc (i,j) in pi, #xij += u^* 
            # for each reverse arc (i,j) in pi, #xij -= u^*
            #b+=u^*
        

        raise utils.NotYetAttemptedException        

    def search(self, source):
        reachable = [source]
        SEL = [source]
        while len(SEL) > 0:
            i = SEL[0]
            SEL = SEL[1:]
            for j in range(0, self.numNodes):
                if self.matrix[i][j] == 1 and j not in reachable:
                    reachable.append(j)
                    SEL.append(j)
        return reachable
        
    def __init__(self, networkFile = None, linkDataFile = None,
                 nodeDataFile = None):
        self.numNodes = 0
        self.matrix = list()
        self.cost = list()
        self.capacity = list()
        self.supply = list()

        if networkFile != None:
            self.readNetworkFile(networkFile)

        if linkDataFile != None:
            self.readLinkDataFile(linkDataFile)

        if nodeDataFile != None:
            self.readNodeDataFile(nodeDataFile)

    def readNetworkFile(self, networkFileName):
        """
        Reads a network adjacency matrix from the given file and set up
        other network data structures.
        """
        networkLines = utils.processFile(networkFileName)
        self.matrix = list()
        for rawLine in networkLines:
            matrixEntries = list(map(int,rawLine.split(",")))
            self.matrix.append(matrixEntries)
        self.numNodes = len(self.matrix)
        self.validateMatrix()
        self.dimensionNetwork()

    def validateMatrix(self):
        """
        Checks whether the adjacency matrix is valid.  It should be square,
        and all entries should be 0 or 1.
        """
        numRows = len(self.matrix)
        for row in self.matrix:
            if len(row) != numRows:
                print("Error: Network adjacency matrix must be square.")
                raise BadNetworkException
            for entry in row:
                if entry not in [0, 1]:
                    print("Error: Network matrix must have 0 or 1 entries.")
                    raise BadNetworkException

    def dimensionNetwork(self):
        self.cost = list()
        self.capacity = list()
        for i in range(self.numNodes):
            self.cost.append([0] * self.numNodes)
            self.capacity.append([0] * self.numNodes)
        self.supply = [0] * self.numNodes

    def readLinkDataFile(self, linkDataFileName):
        """
        Reads link data from a given file.  Format of this file is a series
        of rows, one for each link:

        tail,head,cost,capacity
        """
        linkLines = utils.processFile(linkDataFileName)
        for link in linkLines:
            try:
                tail, head, cost, capacity = link.split(",")
                tail = int(tail)
                head = int(head)
                if (tail < 0 or tail >= self.numNodes
                        or head < 0 or head >= self.numNodes
                        or self.matrix[tail][head] != 1):
                    raise BadNetworkException
                self.cost[tail][head] = float(cost)
                self.capacity[tail][head] = float(capacity)
            except:
                print("Row %s in link file does not correspond to a valid"
                      "link." % link)
                raise BadNetworkException

    def readNodeDataFile(self, nodeDataFileName):
        """
        Reads node data from a given file.  Format of this file is a series
        of rows, one for each node:

        node,supply

        where negative supply indicates a sink (net demand)
        """
        nodeLines = utils.processFile(nodeDataFileName)
        for node in nodeLines:
            try:
                node, supply = split(link,",")
                node = int(node)
                if (node < 0 or node >= self.numNodes):
                    raise BadNetworkException
                self.supply[node] = float(supply)
            except:
                print("Row %s in node file does not correspond to a valid"
                      "node." % node)
                raise BadNetworkException

