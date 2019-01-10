setwd("/home/bebi/DTU_Studies/Applied Statistics/Day_2/Day2/")
process <- read.table("process.txt", header = TRUE)

## Determine whether air flow, temperature of water, or concentration of acid influence on the process loss by a graphical comparison.
pairs(process, panel = panel.smooth)

## Determine whether air flow, temperature of water or concentration of acid influence on the process loss by analysing each variable using simple linear regression.
lmAirflow <- lm(loss ~ airflow, data = process)
summary(lmAirflow)

lmWatertemp <- lm(loss ~ watertemp, data = process)
summary(lmWatertemp)

lmAcidconc <- lm(loss ~ acidconc, data = process)
summary(lmAcidconc)

## Determine whether air flow, temperature of water or concentration of acid influence on the process loss using multiple linear regression?
lm1 <- lm(loss ~ ., process)
summary(lm1)
lm2 <- update(lm1, ~. - acidconc)
summary(lm1)

## Is there evidence of multicollinearity? = independency
cor(process)

## Plot the residuals and analyse the results. Which x-variable should be removed if we want to reduce the model?
plot(lm1)
plot(lm2)




