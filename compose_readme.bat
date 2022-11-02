jupyter nbconvert --to markdown 01_python_01_data_structures.ipynb --output 01_python_01_data_structures.md
jupyter nbconvert --to markdown 01_python_02_primitive_data_management.ipynb --output 01_python_02_primitive_data_management.md
jupyter nbconvert --to markdown 01_python_03_runtime_data_flows.ipynb --output 01_python_03_runtime_data_flows.md
jupyter nbconvert --to markdown 01_python_04_oop.ipynb --output 01_python_04_oop.md
jupyter nbconvert --to markdown 01_python_05_language_skeleton.ipynb --output 01_python_05_language_skeleton.md
jupyter nbconvert --to markdown 01_python_06_multithreading_multiprocessing.ipynb --output 01_python_06_multithreading_multiprocessing.md
jupyter nbconvert --to markdown 01_python_07_common_practice.ipynb --output 01_python_07_common_practice.md

jupyter nbconvert --to markdown 02_sql.ipynb --output 02_sql.md
jupyter nbconvert --to markdown 03_net.ipynb --output 03_net.md
jupyter nbconvert --to markdown 05_algorithms.ipynb --output 05_algorithms.md
jupyter nbconvert --to markdown 07_pytest_mock.ipynb --output 07_pytest_mock.md
jupyter nbconvert --to markdown 10_sqlalchemy.ipynb --output 10_sqlalchemy.md

copy 00_intro.md + 01_python_01_data_structures.md + 01_remark.md + 01_python_02_primitive_data_management.md + 01_python_03_runtime_data_flows.md + 01_python_04_oop.md + 01_python_05_language_skeleton.md + 01_python_06_multithreading_multiprocessing.md + 01_python_07_common_practice.md + 02_sql.md + 03_net.md + 04_architecture.md + 05_algorithms.md + 06_admin_devops.md + 07_pytest_mock.md + 08_fastapi.md + 09_flask.md + 10_sqlalchemy.md + 11_outro.md readme.md

del 01_python_01_data_structures.md
del --output 01_python_02_primitive_data_management.md
del 01_python_03_runtime_data_flows.md
del 01_python_04_oop.md
del 01_python_05_language_skeleton.md
del 01_python_06_multithreading_multiprocessing.md
del 01_python_07_common_practice.md

del 02_sql.md
del 03_net.md
del 05_algorithms.md
del 07_pytest_mock.md
del 10_sqlalchemy.md

pause
