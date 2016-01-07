Since I manage several of my own sites end-to-end, including configuring and running their servers, it is important for me know what the sites are up to. This includes knowing when they may be down, as well as checking out any error codes that may be generated. I went ahead and created this simple dashboard vignette:

to keep track of my `Nginx` response status codes. I can see if there are any error codes that have been generated (those in the 400s or the 500s), and act accordingly.

Why did I go ahead and make my own dashboard? I wasn't too pleased with any of the existing solutions. They seemed far too cluttered with chart junk and lacked customizability. On the other hand, there were a few completely text-based interfaces to monitor one's servers. I found these completely text-based outputs difficult to parse at a glance. In the end, creating a custom dashboard made the most sense for my needs.

The process was fairly straightforward. First, I located my Nginx access logs and write a Python script to read them into a Pandas Dataframe, which is more manageable than their native format. Then, I aggregated and reshaped the dataframe to get a dataset that would identify what error codes had occurred over the course of each hour. This left me with a dataframe that looked like this:

Each row consisted of an hour; each column identified whether a type of error code (one in the 200s, one in the 300s, etc.) had occurred or not.

Then, I used Flask to serve an HTTP response within a web application which served my reshaped dataset in a JSON format. This would enable my front-end view to locate the data and read it in. Here's my basic view code that server my HTTP response:



Finally, I wrote the frontend in `d3.js` which actually renders the discrete sparklines. You can check out my previous tutorial on making discrete sparklines to learn how to make this type of a visualization.

And that's it! I now have an awesome, live-updating, minimalist visualization that lets me know if any concerning error codes have occurred over the last couple of days.



