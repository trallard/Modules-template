{% extends 'markdown.tpl' %}


{# custom header for jekyll post #}
{%- block header -%}
---
layout: default
title: "{{resources['metadata']['name']}}"
tags:
    - Day

permalink: "{{resources['metadata']['name']}}.html"
---
{%- endblock header -%}

{# change the color of the In block #}
{% block in_prompt %}
<br>
<font color ='#00bcd4'> In [{{ cell.execution_count }}]: </font>
{% endblock in_prompt %}


{# code highlight, needs to be changed accordingly #}
{% block input %}
{{ '{% highlight R %}' }}
{{ cell.source }}
{{ '{% endhighlight %}' }}
{% endblock input %}

{% block data_svg %}
![svg]({{ output.metadata.filenames['image/svg+xml'] | path2support }})
{% endblock data_svg %}

{% block data_png %}
![png]({{ output.metadata.filenames['image/png'] | path2support }})
{% endblock data_png %}

{% block data_jpg %}
![jpeg]({{ output.metadata.filenames['image/jpeg'] | path2support }})
{% endblock data_jpg %}

{# cells containing markdown text only #}
{% block markdowncell scoped %}
{{ cell.source | wrap_text(80) }}
{% endblock markdowncell %}

{# headings #}
{% block headingcell scoped %}
{{ '#' * cell.level }} {{ cell.source | replace('\n', ' ') }}
{% endblock headingcell %}

{% block stream -%}
{% endblock stream %}

{# latex data block#}
{% block data_latex %}
{{ output.data['text/latex'] }}
{% endblock data_latex %}


{% block data_text scoped %}
{{ output.data['text/plain'] | indent }}
{% endblock data_text %}

{% block data_html scoped %}
{{ output.data['text/html'] }}
{% endblock data_html %}

{% block data_markdown scoped %}
{{ output.data['text/markdown'] }}
{% endblock data_markdown %}
