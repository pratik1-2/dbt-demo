{% macro payableamt(totalcost, discountpercent) %}
{{totalcost}} - (({{discountpercent}} /100) * {{totalcost}} )
{% endmacro%}