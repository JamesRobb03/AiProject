import snap
import csv
import hashlib
import graphviz

#Function which converts string to an ID
def hashName(string):
	h = hashlib.md5()
	h.update(string.encode("utf-8"))
	return int(str(int(h.hexdigest(), 16))[2:11])

#Creating new network
N1 = snap.TNEANet.New()

#list for labels.
labelList = []
#list for nodes
NodeList = []

#Change this value to determine how many drugs are used (up to 640)
AmountOfDrugNodes = 4

#Adding nodes and edges to network by reading the CSV
with open("dataset.csv", "r") as file:
	reader = csv.reader(file)
	header = next(reader)
	drugNodeCount = 0
	sideEffectCount = 0
	#Loops through all entries in csv file
	for row in reader:

		if drugNodeCount <= AmountOfDrugNodes:

			#Adds a drug node and a side effect node
			drugNode = row[0]
			nodeID = hashName(drugNode)
			
			try:
				#add drug node
				dataReturn = N1.AddNode(nodeID)
				drugNodeCount = drugNodeCount + 1
				if drugNodeCount>AmountOfDrugNodes:
					N1.DelNode(nodeID)
					break
				print "Succesfully added Drug Node - {0} ID: {1}".format(row[0], nodeID)
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
	
	print "Drug Nodes : {0} , Side Effect Nodes : {1}".format(drugNodeCount-1, sideEffectCount)



#function which draws a neato graph for a network
def drawGraph(network, listOfLabels, graphName, graphDesc):
	labels = snap.TIntStrH()
	i=0
	for NI in network.Nodes():
		labels[NI.GetId()] = listOfLabels[i]
		i = i+1

	snap.DrawGViz(network, snap.gvlNeato, graphName, graphDesc, labels)

def colourGraph(graphName):
	with open("{0}.dot".format(graphName), 'r') as dotFile:
		with open("{0}colour.dot".format(graphName), 'w') as outFile:
			i = 0;
			for line in dotFile:
				if '[label="' in line:
					nodeID = NodeList[i]
					NodePointer = N1.GetNI(NodeList[i])
					inDegree = NodePointer.GetInDeg()

					if inDegree == 0:
						outFile.write('	{0} [label = "{1}", style=filled, fillcolor="{2}"];\n'.format(nodeID, labelList[i], "#b8e8a2")) 
					elif inDegree == 1:
						outFile.write('	{0} [label = "{1}", style=filled, fillcolor="{2}"];\n'.format(nodeID, labelList[i], "#ffdede")) 
					elif inDegree == 2:
						outFile.write('	{0} [label = "{1}", style=filled, fillcolor="{2}"];\n'.format(nodeID, labelList[i], "#ff9696")) 
					else:
						outFile.write('	{0} [label = "{1}", style=filled, fillcolor="{2}"];\n'.format(nodeID, labelList[i], "#ff2b2b")) 

					i = i+1
				else:
					outFile.write(line)

	graphviz.render('neato', 'png', "{0}colour.dot".format(graphName))




#For Harry
def findMostCommonDrug(network, numberOfSideEffects):
	position = 0
	i = 0
	largestDegree = 0

	topSideEffectList = []

	for NI in network.Nodes():
		NodePointer = network.GetNI(NodeList[i])
		inDegree = NodePointer.GetInDeg()
		if inDegree>largestDegree:
			largestDegree = inDegree
			position = i
		
		i=i+1  

	topSideEffectList.append(labelList[position])

	j = 0
	while topSideEffectList.len() < numberOfSideEffects:
		NodePointer = network.GetNI(NodeList[i])
		inDegree = NodePointer.GetInDeg()
		



	print "Most common side effect : {0} - With in degree of {1}".format(labelList[position], largestDegree)


#Calling function above that draws a graph.
drawGraph(N1, labelList, "GraphOf4Drugs.png", "A graph of 4 drugs and their side effects")
print "RENDERED BLACK AND WHITE "
colourGraph("GraphOf4Drugs")