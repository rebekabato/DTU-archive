setwd("/home/bebi/DTU_Studies/Applied Statistics/1_Day/Day1 (2)/")
labor <- read.table("labor.txt", header=TRUE)

## Compare LFPR rates in the two years with a pooled t-test since the United States did not change much from 1968 to 1972
x <- labor$x1972
y <- labor$x1968

## POOLED
t.test(x, y, var.equal = TRUE)

## PAIRED
t.test(x, y, paired = TRUE)

## Which of the two methods you have used do you find most appropriate?
## If there is paired data, we always have to use the paired t.test and never the pooled one, because there is significant difference between the p-values

## If you have found a significant change - how big is this change then?
t.test(x, y, paired = TRUE)
## -> 95% confidence interval..
## -> sample estimates:
## mean of the differences 
## 0.03368421 