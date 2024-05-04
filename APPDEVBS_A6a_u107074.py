import geopandas as gpd

# Load the shapefile
shapefile_path = "stm_arrets_sig.shp"
gdf = gpd.read_file(shapefile_path)

# Filter the dataframe based on specific code
ass6a_q1 = "50117"
filtered_gdf = gdf[gdf['stop_name'] == ass6a_q1]

# Print the station names with the specific code
print(filtered_gdf['station_name_column_name'])





import geopandas as gpd
import pyproj
from shapely.ops import transform
from shapely.geometry import Point

# Function to load shapefile and filter dataframe based on stop code
def filter_shapefile_by_stop_code(stop_code):
    stm_arrets_sig_path = "stm_arrets_sig.shp"
    gdf = gpd.read_file(stm_arrets_sig_path)
    print(gdf)
    print(gdf['stop_code'])

    # Filter the dataframe based on specific code
    filtered_gdf = gdf[gdf['stop_code'] == stop_code]

    # Print the station names with the specific code
    print(filtered_gdf['stop_name'])

# Function to count transit routes and their occurrences
def count_transit_routes():
    stm_lignes_sig_path = "stm_lignes_sig.shp"
    gdf = gpd.read_file(stm_lignes_sig_path)

    transit_route_nr = gdf["route_id"].nunique()
    print(transit_route_nr)

    # Count occurrences of each transit route
    route_counts = gdf['route_name'].value_counts()

    # Print the counts
    print(route_counts)

# Function to transform coordinates
def transform_coordinates():
    # Your coordinates to transform
    coordinate = (364051.75, 4109976.75)

    originalcrs = pyproj.CRS("EPSG:4326")
    targetcrs = pyproj.CRS("EPSG:32188")

    project = pyproj.Transformer.from_crs(targetcrs, originalcrs, always_xy=True).transform

    # Transform the coordinate
    transformed_point = transform(project, Point(coordinate))
    REFPOINT = transformed_point
    print(REFPOINT)

# Call the functions
filter_shapefile_by_stop_code(50117)
count_transit_routes()
transform_coordinates()

buffer_distance = 0.5
buffered_line = line.buffer(buffer_distance) # which will generate a buffer with the defined distance around the point.
