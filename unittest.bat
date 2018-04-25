cd test

:: ------------- Clean coverate -------------------------------------------
coverage erase

:: ------------- Unittest + coverage --------------------------------------
nosetests^
 --with-coverage^
 --cover-package=..\src^
 --with-xunit --xunit-file=nosetests.xml^
 --cover-xml --cover-xml-file=coverage.xml^
 --cover-html
cd ..
pause

:: ------------- Pylint ---------------------------------------------------
pylint src test
pause

:: ------------- SonarQube ------------------------------------------------
:: C:\SonarQube\sonar-scanner-3.0.3.778-windows\bin\sonar-scanner.bat