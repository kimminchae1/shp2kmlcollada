from core.dae_manager import copy_dae_files

copy_dae_files(
    input_dir="../input/dae",
    output_dir="../output/dae",
    count=150,
    prefix="GM_TREE",
)

print("DAE 생성 완료")