import pygeoda

snow = pygeoda.open("/Users/xun/github/pygeoda_lixun910/perf/data/deaths_nd_by_house.shp")
v = snow.GetIntegerCol("death_dum")
d20 = pygeoda.weights.distance_weights(snow, dist_thres=20)
print(d20)
snowjc = pygeoda.local_joincount(d20, v, permutations=99999, significance_cutoff=0.01)
snowsig = snowjc.lisa_clusters()
pval = snowjc.lisa_pvalues()
print(sum(snowsig))