#Read in CSV.
#ADD Nodes.
#ADD Edges.
#Visualise graph
import snap
import csv
import hashlib

#Function which converts string to an ID
def hashName(string):
	h = hashlib.md5()
	h.update(string.encode("utf-8"))
	return int(str(int(h.hexdigest(), 16))[2:11])

#Creating new network
N1 = snap.TNEANet.New()

#Adding nodes and edges to network by reading the CSV
with open("dataset.csv", "r") as file:
	reader = csv.reader(file)
	header = next(reader)
	drugNodeCount = 0
	sideEffectCount = 0
	for row in reader:

		if drugNodeCount < 4:

			#Adds a drug node and a side effect node
			drugNode = row[0]
			nodeID = hashName(drugNode)
			
			try:
				#add drug node
				dataReturn = N1.AddNode(nodeID)
				print "Succesfully added Drug Node - {0} ID: {1}".format(row[0], nodeID)
				drugNodeCount = drugNodeCount + 1
			except Exception as e:
				#duplicate drug node
				pass

			sideEffectNode = row[1]
			SEnodeID = hashName(sideEffectNode)
			try:
				#add side effect node
				dataReturn = N1.AddNode(SEnodeID)
				print "Succesfully added Side Effect Node - {0} ID: {1}".format(row[1], SEnodeID)
				sideEffectCount = sideEffectCount + 1
			except Exception as e:
				#duplicate side effect node
				pass


			try:
				#Adds an edge between a drug node and a side effect node
				dataReturn = N1.AddEdge(nodeID, SEnodeID, -1)
				print "Succesfully added edge between {0} and {1}".format(nodeID, SEnodeID)
			except Exception as e:
				pass

		else:
			break

		#Adds an edge between a drug node and a side effect node

	
	print "Drug Nodes : {0} , Side Effect Nodes : {1}".format(drugNodeCount, sideEffectCount)



#Saving graph to text file
snap.SaveEdgeList(N1, "DrugSideEffectEdgelist.txt", "Save as tab-separated list of edges")

#snap.PlotShortPathDistr(N1, "Example", "Network - Shortest Path")
#snap.PlotKCoreNodes(N1, "KCoreNodes", "Network - k-core nodes")

#graph
labels = snap.TIntStrH()
for NI in N1.Nodes():
	labels[NI.GetId()] = str(NI.GetId())
snap.DrawGViz(N1, snap.gvlNeato, "graph.png", "a graph of the drug side effect network.",labels)





#Loop through csv and add all nodes that it contains.
#use if statement to loop through and try and add all nodes.
#once all nodes have been added add all edges.
#try and work out attributes.

#display graph.