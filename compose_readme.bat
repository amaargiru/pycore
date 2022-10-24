jupyter nbconvert --to markdown 01_python_01_data_structures.ipynb --output 01_python_01_data_structures.md
jupyter nbconvert --to markdown 01_python_02_primitive_data_processing.ipynb --output 01_python_02_primitive_data_processing.md
jupyter nbconvert --to markdown 01_python_03_runtime_data_flows.ipynb --output 01_python_03_runtime_data_flows.md
jupyter nbconvert --to markdown 01_python_04_oop.ipynb --output 01_python_04_oop.md
jupyter nbconvert --to markdown 01_python_05_language_skeleton.ipynb --output 01_python_05_language_skeleton.md
jupyter nbconvert --to markdown 01_python_06_multithreading_multiprocessing.ipynb --output 01_python_06_multithreading_multiprocessing.md
jupyter nbconvert --to markdown 01_python_07_useful_libraries.ipynb --output 01_python_07_useful_libraries.md

jupyter nbconvert --to markdown 02_sql.ipynb --output 02_sql.md
jupyter nbconvert --to markdown 04_algorithms.ipynb --output 04_algorithms.md
jupyter nbconvert --to markdown 06_pytest_mock.ipynb --output 06_pytest_mock.md
jupyter nbconvert --to markdown 09_sqlalchemy.ipynb --output 09_sqlalchemy.md

copy 00_intro.md + 01_python_01_data_structures.md + 01_remark.md + 01_python_02_primitive_data_processing.md + 01_python_03_runtime_data_flows.md + 01_python_04_oop.md + 01_python_05_language_skeleton.md + 01_python_06_multithreading_multiprocessing.md + 01_python_07_useful_libraries.md + 02_sql.md + 03_architecture.md + 04_algorithms.md + 05_admin_devops.md + 06_pytest_mock.md + 07_fastapi.md + 08_flask.md + 09_sqlalchemy.md + 10_outro.md readme.md

del 01_python_01_data_structures.md
del 01_python_02_primitive_data_processing.md
del 01_python_03_runtime_data_flows.md
del 01_python_04_oop.md
del 01_python_05_language_skeleton.md
del 01_python_06_multithreading_multiprocessing.md
del 01_python_07_useful_libraries.md

del 02_sql.md
del 04_algorithms.md
del 06_pytest_mock.md
del 09_sqlalchemy.md

pause
