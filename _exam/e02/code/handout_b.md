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

# Test cases for indexLargestEvenInt

`indexLargestEvenInt` should return the index
in the list of the largest even integer.   If there
are no even integers in the list, it should return
`None`.   

{% highlight python linenos %}
list1 = [22,55,88,33,66]
list2 = [33,11,77]
list3 = [33,34,11,66,99]
list4 = [44,11,22]

def test_1():
    assert indexLargestEvenInt(list1)==2

def test_2():
    assert indexLargestEvenInt(list2)==None

def test_3():
    assert indexLargestEvenInt(list3)==3

def test_4():
    assert indexLargestEvenInt(list4)==0
    
{% endhighlight  %}

# Code for `indexLargestEvenInt_a`

{% highlight python linenos %}
def indexLargestEvenInt_a(ilist):
    "index of largest even integer; None if no even ints"
    if type(ilist)!=list:
        raise ValueError("not a list")
    answer=None
    for x in ilist:
      if x%2 == 0:
        if answer==None or x > answer:
          answer = x
    return answer	  
{% endhighlight %}


# Code for `indexLargestEvenInt_b`


{% highlight python linenos %}
def indexLargestEvenInt_b(ilist):
    if type(ilist)!=list:
        raise ValueError("not a list")
    answer=None
    for i in range(len(ilist)):
      if ilist[i]%2 == 0:
        if answer==None or ilist[i] > ilist[answer]:
          answer = i
    return answer

{% endhighlight %}


<div style="page-break-before:always;">
</div>

<div style="font-size: 16px; font-weight:bold; font-family: Arial Narrow, Arial, sans-serif; border: 1px solid black; padding: 2px; margin: 4px; text-align: center; margin-left: auto; margin-right: auto; width: 40em;">
Handout for {{site.course}}, Final Exam, {{site.qtr}}, Page 2
</div>

# Code for `indexLargestEvenInt_c`


{% highlight python linenos %}
def indexLargestEvenInt_c(ilist):

    if type(ilist)!=list:
        raise ValueError("not a list")
    answer=None
    for i in range(len(ilist)):
      if ilist[i]%2 == 0:
        if answer==None or ilist[i] > ilist[answer]:
          answer = i
      return answer

{% endhighlight %}


# Code for `indexLargestEvenInt_d`


{% highlight python linenos %}
def indexLargestEvenInt_d(ilist):

    if type(ilist)!=list:
        raise ValueError("not a list")
    answer=None
    for x in ilist:
      if (x%2 == 0) and x > answer:
        answer = x
    return answer

{% endhighlight %}
 

</div>