setwd("/home/bebi/DTU_Studies/Applied Statistics/1_Day/Day1 (2)/")
calcium<-read.table("calcium.txt", header=TRUE)

## What statistical test is appropriate for comparing the change in blood pressure between the treatment and placebo groups?
## -> wilcox.text () -> for non-parametric test when not assuming any distribution

## May the data in each group be considered as being normally distributed?
## H0: it is normally ditr.
shapiro.test(calcium$Decrease[calcium$Treatment=="Calcium"])
shapiro.test(calcium$Decrease[calcium$Treatment=="Placebo"])
## since  p-values are >> 0.05 in both cases, we cannot reject that there is normality

x <- calcium$Decrease[calcium$Treatment=="Calcium"]
y <- calcium$Decrease[calcium$Treatment=="Placebo"]

## Test whether the variance in each group can be assumed to be the same
var.test(x,y)
## p-value > 0.05, so we cannot reject that the variance is the same for the groups

## Make a graphical comparison of the treatment means.
boxplot(Decrease ~ Treatment, data = calcium)
points(tapply(calcium$Decrease, calcium$Treatment, mean), col="blue")

## Make the statistical test for comparing the change in blood pressure between the treatment and placebo groups. What is your conclusion? What is the p-value of the test?
t.test(x, y)
## p-value > 0.05, we cannot reject the H0 : mean(x) = mean(y)

## Which non-parametric test could be used if data cannot be assumed to be normally distributed?
wilcox.test(x, y)


