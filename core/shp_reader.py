import shapefile

# SHP 파일 읽기 -> 도형, 속성 데이터를 하나씩 반환
def read_shp(shp_path):
    sf = shapefile.Reader(shp_path)
    fields = [f[0] for f in sf.fields[1:]] # 필드명 추출

    # 도형 정보, 속성값 목록
    for shape, record in zip(sf.shapes(), sf.records()):
        yield shape, dict(zip(fields, record)) # yield = 값 하나씩 반환