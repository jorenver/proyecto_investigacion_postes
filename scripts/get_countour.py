from osgeo import gdal
from skimage.morphology import erosion
from skimage.morphology import black_tophat, skeletonize, convex_hull_image
from skimage.morphology import disk
#import tifffile as tiff
import sys
from scipy import ndimage
import numpy as np

#filename = sys.argv[1]
#dst_filename=sys.argv[2]
filename="raster_intersects_recortado.tif"
dst_filename="raster_intersects_recortado_dist.tif"
raster =gdal.Open(filename)
#img = tiff.imread(filename)
band = raster.GetRasterBand(1)
img = band.ReadAsArray()
#tiff.imsave('test.tif',np.float32(img))
selem = disk(1)
eroded = erosion(img, selem)
distance_img = ndimage.distance_transform_edt(eroded)
#tiff.imsave('distance_img',np.float32(distance_img))

# georeference the image and set the projection
driver = gdal.GetDriverByName('GTiff')
y_pixels=len(distance_img)
x_pixels=len(distance_img[0])
dataset = driver.Create(dst_filename,x_pixels,y_pixels,1,gdal.GDT_Float32, )
transform= raster.GetGeoTransform()
proyection=raster.GetProjection()
dataset.SetProjection(proyection)
dataset.setTramsform(transform)
dataset.GetRasterBand(1).WriteArray(distance_img)
dataset.FlushCache()  # Write to disk.
