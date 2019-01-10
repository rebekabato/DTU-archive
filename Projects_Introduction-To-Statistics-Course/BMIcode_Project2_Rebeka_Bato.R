######################## Project 2###################################
# Topic: BMI survey
# Author: Rebeka Bato Julianna (s182575)
# deadline : 13th November

# Set working directory and read data
setwd("~/Project_2_BMI")
D <- read.table("bmi2_data.csv", header=TRUE, sep=";", as.is=TRUE)

# Add log-BMI as "logbmi" to he dataset
D$logbmi <- log(D$bmi)

###########Q/A###########
# Correlation between selected variables
cor(D[,c("logbmi","age","fastfood")], use="pairwise.complete.obs")

# Scatter plots of logbmi-age and logbmi-fastfood
plot(D$logbmi, D$age, xlab="Log-BMI Scores", ylab="Age", main="r ~ 0.185")
plot(D$logbmi, D$fastfood, xlab="Log-BMI Scores", ylab="Fast food consumption (days/year)", main="r ~ 0.046")

# Histograms for variables age, fastfood, logbmi
hist(D$age, xlab="Age", main="Histogram of Age", prob=TRUE)
hist(D$fastfood, xlab="Fast food consumption (days/year)", xlim= c(0, max(D$fastfood)+50), ylim = c(0, 0.065), main="Histogram of fast food consumption", prob=TRUE, nclass=32)
hist(D$logbmi, xlab="Log-BMI Scores", main="Histogram of Log-BMI Scores", prob=TRUE, xlim= c(min(D$logbmi)-0.1, max(D$logbmi)+0.1))

# Box-plots for variables age, fastfood, logbmi
boxplot(D$logbmi, ylab="Log-BMI Scores", main="Box plot of log-BMI scores")
text(1.3, quantile(D$logbmi), c("Minimum", "Q1", "Median", "Q3", "Maximum"), col="blue")

boxplot(D$age, ylab="Age", main="Box plot of Age")
text(1.3, quantile(D$age), c("Minimum", "Q1", "Median", "Q3", "Maximum"), col="blue")

boxplot(D$fastfood, ylab="Fast food consumption (days/year)", main="Box plot of fast food consumption")

# Missing data
sum(is.na(D))

# Calculate summary statistc
# Total number of observations
sum(!is.na(D$bmi), na.rm=TRUE)
# Mean of variables
mean(D$logbmi)
mean(D$age)
mean(D$fastfood)
# Variance of variables
var(D$logbmi)
var(D$age)
var(D$fastfood)
# Std. dev. of variables
sd(D$logbmi)
sd(D$age)
sd(D$fastfood)
# Q1, Q2, Q3 of the variables
quantile(D$logbmi)
quantile(D$age)
quantile(D$fastfood)

###########Q/B###########
# Subsets for the first 840 obs and for the rest
D_model <- subset(D, id <= 840)
D_test <- subset(D, id >= 841)

###########Q/C###########
# Estimate the parameters of the multiple linear regression model
fit <- lm(logbmi ~ age + fastfood, data=D_model)
summary(fit)

###########Q/D###########
# Plots for model validation
# Observations against fitted values
plot(fit$fitted.values, D_model$logbmi, xlab = "Fitted values", ylab = "log(BMI)", main="Observations against fitted values")

# Residuals against each of the explanatory variables
plot(D_model$age, fit$residuals, xlab = "Age", ylab = "Residuals")
plot(D_model$fastfood, fit$residuals, xlab = "Fastfood", ylab = "Residuals")

# Residuals against fitted values
plot(fit$fitted.values, fit$residuals, xlab = "Fitted values", ylab = "Residuals", main="Residuals against fitted values")

# Normal QQ-plot of the residuals
qqnorm(fit$residuals, ylab = "Residuals", xlab = "Theoretical Quantiles", main = "Q-Q plot of the residuals")
qqline(fit$residuals)

###########Q/E###########
# Calculate the t-quantiles with 837 degrees of freedom
qt(0.975, 837)
# 95% conf. interval for the model coeff.
confint(fit, level=0.95) # or
confint(lm(D_model$logbmi ~ D_model$age + D_model$fastfood))

###########Q/F###########
# Calculate t-stat and p-value manually
0.0023744 / 0.0003890
2*(1-pt(abs(6.104), df=837))

# Read off tobs and p-value
summary(fit)

###########Q/G###########
# Get p-values of estimators for the original model
summary(fit)
# Get p-values of estimator x1 for model without x2
summary(lm(D_model$logbmi ~ D_model$age))
# Get p-values of estimator x2 for model without x1
summary(lm(D_model$logbmi ~ D_model$fastfood))

# Get conf. int. of x1 for model without x2
confint(lm(D_model$logbmi ~ D_model$age))
# Get conf. int. of x2 for model without x1 
confint(lm(D_model$logbmi ~ D_model$fastfood))

###########Q/F###########
# Predictions and 95% prediction intervals of D_test
pred <- predict(fit, newdata = D_test, interval = "prediction", level = 0.95)
# Observed values and predictions in D_test
cbind(id=D_test$id, logbmi=D_test$logbmi, pred)
# Find the standard errors of the predictions for the line
pred <- predict(fit, newdata = D_test, interval = "prediction", level = 0.95, se = TRUE)
pred$se

