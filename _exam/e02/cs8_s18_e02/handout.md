---
layout: examHandoutNoName
num: e02
ready: true
desc: "Midterm Handout"
exam_date: 2018-05-15 15:30:00.00
---

<style>
body {
 font-size: 14px;
}

</style>


# Code for `indexShortest_a`

No hints on this one.

{% highlight python linenos %}
def indexShortest_a(slist):
    if type(slist)!=list:
        raise ValueError("not a list")
    if slist==[]:
        raise ValueError("it's empty")

    soFar = 0
    for i in range(0,len(slist)): 
        if type(slist[i])!=str:     
            raise ValueError("found non-string")
        if len(slist[i]) < len(slist[soFar]):
            soFar = i
    return soFar
{% endhighlight %}


# Code for `indexShortest_b`

Hint: Pay attention to the indentation of line 13

{% highlight python linenos %}
def indexShortest_b(slist):
    if type(slist)!=list:
        raise ValueError("not a list")
    if slist==[]:
        raise ValueError("it's empty")

    soFar = 0
    for i in range(0,len(slist)): 
        if type(slist[i])!=str:   
            raise ValueError("found non-string")
        if len(slist[i]) < len(slist[soFar]):
            soFar = i
        return soFar
{% endhighlight %}


<div style="page-break-before:always;">
</div>

<div style="font-size: 16px; font-weight:bold; font-family: Arial Narrow, Arial, sans-serif; border: 1px solid black; padding: 2px; margin: 4px; text-align: center; margin-left: auto; margin-right: auto; width: 40em;">
Handout for {{site.course}}, Final Exam, {{site.qtr}}, Page 2
</div>

# Code for `indexShortest_c`

Hint: pay attention to line 11

{% highlight python linenos %}
def indexShortest_c(slist):
    if type(slist)!=list:
        raise ValueError("not a list")
    if slist==[]:
        raise ValueError("it's empty")

    soFar = 0
    for i in range(0,len(slist)): 
        if type(slist[i])!=str:     
            raise ValueError("found non-string")
        if len(slist[i]) <= len(slist[soFar]):
            soFar = i
    return soFar
{% endhighlight %}


# Code for `indexShortest_d`

Hint: again, pay attention to line 11

{% highlight python linenos %}

def indexShortest_d(slist):
    if type(slist)!=list:
        raise ValueError("not a list")
    if slist==[]:
        raise ValueError("it's empty")

    soFar = 0
    for i in range(0,len(slist)):
        if type(slist[i])!=str:  
            raise ValueError("found non-string")
        if slist[i] < slist[soFar]:
            soFar = i
    return soFar
{% endhighlight %}
 

</div>