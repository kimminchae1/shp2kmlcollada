from core.dae_manager import copy_dae_files

copy_dae_files(
    input_dir="../input/dae",
    output_dir="../output/dae",
    count=41646,
    prefix="tr",
)

print("DAE 생성 완료")