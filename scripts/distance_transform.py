from osgeo import gdal


raster =gdal.Open("raster_intersects_recortado.tif")
band = raster.GetRasterBand(1)
sec_gye = band.ReadAsArray()


