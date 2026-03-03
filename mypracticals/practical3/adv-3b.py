from qgis.core import QgsRasterLayer, QgsProject, QgsPointXY
print("Name:Shishpal Rawat\n roll n:255601")
# Load Raster Layer
raster_path = "C:/Users/SHISHPAL/Downloads/Practical 3-20251205T122933Z-1-001/Practical 3/ind_population_2024.tif"
rl = QgsRasterLayer(raster_path, "India_PopDensity")

if not rl.isValid():
    print("Raster failed to load")
else:
    QgsProject.instance().addMapLayer(rl)
    print("Raster loaded:", rl.name())
    print("Extent:", rl.extent().toString())
    print(f"Width x Height (px): {rl.width()} x {rl.height()}") 
    print("Bands:", rl.bandCount())

    dp = rl.dataProvider()
    # statistics for band 1
    stats = dp.bandStatistics(1)
    
    # *** MODIFIED LINE: NO PARENTHESES on the statistics functions ***
    print(f"Min: {stats.minimumValue}, Max: {stats.maximumValue}, Mean: {stats.mean}")