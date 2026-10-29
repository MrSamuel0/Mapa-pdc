import folium
import geopandas as gpd

def MapVisualization(filepath: str, outname: str):

  mapa = gpd.read_file(filepath)

  if mapa.crs != "EPSG:4326":
    mapa = mapa.to_crs(epsg=4326)

  centroid = mapa.geometry.unary_union.centroid
  lat, lon = centroid.y, centroid.x

  m = folium.Map(location=[lat, lon], zoom_start=16)

  folium.GeoJson(
      mapa,
      style_function=lambda x: {
          "fillColor": "#3186cc",
          "color": "#1f4e79",
          "weight": 2,
          "fillOpacity": 0.6,
      },
  ).add_to(m)

  m.save(f"./output/{outname}.html")

  return f"Operation Successful: Interactive map saved to: {outname}"