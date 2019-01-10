setwd("/home/bebi/DTU_Studies/Applied Statistics/1_Day/Day1 (2)/")
bodyfat <- read.table("bodyfat.txt", header=TRUE)

# Can the data in each group (gender) be assumed to be normally distributed?
bodyfat$logfatpc <- log(bodyfat$fatpct)
qqnorm(bodyfat$logfatpc[bodyfat$gender=="m"])
qqline(bodyfat$logfatpc[bodyfat$gender=="m"])

qqnorm(bodyfat$logfatpc[bodyfat$gender=="f"])
qqline(bodyfat$logfatpc[bodyfat$gender=="f"])

# Is there a difference in the percentage of body fat for men and women? Perform a t-test?
x <- c(bodyfat$logfatpc[bodyfat$gender=="m"])
y <- c(bodyfat$logfatpc[bodyfat$gender=="f"])
t.test(x, y)
# since p-value > 0.05 we accept (cannot reject) H0: mean(male) = mean(female)

# par function -> place plots next to each other

# Is there a difference in the percentage of body fat for men and women? Perform a non-parametric test
wilcox.test(x, y)
# since p-value > 0.05 we cannot reject the HO: mean(male) = mean(female)