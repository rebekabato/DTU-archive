setwd("/home/bebi/DTU_Studies/Applied Statistics/Day_2/Day2/")
brain <- read.table("brainweight.txt", header = TRUE)

## Make a scatterplot of body against brain. Do you see any correlation?
plot(body ~ brain, data = brain)
lm1 <- lm(body ~ brain, data = brain)
abline(lm1)
cor(brain$body, brain$brain)
## cor = 0.9341638, we can state that there is correlation btw weight of body and brain)

## Make a log transform of both body and brain. Make a scatterplot of the transformed variables. Compute the correlation.
brain$logbody <- log(brain$body)
brain$logbrain <- log(brain$brain)

plot(logbody ~ logbrain, data = brain)
lm2 <- lm(logbody ~ logbrain, data = brain)
abline(lm2)
cor(brain$logbody, brain$logbrain)

## Fit a regression model between log(body) and log(brain).Above!

## Is there any outlier in the data?
# Plot 95% confidence intervals for the regression line
x.new <- seq(min(brain$logbrain), max(brain$logbrain))
pred.x <- data.frame(logbrain = x.new)
range.pred <- predict(lm2, newdata = pred.x, interval = "confidence")
plot(logbody ~ logbrain, data = brain, pch = 19)
lines(x.new, range.pred[,1], lw = 2)
lines(x.new, range.pred[,2], col = 2, lw = 2)
lines(x.new, range.pred[,3], col = 2, lw = 2)
legend("topleft", legend = c("prediciton interval","confidence interval"), col = c("green", "red"), lty = c(2, 1))

# Plot 95% prediction intervals using function matlines
range.pred <- predict(lm2, newdata = pred.x, interval = "prediction")
matlines(x.new, range.pred[,2:3], lty = 2, col = 3, lw = 2)
# Outlier data is outside of the pred. interval

## How would you evaluate the fit of the model?
summary(lm2)

par(mfrow = c(2,2))
plot(lm2)




