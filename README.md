# SHP → KML 변환

## 설명
SHP 파일을 기반으로 각 객체를 개별 KML 파일로 변환

---

## 프로젝트 구조
```
project/
│
├── input/
│ └── shp/
│
├── output/
│ └── kml/
│
└── shp2kmlcollada/
├── shp2kml.py 
├── generate_dae.py 
├── template.kml 
└── requirements.txt
```
---

## 입력 데이터

```
input/
└── shp/
├── RDL_TREE_PS.shp
├── RDL_TREE_PS.dbf
├── RDL_TREE_PS.shx
├── RDL_TREE_PS.prj
```

---

## 출력 데이터

- 객체 단위 KML 파일 생성
  - 예: `GM_LED_1.kml ~ GM_LED_40000.kml`

```
output/
└── kml/
├── GM_LED_1.kml
├── GM_LED_2.kml
└── ...
```

---

## 실행 방법

### 1. 파이썬 설치 확인 (권장: 3.9 ~ 3.10)
```
python --version
```

### 2. 가상환경 생성
```
python -m venv venv
```

### 3. 가상환경 활성화
```
venv\Scripts\activate
```

### 4. 라이브러리 설치
```
pip install -r requirements.txt
```

### 5. main.py 실행
```
python main.py
```