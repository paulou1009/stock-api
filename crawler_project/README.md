
stock-crawler API

Query parameters:
  1. ticker: ex: AAPL
  2. freq: min or day
  2. startdate: YEAR-MONTH-DATE (ex: 2015-11-22)
  3. enddate: YEAR-MONTH-DATE (ex: 2015-11-25)
  4. starttime: HR-MIN (ex: 10-30)
  5. endtime: HR-MIN (ex: 11-50)
  6. type: OPEN/CLOSE (TBD. This curently is only for day data)
  
Example:
  http://127.0.0.1:8000/server/?ticker=AAPL&freq=min&startdate=2015-11-22&enddate=2015-11-25&starttime=10-30&endtime=11-50&type=



