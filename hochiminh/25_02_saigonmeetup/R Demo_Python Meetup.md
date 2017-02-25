
<style>
.reveal a:not(.image){
  color: red;
}
.midcenter {
    position: fixed;
    top: 20%;
    left: 45%;
}
.h4 {
    color: rgb(0,112,192);
    font-size: 30pt;
    font-weight: bold;
}

</style>

Communicating Results in R
========================================================
author: Nadav Rindler
date: February 25, 2017
autosize: true

Full-Cycle Analytics Workflow in R
========================================================

1. Build dataset using in-database queries
2. Import data
3. Data prep and analysis
4. Predictive modeling
5. Visualizations
6. Publishing Results

Full-Cycle Analytics Workflow in R
========================================================

1. Build dataset using in-database queries
2. Import data
3. Data prep and analysis
4. Predictive modeling
5. [Visualizations]()
6. [Publishing Results]()

Getting Started in R
========================================================


```r
#Install a new package (once)
install.packages("ggplot2") #GGPLOT is a visualization package

#Activate the package (every session)
library(ggplot2)
```

Visualizations in R - GGPLOT
========================================================

GGPLOT is a useful R package for creating charts, and uses a structured syntax to add layers to the chart


```r
ggplot(DF, x=age, y=num_complaints) + 
   aes(age, num_complaints) +
   geom_smooth(method="lm", size=2, linetype=3) + 
   geom_point(aes(color = Generations), size=4, alpha=1/2) +
   labs(title="TR Complaints by Age and Generation", x="Age", y="Complaint Count")
```

GGPLOT code creates this chart:
========================================================

<div class="slideContent"> <img style="margin-left:100px;border:0px;box-shadow:none" src="figure/tr_complaints_age.png"></img></div>

Mapping with Leaflet
========================================================

Leaflet is one of the most popular open-source JavaScript libraries for interactive maps (but you don't have to know JavaScript!)


```r
library(leaflet)

leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=106.685, lat=10.780, popup="Saigon Innovation Hub") %>% 
  setView(lng=106.685, lat=10.780, zoom=14)
```

Creates [this map](WeAreHere.html)

More Interactive Visualizations
========================================================

[HTML widgets](http://www.htmlwidgets.org/showcase_dygraphs.html) allow you to create interactive charts and maps **in a single line of code** that can be published directly to HTML, with no knowledge of Javascript

[Shiny](https://shiny.rstudio.com/gallery/movie-explorer.html) creates interactive dashboards, also publishable directly to HTML

Publish Results in R
========================================================

- Publish directly to documents or slides
- HTML or PDF format
- Uses Markdown syntax (similar to LaTex) 
- Default templates available, however custom design requires knowledge of HTML/CSS

*(Note: This presentation was created in R)*

The Big Picture
========================================================

- R streamlines analytics by bringing entire workflow into a single environment
- Free and open source, with dynamic user and development community
- Quick install and set-up
- Powerful visualizations, including interactive maps and dashboards
- Ability to run on desktop or server-side (e.g., Amazon AWS hosting)
- Can connect with a wide range of SQL databases and run queries in-database without transferring data
- Wide range of modeling/analytic functions, including regression, tree-based, neural net, clustering, text mining, sentiment analysis

Drawbacks of R
========================================================

- Coding environment, not point-and-click, designed for technical users
- Many different ways to do the same task (many options of packages)
- Even within R, completely different syntax between R, R Markdown, and Shiny
- Not the only free option, many data scientists choose Python for analytics
- Memory size limitations require advanced methods to handle 'big data'

Resources
========================================================

- [R for Data Science textbook](http://r4ds.had.co.nz/)
- [Intro to Statistical Learning in R textbook](http://ggplot2.org/)
- [Intro to DPLYR](https://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html)
- [GGPLOT](http://ggplot2.org/)
- [HTML widgets](http://www.htmlwidgets.org)
- [Shiny](http://shiny.rstudio.com)
- [R Markdown](http://rmarkdown.rstudio.com/)

========================================================

<span class="h4 midcenter" style="margin-left:-150px;margin-top:150px;font-size:48px;color: rgb(255,0,0);"><b>Questions & R Demo</b></span>

