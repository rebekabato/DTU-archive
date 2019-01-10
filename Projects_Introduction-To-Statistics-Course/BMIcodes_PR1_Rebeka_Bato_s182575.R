######################## Project 1###################################
# Topic: BMI survey
# Author: Rebeka Bato Julianna (s182575)
# deadline : 23th October

# Reading the data into R and setting working directory
setwd("~/")
D <- read.table("bmi1_data.csv", header=TRUE, sep=";", as.is=TRUE)

#######First part: Discriptive analysis#######

###########Q/A###########
# Number of observational unites
dim(D)[1]
# Names of the variables:
names(D)
# Missing data
sum(is.na(D))

############Q/B###########
# Calculation of BMI scores, adding to data frame as "bmi"
D$bmi <- D$weight / (D$height/100) ^ 2
# Testing the new set of names and some BMI scores
head(D)
# Density histogram of the BMI scores
hist(D$bmi, xlab="BMI", prob=TRUE, main="Histogram of the BMI scores")
# Finding the meadian and the mean of BMI scores to verify the histogram is right-skewed
median(D$bmi)
mean(D$bmi)

###########Q/C############
# Dividing data into two subsets based on gender
Dfemale <- subset(D, gender == 0)
Dmale <- subset(D, gender == 1)
# Making separate density histograms of the subsets
hist(Dfemale$bmi, xlab="BMI (female)", prob=TRUE, main="Histogram of the BMI scores of women")
hist(Dmale$bmi, xlab="BMI (male)", prob=TRUE, main="Histogram of the BMI scores of men")
# Calculating the means and medians of the subsets
mean(Dfemale$bmi)
median(Dfemale$bmi)
mean(Dmale$bmi)
median(Dmale$bmi)

###########Q/D############
# Making box plot of the BMI scores by gender
boxplot(Dfemale$bmi, Dmale$bmi, names=c("Female", "Male"), xlab="Gender", ylab="BMI")

###########Q/E############
# Total number of observations
sum(!is.na(D$bmi), na.rm=TRUE)
# Mean of BMI scores, gender combined
mean(D$bmi, na.rm=TRUE)
# Median of BMI scores, gender combined
median(D$bmi, na.rm=TRUE)
# Sample variance of BMI scores, gender combined
var(D$bmi, na.rm=TRUE)
# Sample standard deviation of BMI scores, gender combined
sd(D$bmi, na.rm=TRUE)
# Finding lower (25%) and upper (75%) quartiles of the sample of BMI scores, gender combined
quantile(D$bmi, na.rm=TRUE)
---------------------------------
# Total number of observations of women
sum(!is.na(Dfemale$bmi), na.rm=TRUE)
# Mean of BMI scores of females
mean(Dfemale$bmi, na.rm=TRUE)
# Median of BMI scores of females
median(Dfemale$bmi, na.rm=TRUE)
# Sample variance of BMI scores of females 
var(Dfemale$bmi, na.rm=TRUE)
# Sample standard deviation of BMI scores of females
sd(Dfemale$bmi, na.rm=TRUE)
# Finding lower (25%) and upper (75%) quartiles of the sample of BMI scores of females
quantile(Dfemale$bmi, na.rm=TRUE)
---------------------------------
# Total number of observations of males
sum(!is.na(Dmale$bmi), na.rm=TRUE)
# Mean of BMI scores of males
mean(Dmale$bmi, na.rm=TRUE)
# Median of BMI scores of males
median(Dmale$bmi, na.rm=TRUE)
# Sample variance of BMI scores of males 
var(Dmale$bmi, na.rm=TRUE)
# Sample standard deviation of BMI scores of males
sd(Dmale$bmi, na.rm=TRUE)
# Finding lower (25%) and upper (75%) quartiles of the sample of BMI scores of males
quantile(Dmale$bmi, na.rm=TRUE)

#######Second part: Statistical analysis#######

###########Q/F############
# Adding log-transformation of BMI scores as a new vaiable to dataset
D$logbmi <- log(D$bmi)
# Creating qq-plot of log-transformed BMI
qqnorm(D$logbmi)
qqline(D$logbmi)
# Estimation of model parameters; mean and standard deviation of logbmi
mean(D$logbmi)
sd(D$logbmi)
# CLT
N1 = (D$logbmi-mean(D$logbmi))*1/sd(D$logbmi)
N2 = (D$logbmi-mean(D$logbmi))/sd(D$logbmi)/sqrt(2)
N10 = (D$logbmi-mean(D$logbmi))/sd(D$logbmi)/sqrt(10)
N30 = (D$logbmi-mean(D$logbmi))/sd(D$logbmi)/sqrt(30)

hist(N1, col="blue", main="n = 1", xlab="Sample means", ylab="Frequency", xlim=c(-1,1))
hist(N2, col="blue", main="n = 2", xlab="Sample means", ylab="Frequency", xlim=c(-1,1))
hist(N10, col="blue", main="n = 10", xlab="Sample means", ylab="Frequency", xlim=c(-1,1))
hist(N30, col="blue", main="n = 30", xlab="Sample means", ylab="Frequency", xlim=c(-1,1))
###########Q/G############
# Giving the t-quantiles with n=144 degrees of freedom
qt(0.975, 144)
# Giving the CI of mean of logbmi
t.test(D$logbmi, conf.level = 0.975)
# Taking the exponential of CI of mean of logbmi
exp(3.193203)
exp(3.242078)

###########Q/H############
# Giving tobs
tobs = (mean(D$logbmi)-log(25)) / (sd(D$logbmi) / sqrt(dim(D)[1]))
# Giving the p-value
pvalue = 2*(1-pt(abs(tobs),df=dim(D)[1]-1))
# Comparing the reults of the t-test with results in R
t.test(D$logbmi, mu=log(25))

###########Q/I############
# Adding log-transformation of BMI scores of women as a new vaiable to dataset Dfemale
Dfemale$logbmi <- log(Dfemale$bmi)
# Creating qq-plot of log-transformed BMI for females
qqnorm(Dfemale$logbmi)
qqline(Dfemale$logbmi)
# Adding log-transformation of BMI scores of men as a new vaiable to dataset Dmale
Dmale$logbmi <- log(Dmale$bmi)
# Creating qq-plot of log-transformed BMI for males
qqnorm(Dmale$logbmi)
qqline(Dmale$logbmi)
# Estimation of model parameters; mean and standard deviation of logbmi of females
mean(Dfemale$logbmi)
sd(Dfemale$logbmi)
# Estimation of model parameters; mean and standard deviation of logbmi of males
mean(Dmale$logbmi)
sd(Dmale$logbmi)

###########Q/I############
# Giving the CI of mean of logbmi of females
exp(t.test(Dfemale$logbmi, conf.level = 0.95)$conf.int)
# Giving the CI of mean of logbmi of females
exp(t.test(Dmale$logbmi, conf.level = 0.95)$conf.int)

###########Q/K############
# Giving tobs of two-sample setup
ms <- c(mean(Dmale$logbmi), mean(Dfemale$logbmi))
vs <- c(sd(Dmale$logbmi)^2, sd(Dfemale$logbmi)^2)
ns <- c(73, 72)
tobs2 = (ms[1]-ms[2])/sqrt(vs[1]/ns[1]+vs[2]/ns[2])
# Giving degrees of freedom of tobs2
v = ((vs[1]/ns[1]+vs[2]/ns[2])^2)/((vs[1]/ns[1])^2/(ns[1]-1)+(vs[2]/ns[2])^2/(ns[2]-1))
# Giving the p-value
pvalue2 = 2*(1-pt(abs(tobs2), df=133.7501))
# Comparing the reults of the t-test with results in R
t.test(D$logbmi[D$gender == 0], D$logbmi[D$gender == 1])

###########Q/L############
# Correlation between BMI and weight
cov(D$bmi, D$weight)/(sd(D$bmi)*sd(D$weight))
# Correlation between selected variables
cor(D[,c("weight","fastfood","bmi")], use="pairwise.complete.obs")
# Scatter-plots of different variables
plot(D$bmi, D$weight, xlab="BMI", ylab="weight", main="r = 0.828261")
plot(D$bmi, D$fastfood, xlab="BMI", ylab="Fast food", main="r = 0.1531578")
plot(D$weight, D$fastfood, xlab="Weight", ylab="Fast food", main="r = 0.2793223")
