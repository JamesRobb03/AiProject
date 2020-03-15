#
# Network - Shortest Path. G(10823, 174977). Diam: avg:0.94  eff:0.89  max:1 (Sun Mar 15 17:08:40 2020)
#

set title "Network - Shortest Path. G(10823, 174977). Diam: avg:0.94  eff:0.89  max:1"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'diam.Example.png'
plot 	"diam.Example.tab" using 1:2 title "" with linespoints pt 6
