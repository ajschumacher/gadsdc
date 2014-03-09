# API Lab

_Application Programming Interface_ (API) can refer to a range of things, but it's now commonly used to refer to conventions used to communicate with web services, many of which provide data. These web services often describe themselves as [REST](http://en.wikipedia.org/wiki/Representational_state_transfer)ful over [HTTP](http://en.wikipedia.org/wiki/Http), most commonly using the GET and POST methods.

APIs are useful for accessing data that they make available, but the _idea_ of APIs is also useful. APIs offer a level of abstraction between different parts of a system, and thinking about your own data projects in this way can be very helpful. For example, you might determine toward the beginning of a project the APIs that you need, either as final products or internally. This helps you to articulate goals and to work on different parts of the project separately. It lets you change one part of the project without breaking other parts of the project.

[capitolwords](http://capitolwords.org/) is a project of [the Sunlight Foundation](http://sunlightfoundation.com/) that makes accessible a range of data derivations from the US Congressional Record. It's fun to play with their web interface, but they also make many things available via their API.

As is often the case, there is some level of authentication required to use the capitalwords API, but it's quite easy. You can [sign up](http://sunlightfoundation.com/api/accounts/register/) for an API key which you'll get in your email. That single API key is all you need. ([OAuth](http://oauth.net/) is a common and slightly more complex authentication scheme.)

We can use simple HTTP GET requests, for example in a browser or with `curl`, to get data from capitalwords in JSON format. You can [explore](http://tryit.sunlightfoundation.com/capitolwords) a lot of functionality and get help building your request. We'll just use the `dates.json` endpoint to get two simple datasets.

```bash
curl 'http://capitolwords.org/api/1/dates.json?phrase=budget&percentages=true&granularity=year&apikey=YOUR_KEY_HERE' > lab_API-budget.json
curl 'http://capitolwords.org/api/1/dates.json?phrase=deficit&percentages=true&granularity=year&apikey=YOUR_KEY_HERE' > lab_API-deficit.json
```

We now have two files with JSON data in them about how much the US government was talking about "[budget](lab_API-budget.json)" and "[deficit](lab_API-deficit.json)".



[Convert JSON to CSV](http://konklone.io/json/) in your browser.
