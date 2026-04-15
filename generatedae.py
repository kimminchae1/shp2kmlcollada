import os
import shutil

input_dir = r"D:\shp2kmlcollada\input\dae"
output_dir = r"D:\shp2kmlcollada\output\dae"

# input 폴더에 있는 dae 파일 찾기 (1개라고 가정)
files = [f for f in os.listdir(input_dir) if f.endswith(".dae")]

if not files:
    print("dae 파일 없음")
    exit()

source_file = os.path.join(input_dir, files[0])

# 1~10까지 복사
for i in range(1, 11):
    new_name = f"gumi_{i}.dae"
    dest_file = os.path.join(output_dir, new_name)

    shutil.copy(source_file, dest_file)

print("완료")