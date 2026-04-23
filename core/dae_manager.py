import os
import shutil
from tqdm import tqdm
import time

def copy_dae_files(input_dir, output_dir, count, prefix="gumi"):
    files = [f for f in os.listdir(input_dir) if f.lower().endswith(".dae")]

    if not files:
        raise Exception("dae 파일 없음")

    source_file = os.path.join(input_dir, files[0])
    os.makedirs(output_dir, exist_ok=True)

    # 용량 체크
    file_size = os.path.getsize(source_file)
    required_size = file_size * count
    free_size = shutil.disk_usage(output_dir).free

    print(f"원본 파일 크기: {file_size / (1024*1024):.2f} MB")
    print(f"필요 용량: {required_size / (1024*1024*1024):.2f} GB")
    print(f"남은 용량: {free_size / (1024*1024*1024):.2f} GB")

    if free_size < required_size:
        raise Exception("디스크 용량 부족")

    # 복사 + 진행률
    # for i in tqdm(range(1, count + 1), desc="DAE 생성 중"):
    for i in range(1, count + 1):
        name = f"{prefix}_{i}.dae"
        dest_file = os.path.join(output_dir, name)
        shutil.copyfile(source_file, dest_file)

        if i % 500 == 0:
            print(f"{i}개 완료")
            time.sleep(1)