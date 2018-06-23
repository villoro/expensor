:: ------------- Unittest + coverage --------------------------------------
nosetests --with-coverage --cover-package=src --cover-erase --cover-inclusive
pause

:: ------------- Pylint ---------------------------------------------------
pylint src test
pause
