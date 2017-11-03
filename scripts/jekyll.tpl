{% extends 'markdown.tpl' %}

{# custom header for jekyll post #}
{%- block header -%}
---
layout: notebook
title: "{{resources['metadata']['name']}}"
tags:
---
{%- endblock header -%}


{% block in_prompt -%}
<div class="prompt input_prompt">
{%- if cell.execution_count is defined -%}
{%- if resources.global_content_filter.include_input_prompt-%}
<font color ='#00bcd4'> In [{{ cell.execution_count }}]: </font>
{%- else -%}
In&nbsp;[&nbsp;]:
{%- endif -%}
{%- endif -%}
</div>
{%- endblock in_prompt %}

{% block output %}
<div class="output_area">
{% if resources.global_content_filter.include_output_prompt %}
{% block output_area_prompt %}
{%- if output.output_type == 'execute_result' -%}
    <div class="prompt output_prompt">
{%- if cell.execution_count is defined -%}
    Out[{{ cell.execution_count|replace(None, "&nbsp;") }}]:
{%- else -%}
    Out[&nbsp;]:
{%- endif -%}
{%- else -%}
    <div class="prompt">
{%- endif -%}
    </div>
{% endblock output_area_prompt %}
{% endif %}
{{ super() }}
</div>
{% endblock output %}


{# Images will be saved in the custom path #}
{% block data_svg %}
<img src="{{ output.metadata.filenames['image/svg+xml'] | jekyllpath }}" alt="svg" />
{% endblock data_svg %}

{% block data_png %}
<img src="{{ output.metadata.filenames['image/png'] | jekyllpath }}" alt="png"/>
{% endblock data_png %}

{% block data_jpg %}
<img src="{{ output.metadata.filenames['image/jpeg'] | jekyllpath }}" alt="jpeg" />
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

{% block data_html scoped -%}
<div class=" output_subarea {{ extra_class }}">
{{ output.data['text/html'] }}
</div>
{%- endblock data_html %}

{% block data_markdown scoped -%}
<div class=" output_subarea {{ extra_class }}">
{{ output.data['text/markdown'] | markdown2html }}
</div>
{%- endblock data_markdown %}
