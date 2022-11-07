        import heapdict
        self.initPygame()


        open_set = heapdict.heapdict()
        closed_set = []

        # Check to see that startvertex is in Graph
        if startVertexName not in self.vertecies:
            raise KeyError("Start node not present in graph")
        # Reset visited and previous pointer before running algorithm
        current = self.vertecies[startVertexName]
        current.distance = distance = weight = 0
        
        previous_node = None
        startNode = self.vertecies[startVertexName]
        toNode = self.vertecies[targetVertexName]
        current.g = 0
        current.h = self.heuristics(current.name, targetVertexName=targetVertexName)
        current.f = current.g + current.h
        open_set[current] = current.f

        while open_set:
            current = open_set.popitem()[0]
            self.pygameState(current, self.GREEN)
            self.pygameState(startNode, self.BLUE)
            self.pygameState(toNode, self.RED)
            
            if current.name == targetVertexName:
                break
            closed_set.insert(0, current)
            for adjacentedge in current.adjecent:
                if adjacentedge.vertex not in open_set:
                    if not adjacentedge.vertex in closed_set:
                        adjacentedge.vertex.previous = current
                        adjacentedge.vertex.g = current.g + adjacentedge.weight
                        adjacentedge.vertex.h = self.heuristics(adjacentedge.vertex.name, targetVertexName=targetVertexName)
                        adjacentedge.vertex.f = adjacentedge.vertex.g + adjacentedge.vertex.h
                        open_set[adjacentedge.vertex] = adjacentedge.vertex.f
                        self.pygameState(adjacentedge.vertex, self.PINK)
                    else:
                        if adjacentedge.vertex.g > current.g + adjacentedge.weight:
                            adjacentedge.vertex.previous = current
                            adjacentedge.vertex.g = current.g + adjacentedge.weight
                            adjacentedge.vertex.f = adjacentedge.vertex.g + adjacentedge.vertex.h
                            
    
                        if adjacentedge.vertex in closed_set:
                            test = closed_set.pop()
                            open_set[test] = test.f
                        