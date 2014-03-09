curl 'capitolwords.org/api/1/dates.json?phrase=deficit&percentages=true&granularity=year&apikey=76004e1953b7437587fb5fe32f66c4ab' > test.json 
cat test.json | in2csv -f json -k results > test.csv


create table budget (count int, percentage float, total int, year int);
.import blah.csv budget
echo "sql command" | sqlite3 dbfile

select b.year as year, d.count as deficit, b.count as budget, 100*d.percentage/b.percentage as dtob from budget as b join deficit as d on b.year=d.year where b.year > 2010;
