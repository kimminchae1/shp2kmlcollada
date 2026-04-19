import shapefile
from pyproj import Transformer
import os

# 경로 설정
shp_path = "../input/shp/RDL_TREE_PS.shp"
template_path = "template.kml"
output_dir = "../output/kml"

# 좌표계
SRC_EPSG = "EPSG:5187"   # SHP 좌표계
DST_EPSG = "EPSG:4326"   # KML 좌표계

os.makedirs(output_dir, exist_ok=True)

# SHP 읽기
sf = shapefile.Reader(shp_path)

# 필드명 가져오기 (첫 번째 DeletionFlag 제외)
fields = [f[0] for f in sf.fields[1:]]

# 좌표 변환기
transformer = Transformer.from_crs(SRC_EPSG, DST_EPSG, always_xy=True)

# 템플릿 읽기
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

# 반복 처리
for i, (shape, record) in enumerate(zip(sf.shapes(), sf.records())):

    # 좌표 추출 (Point 기준)
    x, y = shape.points[0]
    lon, lat = transformer.transform(x, y)

    # 이름 / href
    name = f"GM_LED_{i+1}"
    href = f"{name}.dae"

    # 속성 dict 생성
    attr_dict = dict(zip(fields, record))

    # None 값 처리
    for k in attr_dict:
        if attr_dict[k] is None:
            attr_dict[k] = ""

    # 템플릿 변수 구성
    format_dict = {
        "name": name,
        "longitude": lon,
        "latitude": lat,
        "altitude": 0,
        "href": href,
        **attr_dict
    }

    # KML 생성
    try:
        kml_content = template.format(**format_dict)
    except KeyError as e:
        print(f"[ERROR] 필드 누락: {e}")
        continue

    # 파일 저장
    output_path = os.path.join(output_dir, f"{name}.kml")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(kml_content)

    if (i + 1) % 1000 == 0:
        print(f"{i+1}개 생성 완료")

print("전체 KML 생성 완료")