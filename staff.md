---
title: Staff
---

# {{site.course}}, {{site.quarter}}


<div id="staffinfo" data-role="collapsible" data-collapsed="false">
  <h2>Staff Information</h2>
  <ul>
   {% for topic in site.staffinfo %}
     <li {% if topic.indent %} class="indent" {% endif %}><a href="{{topic.url}}">{{ topic.topic }}</a>&mdash;{{topic.desc}}</li>
   {% endfor %}
  </ul>
</div>

