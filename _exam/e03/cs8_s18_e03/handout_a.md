---
layout: examHandoutNoName
num: e02
ready: true
desc: "Midterm Handout A"
exam_date: 2018-05-15 15:30:00.00
---

<style>
body {
 font-size: 14px;
}

</style>

{% include cancel_syntax_colors.html %}

# Dictionary `states`

The dictionary `states` maps state abbreviations such as `AZ` and `CA` to dictionaries with information
about states of the United States.   The three items in those dictionaries are:

* `"name"`: the name of the state (e.g. "Arizona", or "California")
* `"capital"`: the capital city of that state (e.g. "Sacramento")
* `"largest"`: the largest city in that state (e.g. "Los Angeles")
* `"baseball"`: the names of the major league professional baseball teams in that state, if any. 

The dictionary `states` only has information about five western states.
On the back of this handout is another example of one of these dictionaries, with information on
a few eastern states.

{% highlight python linenos %}
states = {
 "AZ" : { "name": "Arizona",
          "capital" : "Phoenix",
          "largest": "Phoenix",
	  "baseball": ["Diamondbacks"] },
 "CA" : { "name": "California",
          "capital" : "Sacramento",
          "largest" : "Los Angeles",
          "baseball": ["Angels","Dogders","A's","Padres","Giants"] },
 "NV" : { "name" : "Nevada",
          "capital" : "Carson City",
          "largest" : "Las Vegas",
	  "baseball" : [] },
 "OR" : { "name" : "Oregon",
          "capital" : "Salem",
          "largest" : "Portland",
	  "baseball" : [] },	 
 "WA" : { "name" : "Washington",
          "capital" : "Olympia",
          "largest" : "Seattle",
	  "baseball" : ["Mariners"] },     
 }
{% endhighlight %}

<div style="page-break-before:always;">
</div>

<div style="font-size: 16px; font-weight:bold; font-family: Arial Narrow, Arial, sans-serif; border: 1px solid black; padding: 2px; margin: 4px; text-align: center; margin-left: auto; margin-right: auto; width: 40em;">
{{page.desc}} for {{site.course}}, Final Exam, {{site.qtr}}, Page 2
</div>


{% highlight python linenos %}
eastern_states = {
 "NY" : { "name": "New York",
          "capital" : "Albany",
          "largest": "New York",
	  "baseball": ["Mets","Yankees"] },
 "PA" : { "name": "Pennsylvania",
          "capital" : "Harrisburg",
          "largest" : "Philadelphia",
          "baseball": ["Phillies","Pirates"] },
 "MD" : { "name" : "Maryland",
          "capital" : "Annapolis",
          "largest" : "Baltimore",
	  "baseball" : [Orioles] },
 "NJ" : { "name" : "New Jersey",
          "capital" : "Trenton",
          "largest" : "Newark",
	  "baseball" : [] },	 
 "DE" : { "name" : "Delaware",
          "capital" : "Dover",
          "largest" : "Wilmington",
	  "baseball" : [] },	 
 }
{% endhighlight %}


