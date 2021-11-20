---
layout: dashboard
title: Welcome to Your Dashboard 
---

[(click here to go to the first page)](./)

[(click here to see how it was done)](./description.html)


<script src="{{ "/assets/js/Setup.js" | relative_url }}"></script>
<script src="{{ "/assets/js/Config.js" | relative_url }}"></script>

## Understanding your CO2 impact

You are currently working with 21 categories, in the 4 graphs below you will find:

1.    CO2kg by category
2.    CO2kg/Eur by category
3.    Approximated CO2kg by Category
4.    Four of your Categories are critical to optimise



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


## CO2kg/Eur by Category

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



### Combined cost and CO2 impact 

By multiplying the carbon emission (CO2/1€) for a category with your total cost for the category, we can see the relative impact of each category on the combined bottom line of your organisation and the planet. 




### Approximated Total CO2kg by Category

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

## Opportunities and recommendations 

Within your procured categories, there are 4 categories in particular that account for almost all of your combined cost and CO2 emissions. If these categories are absolutely essential to your business, we'd strongly recommend considering an alternative vendor with lower CO2 emissions and neutral or lower price.

### 4 of your Categories are Critical to Optimize

<div>
  <canvas id="myChart4"></canvas>
</div>


<script>
  // === include 'setup' then 'config' above ===

  const myChart4 = new Chart(
    document.getElementById('myChart4'),
    chart4
  );
</script>



[(click here to go to the first page)](./)

[(click here to see how it was done)](./description.html)