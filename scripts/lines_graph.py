import shapefile
import csv
file_path="/Users/jorge/Documents/CVR/proyecto_investigacion/data/grafo_distancia.csv"
postes_path_shp="/Users/jorge/Documents/CVR/proyecto_investigacion/data/postes_2/postes_2.shp"
postes_path_dbf="/Users/jorge/Documents/CVR/proyecto_investigacion/data/postes_2/postes_2.dbf"
postes_sph=open(postes_path_shp, "rb")
postes_dbf=open(postes_path_dbf, "rb")
postes= shapefile.Reader(shp=postes_sph, dbf=postes_dbf)
new_shapefile_path="/Users/jorge/Documents/CVR/proyecto_investigacion/data/postes_2/gaph_lines"
postes_hash={}

def objetc_line(origin,destination):
    result = []
    line=[]
    line.append(origin)
    line.append(destination)
    result.append(line)
    return result

print("creando diccionario....")
for p in postes.shapeRecords():
    global_id = p.record[27]
    postes_hash[global_id]=p
print("creando lines....")
with open(file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    new_shapefile = shapefile.Writer(shapefile.POLYLINE)
    new_shapefile.field("InputID", 'C')
    new_shapefile.field("TargetID", 'C')
    for row in reader:
        origin_id=row['InputID']
        destination_id=row['TargetID']
        print("origin_id:", origin_id)
        print("destination_id:", destination_id)
        origin=postes_hash[origin_id]
        destination = postes_hash[destination_id]
        points_line=objetc_line(origin.shape.points[0],destination.shape.points[0])
        print("line: ",points_line)
        new_shapefile.record(origin_id,destination_id)
        new_shapefile.line(parts=points_line)
    new_shapefile.save(new_shapefile_path)
