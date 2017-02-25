# R Demo
#Feb 25, 2017
#Python Meetup @ Saigon Innovation Hub

#install packages (only the first time)
#install.packages(c("dplyr","ggplot2","sqldf",
#                   "ISLR","leaflet","maps","ggmap"))

#load packages
library(dplyr) #data manipulation
library(ggplot2) #visualizations
library(sqldf) #write SQL queries directly in R
library(ISLR) #package with a sample dataset to analyze
library(leaflet) #mapping
require(maps) 
require(ggmap) 


#import pre-loaded data from ISLR package
attach(Auto)

#Print first few rows of data
head(Auto)

#how big is the data set?
length(Auto) #number of columns
nrow(Auto) #number of rows

#count number of cars by number of cylinders, using SQL syntax
sqldf("select cylinders, count(*) from Auto group by 1")

#the same task using dplyr syntax
t <- Auto %>% 
      group_by(cylinders) %>% 
      summarise(num_cars=n())
t

#plot using built-in plot function
attach(t)
bp <- barplot(num_cars, 
        main="Cars by Number of Cylinders",
        xlab="# Cylinders",
        ylab="# Cars")
axis(1,at=bp,labels=t$cylinders)
bp

#plot using GGPLOT
ggplot(data=t,aes(x=cylinders,y=num_cars))+
  geom_bar(stat="identity", fill="purple")+
  labs(title="Cars by Number of Cylinders", x="Cylinders", y="Number of Cars")

#another GGPLOT example  
ggplot(data=Auto,aes(x=horsepower,y=mpg))+
  geom_point(aes(color=cylinders),size=4, alpha=1/2)+
  geom_smooth(method="lm", size=2, linetype=3) + 
  labs(title="MPG by Horsepower", x="Horsepower", y="MPG")

#mapping with Leaflet
leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=106.685, lat=10.780, popup="Saigon Innovation Hub") %>% 
  setView(lng=106.685, lat=10.780, zoom=14)

#mapping with maps package

#a US Cities
data(us.cities) #using built-in dataset of US cities
head(us.cities) #view first few rows of data set
big_cities <- subset(us.cities, pop > 500000)
qplot(long, lat, data = big_cities) + borders("state", size = 0.5)

#b California
ca_cities <- subset(us.cities, country.etc == "CA")
ggplot(ca_cities, aes(long, lat)) + borders(database="county", regions="california", color = "grey70") + geom_point()

