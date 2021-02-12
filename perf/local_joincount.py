import pygeoda
import time

snow = pygeoda.open("/Users/xun/Github/pygeoda_lixun910/perf/data/deaths_nd_by_house.shp")
w20 = pygeoda.weights.distance(snow, 20.0)
x = snow.GetIntegerCol("death_dum")

start_time = time.time()
lisa = pygeoda.local_joincount(w20, x, permutations=99999, cpu_threads=6)

print("--- %s seconds ---" % (time.time() - start_time))

pvals = lisa.lisa_pvalues()
print(pvals)
