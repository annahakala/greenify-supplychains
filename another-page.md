---
layout: dashboard
title: Welcome to Your Dashboard 
---

[First page](./)

[How it was done](./description.html)


<script src="{{ "/assets/js/Setup.js" | relative_url }}"></script>
<script src="{{ "/assets/js/Config.js" | relative_url }}"></script>

## Cost and CO2 baseline 

You are currently working with 21 product categories, in the graphs below you can see the share of cost (€) for each category as well as the estimated share of carbon emission (CO2/1€) for each category. 

### Approximated CO2kg by Category

<div>
  <canvas id="myChart1"></canvas>
</div>


<script>
  // === include 'setup' then 'config' above ===

  const myChart1 = new Chart(
    document.getElementById('myChart1'),
    chart1
  );
</script>


### Cost by Category

<div>
  <canvas id="myChart2"></canvas>
</div>


<script>
  // === include 'setup' then 'config' above ===

  const myChart2 = new Chart(
    document.getElementById('myChart2'),
    chart2
  );
</script>

### CO2kg per € spent by Category

By multiplying the carbon emission (CO2/1€) for a category with your total cost for the category, we can see the relative impact of each category on the combined bottom line of your organisation and the planet. 


## The Third Chart from chart.js

<div>
  <canvas id="myChart3"></canvas>
</div>



<script>
  // === include 'setup' then 'config' above ===

  const myChart3 = new Chart(
    document.getElementById('myChart3'),
    chart3
  );
</script>

## Opportunities and recommendations 

Within your procured categories, there are 5(?) categories in particular that account for 70%(?) of your combined cost and CO2 emissions. If these categories are absolutely essential to your business, we'd strongly recommend considering an alternative vendor with lower CO2 emissions and neutral or lower price, click here to see a comparison of similar vendors (dead link).



[First page](./)

[How it was done](./description.html)
