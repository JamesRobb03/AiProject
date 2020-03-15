#
# Network - k-core nodes. G(10823, 174977). (Sun Mar 15 17:08:40 2020)
#

set title "Network - k-core nodes. G(10823, 174977)."
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "k-Core"
set ylabel "Number of nodes in the k-Core"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'coreNodes.KCoreNodes.png'
plot 	"coreNodes.KCoreNodes.tab" using 1:2 title "" with linespoints pt 6
