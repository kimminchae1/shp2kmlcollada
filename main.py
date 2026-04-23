import os
from core.shp_reader import read_shp
from core.transformer import get_transformer, to_wgs84
from core.kml_writer import load_template, write_kml
from core.utils import clean_xml
from tqdm import tqdm

# SHP 파일을 읽어 객체별 KML 파일을 생성

# 경로 및 원본 좌표계 설정
shp_path = "../input/shp_test/RDL_TREE_PS_TEST"
output_dir = "../output/kml"
template_path = "template.kml"
EPSG = 5187

# 출력 폴더 생성 
os.makedirs(output_dir, exist_ok=True)

# 좌표변환 및 템플릿 준비
transformer = get_transformer(EPSG) # 5187 -> 4326
template = load_template(template_path)

total = len(list(read_shp(shp_path)))

# 실행
# shape : 공간 정보 (좌표, geometry) // attrs : 속성 정보 (컬럼 값)
for i, (shape, attrs) in enumerate(tqdm(read_shp(shp_path), total=total, desc="KML 생성 중")):
    
    # 테스트
    # if i >= 10:
    #   break

    if not shape.points:
        continue

    # geometry 좌표 → WGS84 경위도 변환
    x, y = shape.points[0]
    lon, lat = to_wgs84(transformer, x, y)

    name = f"tr_{i+1}"
    href = f"{name}.dae"
    # href = "tree.dae"

    # XML 안전 처리
    safe_attrs = {k: clean_xml(v) for k, v in attrs.items()}

    data = {
        "name": name,
        "longitude": lon,
        "latitude": lat,
        "altitude": 0,
        "href": href,
        **safe_attrs
    }

    output_path = os.path.join(output_dir, f"{name}.kml")
    write_kml(output_path, template, data)

print("완료")