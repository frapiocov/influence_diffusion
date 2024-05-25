import snap

print("----- vector ----- ")

v = snap.TIntV()

v.append(1)
v.append(2)
v.append(3)
v.append(4)
v.append(5)

print(len(v))
print(v[2])

v[2] = 2*v[2]
print(v[2])

for item in v:
    print(item)

for i in range(0, len(v)):
    print(i, v[i])

print("----- hash table ----- ")

h = snap.TIntStrH()

h[5] = "apple"
h[3] = "orange"
h[9] = "plum"
h[6] = "mango"
h[1] = "banana"

print(h.Len())

print("h[3] =", h[3])

h[3] = "apricot"
print("h[3] =", h[3])

for key in h:
    print(key, h[key])

print("----- pair ----- ")

p = snap.TIntStrPr(1, "one");

print(p.GetVal1())
print(p.GetVal2())

print("----- graphs ----- ")

G1 = snap.TUNGraph.New()
G2 = snap.TNGraph.New()
N1 = snap.TNEANet.New()

G1.AddNode(1)
G1.AddNode(5)
G1.AddNode(32)

G1.AddEdge(1,5)
G1.AddEdge(5,1)
G1.AddEdge(5,32)

# create a directed random graph on 100 nodes and 1k edges
G2 = snap.GenRndGnm(snap.PNGraph, 100, 1000)
print("G2: Nodes %d, Edges %d" % (G2.GetNodes(), G2.GetEdges()))

# traverse the nodes
for NI in G2.Nodes():
    print("node id %d with out-degree %d and in-degree %d" % (
        NI.GetId(), NI.GetOutDeg(), NI.GetInDeg()))
# traverse the edges
for EI in G2.Edges():
    print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

# traverse the edges by nodes
for NI in G2.Nodes():
    for Id in NI.GetOutEdges():
        print("edge (%d %d)" % (NI.GetId(), Id))

# save and load binary
FOut = snap.TFOut("test.graph")
G2.Save(FOut)
FOut.Flush()
FIn = snap.TFIn("test.graph")
G4 = snap.TNGraph.Load(FIn)
print("G4: Nodes %d, Edges %d" % (G4.GetNodes(), G4.GetEdges()))

# save and load from a text file
snap.SaveEdgeList(G4, "test.txt", "Save as tab-separated list of edges")
G5 = snap.LoadEdgeList(snap.PNGraph, "test.txt", 0, 1)
print("G5: Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges()))

# create a directed random graph on 10k nodes and 5k edges
G6 = snap.GenRndGnm(snap.PNGraph, 10000, 5000)
print("G6: Nodes %d, Edges %d" % (G6.GetNodes(), G6.GetEdges()))
# convert to undirected graph
G7 = G6.ConvertGraph(snap.TUNGraph)
print("G7: Nodes %d, Edges %d" % (G7.GetNodes(), G7.GetEdges()))
# get largest weakly connected component
WccG = G6.GetMxWcc()

# generate a network using Forest Fire model
G8 = snap.GenForestFire(1000, 0.35, 0.35)
print("G8: Nodes %d, Edges %d" % (G8.GetNodes(), G8.GetEdges()))

# get a subgraph induced on nodes [0,1,2,3,4]
SubG = G8.GetSubGraph([0,1,2,3,4])

# get 3-core of G8
Core3 = G8.GetKCore(3)
print("Core3: Nodes %d, Edges %d" % (Core3.GetNodes(), Core3.GetEdges()))

# delete nodes of out degree 3 and in degree 2
G8.DelDegKNodes(3, 2)

# create a directed random graph on 10k nodes and 1k edges
G9 = snap.GenRndGnm(snap.PNGraph, 10000, 1000)
print("G9: Nodes %d, Edges %d" % (G9.GetNodes(), G9.GetEdges()))

# define a vector of pairs of integers (size, count) and
# get a distribution of connected components (component size, count)
CntV = G9.GetWccSzCnt()
for p in CntV:
    print("size %d: count %d" % (p.GetVal1(), p.GetVal2()))

# get degree distribution pairs (out-degree, count):
CntV = G9.GetOutDegCnt()
for p in CntV:
    print("degree %d: count %d" % (p.GetVal1(), p.GetVal2()))

# generate a Preferential Attachment graph on 100 nodes and out-degree of 3
G10 = snap.GenPrefAttach(100, 3)
print("G10: Nodes %d, Edges %d" % (G10.GetNodes(), G10.GetEdges()))

# define a vector of floats and get first eigenvector of graph adjacency matrix
EigV = G10.GetLeadEigVec()
nr = 0
for f in EigV:
    nr += 1
    print("%d: %.6f" % (nr, f))

# get an approximation of graph diameter
diam = G10.GetBfsFullDiam(10)
print("diam", diam)

# count the number of triads:
triads = G10.GetTriads()
print("triads", triads)

# get the clustering coefficient
cf = G10.GetClustCf()
print("cf", cf)
