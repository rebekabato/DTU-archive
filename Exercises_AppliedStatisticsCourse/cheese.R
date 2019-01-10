setwd("/home/bebi/DTU_Studies/Applied Statistics/Day_2/Day2/")
cheese <- read.table("cheese.txt", header = TRUE)

## Use scatterplots, correlation, and simple regression to examine the relationships among the individual variables.
pairs(cheese, panel = panel.smooth)
cor(cheese)
lmAcetic <- lm(taste ~ Acetic, data = cheese)
summary(lmAcetic)

lmH2S <- lm(taste ~ H2S, data = cheese)
summary(lmH2S)

lmLactic <- lm(taste ~ Lactic, data = cheese)
summary(lmLactic)

## Why do you think acetic and h2s has been transformed?
par(mfrow = c(2,2))
plot(taste ~ Acetic, data = cheese)
abline(lmAcetic)

plot(taste ~ H2S, data = cheese)
abline(lmH2S)

cheese$expAcetic <- exp(cheese$Acetic)
cheese$expH2S <- exp(cheese$H2S)

plot(taste ~ expAcetic, data = cheese)
lmexpAcetic <- lm(taste ~ expAcetic, data = cheese)
abline(lmexpAcetic)
# the intercept is not significant here, we need to apply lof transpormation? 

plot(taste ~ expH2S, data = cheese)
lmexpH2S <- lm(taste ~ expH2S, data = cheese)
abline(lmexpH2S)

## Predict the ’taste’ of a cheese where (log) acetic is 5.3, (log) h2s is 8.0 and lactic is 3.0.
lm1 <- lm(taste ~ Acetic, H2S, Lactic, data = cheese)
predict(lm1, data.frame(Acetic=5.3, H2S=8.0, Lactic=3.0, Case=31), interval = "prediction")
## since the lctic = 3 which is higher than the max value of lactic in the data, the lwr and the upr limit of prediction interval are growing (as we getting far from the data we had) 