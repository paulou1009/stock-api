
stock-crawler API

To run:
  1. Install Django / MongoDB
  2. Open a terminal and run "mongod"
  3. Open another terminal, cd to this folder, and run "python manage.py runserver"
  4. Open browser go to URL: http://127.0.0.1:8000/server/?abc=123&ert=234

Query parameters:
  1. ticker: ex: AAPL
  2. freq: min or day
  2. startdate: YEAR-MONTH-DATE (ex: 2015-11-22)
  3. enddate: YEAR-MONTH-DATE (ex: 2015-11-25)
  4. starttime: HR-MIN (ex: 10-30)
  5. endtime: HR-MIN (ex: 11-50)
  6. type: OPEN/CLOSE/HIGH/LOW (TBD. This is for daily data)
  
Example:
  http://127.0.0.1:8000/server/?ticker=AAPL&freq=min&startdate=2015-11-22&enddate=2015-11-25&starttime=10-30&endtime=11-50&type=



