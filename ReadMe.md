How to run

- open terminal in project folder
- npm install
- python RunAllTests.py https://{url} -users -ramp_up_rate(seconds) -test_time(seconds)
    - ex : python RunAllTests.py https://apple.com 10 6 30
    - ** Some sites require www. to get all their urls ** 

- Program will generate load_test.py, which will run automatically after genrated, then it will genreate csv files with data from the load test, then it will generate the output.html file with the results visualized

