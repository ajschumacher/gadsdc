# API Lab

_Application Programming Interface_ (API) can refer to a range of things, but it's now commonly used to refer to conventions used to communicate with web services, many of which provide data. These web services often describe themselves as [REST](http://en.wikipedia.org/wiki/Representational_state_transfer)ful over [HTTP](http://en.wikipedia.org/wiki/Http), most commonly using the GET and POST methods.

APIs are useful for accessing data that they make available, but the _idea_ of APIs is also useful. APIs offer a level of abstraction between different parts of a system, and thinking about your own data projects in this way can be very helpful. For example, you might determine toward the beginning of a project the APIs that you need, either as final products or internally. This helps you to articulate goals and to work on different parts of the project separately. It lets you change one part of the project without breaking other parts of the project.

[capitolwords](http://capitolwords.org/) is a project of [the Sunlight Foundation](http://sunlightfoundation.com/) that makes accessible a range of data derivations from the US Congressional Record. It's fun to play with their web interface, but they also make many things available via their API.

As is often the case, there is some level of authentication required to use the capitalwords API, but it's quite easy. You can [sign up](http://sunlightfoundation.com/api/accounts/register/) for an API key which you'll get in your email. That single API key is all you need. ([OAuth](http://oauth.net/) is a common and slightly more complex authentication scheme.)

We can use simple HTTP GET requests, for example in a browser or with `curl`, to get data from capitalwords in JSON format. You can [explore](http://tryit.sunlightfoundation.com/capitolwords) a lot of functionality and get help building your request. There's other [documentation](http://capitolwords.org/api/1/) available as well. We'll just use the `dates.json` endpoint to get two simple datasets.

```bash
curl 'http://capitolwords.org/api/1/dates.json?phrase=budget&percentages=true&granularity=year&apikey=YOUR_KEY_HERE' > lab_API-budget.json
curl 'http://capitolwords.org/api/1/dates.json?phrase=deficit&percentages=true&granularity=year&apikey=YOUR_KEY_HERE' > lab_API-deficit.json
```

We now have two files with JSON data in them about how much the US government was talking about "[budget](lab_API-budget.json)" and "[deficit](lab_API-deficit.json)".

We would like to work with this data in a tabular format. `R` and `python` have ways of doing this transformation, as does [csvkit](http://csvkit.readthedocs.org/). [Eric Mill](https://twitter.com/konklone), who worked for the Sunlight Foundation and inspired this lab, has made a web-based tool to [convert JSON to CSV](http://konklone.io/json/) in your browser, which is very handy. One way or another, we can change JSON to CSV. (This is especially true when the structure is simple and not too nested; it becomes trickier when the structure is more complex, and may require custom code.)

```bash
in2csv -f json -k results lab_API-budget.json > lab_API-budget.csv
in2csv -f json -k results lab_API-deficit.json > lab_API-deficit.csv
```

We're now in very good shape to do whatever analysis we'd like to do with the data. Here's a parting note from Eric Mill:

> ...hopefully this demystifies some words for you: URLs, JSON, and APIs don't take a computer science degree to understand. They are patterns, meant for both humans and computers to understand.

> Understanding how this stuff fits together will help you in seeing how the web works, the value in tools people make, and maybe even to know when someone is feeding you a line.
