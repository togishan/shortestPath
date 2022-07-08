


# [A,C,[A,B,5],[B,C,23],[D,A,11],[A,E,2],[D,E,5],[E,C,5],[A,C,35]]




from cmath import e


def Nodes(lst):
    nodes={}
    count=0
    for i in range(len(lst)):
        if lst[i][0] not in nodes:
            nodes[lst[i][0]]=count
            count+=1
        if lst[i][1] not in nodes:
            nodes[lst[i][1]]=count
            count+=1
    return nodes


def adjacencyMatrix(edges):
    nodes=Nodes(edges)
    
    matrix=[[ "-" for i in range(len(nodes))] for i in range(len(nodes))]

    for i in range(len(edges)):

        matrix[nodes[edges[i][0]]][nodes[edges[i][1]]]=edges[i][2]
        matrix[nodes[edges[i][1]]][nodes[edges[i][0]]]=edges[i][2]
    return matrix
    


def findMin(lst,marked_lst):
    min_value=-1
    min_index=-1
    
    for i in range(len(lst)):
        if marked_lst[i]==False:
            if min_value==-1:
                min_value=lst[i]
                min_index=i
            else:
                if lst[i]!=-1 and min_value>lst[i]:
                    min_value=lst[i]
                    min_index=i
    return min_index



def shortestPath(_input):
    matrix=adjacencyMatrix(_input[2:])
    nodes=Nodes(_input[2:])
    start=nodes[_input[0]]
    end=nodes[_input[1]]

    current=start
    previous_nodes=["-" for i in range(len(nodes))]
    distances=[-1 for i in range(len(nodes))]
    marked=[False for i in range(len(nodes))]
    distances[current]=0
    
    
    
    while False in marked:
        
        for i in range(len(matrix)):
        
            if i!=current:
                if matrix[current][i]!="-" :
                    if distances[i]==-1 or distances[i]>matrix[current][i]+distances[current]:
                        distances[i]=matrix[current][i]+distances[current]
                        previous_nodes[i]=current                    
        marked[current]=True
        current=findMin(distances,marked)

    path=""
    
    distance=distances[end]



    while previous_nodes[end]!="-":
        path= list(nodes.keys())[end]+" - "+path
        end=previous_nodes[end]
        
    return "Path: " + list(nodes.keys())[start] +" - "+path[:-3]+"\n"+"Distance: " +str(distance)



