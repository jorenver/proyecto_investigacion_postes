import shapefile

path_shp_sectores="/Users/jorge/Documents/CVR/proyecto_investigacion/data/SECTORES_CNEL/SECTORES_CENEL.shp"
path_dbf_sectores="/Users/jorge/Documents/CVR/proyecto_investigacion/data/SECTORES_CNEL/SECTORES_CENEL.dbf"
sf_sectores=open(path_shp_sectores, "rb")
db_sectores=open(path_dbf_sectores, "rb")
sectores= shapefile.Reader(shp=sf_sectores, dbf=db_sectores)

path_shp_manzanas="/Users/jorge/Documents/CVR/proyecto_investigacion/data/INTERSECTS/INTERSECTS.shp"
path_dbf_manzanas="/Users/jorge/Documents/CVR/proyecto_investigacion/data/INTERSECTS/INTERSECTS.dbf"
sf_manzanas=open(path_shp_manzanas, "rb")
db_manzanas=open(path_dbf_manzanas, "rb")
manzanas= shapefile.Reader(shp=sf_manzanas, dbf=db_manzanas)


for m in manzanas.iterShapes():
    print(m.points)


