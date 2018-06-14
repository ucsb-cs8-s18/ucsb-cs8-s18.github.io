---
layout: examHandoutNoName
num: e03
ready: true
desc: "Midterm Handout A"
exam_date: 2018-06-14 16:00:00.00
---

<style>
body {
 font-size: 14px;
}

</style>

{% include cancel_syntax_colors.html %}

# `screen` functions

<table>
<tr>
<td markdown="1">

```
def create_screen(rows, columns):
    '''
    Creates a screen of rows x columns pixels
    '''
    grid = []
    for row in range(rows):
        grid.append([0] * columns)
    return grid
```

</td>

<td markdown="1">

```
def print_screen(screen):
    ''' Prints the screen to the console.
        When a pixel == 0, then a '*' is displayed
        When a pixel == 1, then a ' ' is displayed
    '''
    for row in range(len(screen)):
        for col in range(len(screen[0])):
            if screen[row][col] == 0:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    return
```

</td>
</tr>
</table>


<div style="page-break-before:always;">
</div>

<div style="font-size: 16px; font-weight:bold; font-family: Arial Narrow, Arial, sans-serif; border: 1px solid black; padding: 2px; margin: 4px; text-align: center; margin-left: auto; margin-right: auto; width: 40em;">
{{page.desc}} for {{site.course}}, Final Exam, {{site.qtr}}, Page 2
</div>

# TBD

{% highlight python linenos %}
TBD
{% endhighlight %}


