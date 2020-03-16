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

#list for labels.
labelList = []

NodeList = []

#Adding nodes and edges to network by reading the CSV
with open("dataset.csv", "r") as file:
	reader = csv.reader(file)
	header = next(reader)
	drugNodeCount = 0
	sideEffectCount = 0
	for row in reader:

		if drugNodeCount < 500:

			#Adds a drug node and a side effect node
			drugNode = row[0]
			nodeID = hashName(drugNode)
			
			try:
				#add drug node
				dataReturn = N1.AddNode(nodeID)
				print "Succesfully added Drug Node - {0} ID: {1}".format(row[0], nodeID)
				drugNodeCount = drugNodeCount + 1
				labelList.append(row[0])
				NodeList.append(nodeID)

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
				labelList.append(row[2])
				NodeList.append(SEnodeID)
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
	
	print "Drug Nodes : {0} , Side Effect Nodes : {1}".format(drugNodeCount, sideEffectCount)



#graph
#labels = snap.TIntStrH()
#i=0
#for NI in N1.Nodes():
#	labels[NI.GetId()] = labelList[i]
#	i = i+1
#snap.DrawGViz(N1, snap.gvlNeato, "graph.png", "a graph of the drug side effect network.", labels)

#I want to loop through the lists and find which side effect is most common
#InDegV = snap.TIntPrV()
#s#nap.GetNodeInDegV(N1, InDegV)
#for item in InDegV:
#    print("node ID %d: in-degree %d" % (item.GetVal1(), item.GetVal2()))

position = 0
i = 0
largestDegree = 0

for NI in N1.Nodes():
	NodePointer = N1.GetNI(NodeList[i])
	inDegree = NodePointer.GetInDeg()
	if inDegree>largestDegree:
		largestDegree = inDegree
		position = i
	#print "{0} has in degree {1}".format(NodeList[i], inDegree)
	i=i+1  

print "Most common side effect : {0} - With in degree of {1}".format(labelList[position], largestDegree)