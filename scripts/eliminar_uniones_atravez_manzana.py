ruta_imagen="/Users/jorge/Documents/CVR/proyecto_investigacion/data/GYE_PROJ_DIS"
from osgeo import gdal,ogr
import struct


def get_pixel_value(img,px,py):
    structval = img.ReadRaster(px, py, 1, 1, buf_type=gdal.GDT_UInt16)  # Assumes 16 bit int aka 'short'
    intval = struct.unpack('h', structval)  # use the 'short' format code (2 bytes) not int (4 bytes)
    return intval[0]

def get_value_coordinate(geoTransform,img,cordX, cordY):
    px = int((cordX - geoTransform[0]) / geoTransform[1])  # x pixel
    py = int((cordY - geoTransform[3]) / geoTransform[5])  # y pixel
    return get_pixel_value(img,px,py)

valor_corte=18
src_ds=gdal.Open(ruta_imagen)
gt=src_ds.GetGeoTransform()
img_dist=src_ds.GetRasterBand(1)

mx=614323.3
my=9769245.5
pixel_value=get_value_coordinate(gt,img_dist,mx,my)
print(pixel_value)



