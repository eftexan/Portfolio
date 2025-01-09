# Density Plots/Box Plots/Scatterplots

#Height of function is occurance of each x value that occurs
#Normal Distribution 
#Conform function for height observed at the range, one at a time

setwd("/Users/ethan/Documents")
getwd()
ws <- read.table(file = "whiteside.csv", header = TRUE, sep = ",")
URL <- "https://raw.githubusercontent.com/fammediavilla2/datasets/main/titanic.csv"
titanic <- read.table(file = URL,sep = ",",header = T)
# density function sets up data
d <- density(ws$Temp)
#Plot the data
plot(x = d, main = 'Temperature Density Plot',
     xlab = "Temp in Celcius")
polygon(d, col='lightblue') #adds shading
summary(ws$Temp)

#Compare distributions of temp
d1 <-density(ws$Temp[ws$Insul=="Before"]) # red
d2<- density(ws$Temp[ws$Insul=="After"]) # blue

plot(d1, main="Temp Density Plot",
     xlab = "Temp in celsius", col = 'red', ylim=c(0,0.15))
lines(d2, main = "Temp Density Plot", 
      xlab = "Temp in celsius", col = 'blue')

median(ws$Temp[ws$Insul=="Before"])
median(ws$Temp[ws$Insul=="After"])

#Boxplots
#advantage to help flag outliers

#General distribution with fares
boxplot(x = titanic$fare, horizontal = TRUE,
        col='skyblue',
        main="Distribution of fare paid in RMS Titanic",
        xlab = 'Pounds (1912)')

#Examine dist based on ports
boxplot(formula = fare~embarked, data=titanic, horizontal = TRUE,
        col=c("skyblue1","tan","orange"),
        main="Distribution of fare paid in RMS Titanic",
        xlab = 'Pounds (1912)')

#Scatterplots
#plot(x,y, ...)

#Useful for trends/patterns/spot outliers, reveal correlation 

plot(x = ws$Temp, y = ws$Gas, pch=16, col='blue')

#scatterplot before and after
plot(x=ws$Temp, y = ws$Gas, pch=16, col=as.factor(ws$Insul))
