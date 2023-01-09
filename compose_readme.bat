jupyter nbconvert --to markdown 01_data_structures.ipynb --output 01_data_structures.md
jupyter nbconvert --to markdown 02_data_management.ipynb --output 02_data_management.md
jupyter nbconvert --to markdown 03_data_flows.ipynb --output 03_data_flows.md
jupyter nbconvert --to markdown 04_oop.ipynb --output 04_oop.md
jupyter nbconvert --to markdown 05_language_skeleton.ipynb --output 05_language_skeleton.md
jupyter nbconvert --to markdown 06_multithreading_multiprocessing.ipynb --output 06_multithreading_multiprocessing.md
jupyter nbconvert --to markdown 07_common_practice.ipynb --output 07_common_practice.md

jupyter nbconvert --to markdown 08_algorithms.ipynb --output 08_algorithms.md
jupyter nbconvert --to markdown 09_database.ipynb --output 09_database.md
jupyter nbconvert --to markdown 10_net.ipynb --output 10_net.md

copy 00_intro.md + 01_data_structures.md + 01_remark.md + 02_data_management.md + 03_data_flows.md + 04_oop.md + 05_language_skeleton.md + 06_multithreading_multiprocessing.md + 07_common_practice.md + 08_algorithms.md + 09_database.md + 10_net.md + 11_architecture.md + 12_admin_devops.md + 13_outro.md readme.md

del 01_data_structures.md
del 02_data_management.md
del 03_data_flows.md
del 04_oop.md
del 05_language_skeleton.md
del 06_multithreading_multiprocessing.md
del 07_common_practice.md

del 08_algorithms.md
del 09_database.md
del 10_net.md

rem Delete file from "Context manager" chapter
del test_context_connect.db

pause
