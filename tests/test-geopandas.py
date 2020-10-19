import unittest
import pygeoda
import geopandas
import matplotlib
import matplotlib.pyplot as plt
import os

__author__ = "Hang Zhang <zhanghanggis@163.com>, "

class Testgeopandas(unittest.TestCase):
    def setUp(self):
        self.gdf = geopandas.read_file("./data/Guerry.shp")
        self.guerry = pygeoda.geopandas_to_geoda(self.gdf)
        self.queen_w = pygeoda.weights.queen(self.guerry)
        self.crm_prp = self.gdf.Crm_prs.to_list() 
        self.data = [self.gdf.Crm_prs.to_list(),self.gdf.Crm_prp.to_list(),self.gdf.Litercy.to_list(),self.gdf.Donatns.to_list(),self.gdf.Infants.to_list(),self.gdf.Suicids.to_list()]
        self.bound_vals = self.gdf.Pop1831.to_list()

    def test_LISA_ClusterMap(self):
        crm_lisa = pygeoda.local_moran(self.queen_w,self.crm_prp)
        fig, ax = plt.subplots(figsize = (10,10))
        lisa_colors = crm_lisa.GetColors()
        lisa_labels = crm_lisa.GetLabels()

        # attach LISA cluster indicators to geodataframe
        self.gdf['LISA'] = crm_lisa.GetClusterIndicators()

        for ctype, data in self.gdf.groupby('LISA'):
            color = lisa_colors[ctype]
            lbl = lisa_labels[ctype]
            data.plot(color = color,
                ax = ax,
                label = lbl,
                edgecolor = 'black',
                linewidth = 0.2)

        # Place legend in the lower right hand corner of the plot
        # Place legend in the lower right hand corner of the plot
        lisa_legend = [matplotlib.lines.Line2D([0], [0], color=color, lw=2) for color in lisa_colors]
        ax.legend(lisa_legend, lisa_labels,loc='lower left', fontsize=12, frameon=True)
        ax.set(title='Local Moran Cluster Map of Crm_prp\n Population per Crime against persons')
        ax.set_axis_off()

    def test_LISA_PMap(self):
        crm_lisa = pygeoda.local_moran(self.queen_w,self.crm_prp)
        fig, ax = plt.subplots(figsize = (10,10))

        # attach LISA cluster indicators to geodataframe
        self.gdf['LISA_PVAL'] = crm_lisa.GetPValues()
        fig, ax = plt.subplots(figsize = (10,10))
        self.gdf.plot(color='#eeeeee', ax=ax, edgecolor = 'black', linewidth = 0.2)
        self.gdf[self.gdf['LISA_PVAL'] <= 0.05].plot(color="#84f576", ax=ax)
        self.gdf[self.gdf['LISA_PVAL'] <= 0.01].plot(color="#53c53c", ax=ax)
        self.gdf[self.gdf['LISA_PVAL'] <= 0.001].plot(color="#348124", ax=ax)
        ax.set(title='Local Moran Significance Map of Crm_prp\n Population per Crime against persons')
        ax.set_axis_off()

    def test_geary_ClusterMap(self):
        crm_geary = pygeoda.local_geary(self.queen_w, self.crm_prp)
        fig, ax = plt.subplots(figsize = (10,10))
        lisa_colors = crm_geary.GetColors()
        lisa_labels = crm_geary.GetLabels()

        # attach LISA cluster indicators to geodataframe
        self.gdf['GEARY'] = crm_geary.GetClusterIndicators()

        for ctype, data in self.gdf.groupby('GEARY'):
            color = lisa_colors[ctype]
            lbl = lisa_labels[ctype]
            data.plot(color = color,
                ax = ax,
                label = lbl,
                edgecolor = 'black',
                linewidth = 0.2)

        # Place legend in the lower right hand corner of the plot
        lisa_legend = [matplotlib.lines.Line2D([0], [0], color=color, lw=2) for color in lisa_colors]
        ax.legend(lisa_legend, lisa_labels,loc='lower left', fontsize=12, frameon=True)
        ax.set(title='Local Geary Cluster Map of Crm_prp\n Population per Crime against persons')
        ax.set_axis_off()

    def test_local_gMap(self):
        crm_g = pygeoda.local_g(self.queen_w, self.crm_prp)
        fig, ax = plt.subplots(figsize = (10,10))
        lisa_colors = crm_g.GetColors()
        lisa_labels = crm_g.GetLabels()

        # attach LISA cluster indicators to geodataframe
        self.gdf['GO'] = crm_g.GetClusterIndicators()

        for ctype, data in self.gdf.groupby('GO'):
            color = lisa_colors[ctype]
            lbl = lisa_labels[ctype]
            data.plot(color = color,
                ax = ax,
                label = lbl,
                edgecolor = 'black',
                linewidth = 0.2)

        # Place legend in the lower right hand corner of the plot
        lisa_legend = [matplotlib.lines.Line2D([0], [0], color=color, lw=2) for color in lisa_colors]
        ax.legend(lisa_legend, lisa_labels,loc='lower left', fontsize=12, frameon=True)
        ax.set(title='Local Getis-Ord G Cluster Map of Crm_prp\n Population per Crime against persons')
        ax.set_axis_off()


    def test_SKATERMap(self):
        skater_clusters = pygeoda.skater(4, self.queen_w, self.data)
        flat_clusters = [0] * self.guerry.num_obs
        for cid, cluster in enumerate(skater_clusters):
             for idx in cluster:
                flat_clusters[idx] = cid
        self.gdf['SKATER_C'] = flat_clusters
        fig, ax = plt.subplots(figsize = (8,10))
        self.gdf.plot(column="SKATER_C", ax=ax, edgecolor = 'black', linewidth = 0.2, cmap="Pastel1")
        ax.set(title="SKATER Clustering Map")
        ax.set_axis_off() 


    def Mac_p_ClusterMap(self):
        min_bound = 3236.67 # 10% of Pop1831
        maxp_clusters = pygeoda.maxp(self.queen_w, self.data, self.bound_vals, min_bound, "greedy")
        for cid, cluster in enumerate(maxp_clusters):
            for idx in cluster:
                maxp_clusters[idx] = cid
        self.gdf['MAXP_C'] = maxp_clusters
        fig, ax = plt.subplots(figsize = (8,10))
        self.gdf.plot(column="MAXP_C", ax=ax, edgecolor = 'black', linewidth = 0.2, cmap="Pastel1")
        ax.set(title="Max-p Clustering Map")
        ax.set_axis_off()


