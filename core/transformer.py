from pyproj import Transformer

# 입력좌표계(5187) -> 출력좌표계(4326)
def get_transformer(src_epsg):
    return Transformer.from_crs(f"EPSG:{src_epsg}", "EPSG:4326", always_xy=True)

def to_wgs84(transformer, x, y):
    lon, lat = transformer.transform(x, y)
    return lon, lat