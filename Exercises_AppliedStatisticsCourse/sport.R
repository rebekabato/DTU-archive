setwd("/home/bebi/DTU_Studies/Applied Statistics/Day_2/Day2/")
sport <- read.table("sport.txt", header = TRUE)

## Make appropriate plots for the different sport disciplines. Is there a tendency?
## exclude the data before 1900
sport1900 <- sport[sport$year>-1,]

par(mfrow=c(2,2))
plot(sport1900$high.jump ~ sport1900$year)
lm1 <- lm(sport1900$high.jump ~ sport1900$year)
abline(lm1)

plot(sport1900$Discus.Throw ~ sport1900$year)
lm2 <- lm(sport1900$Discus.Throw ~ sport1900$year)
abline(lm2)

plot(sport1900$long.jump ~ sport1900$year)
lm3 <- lm(sport1900$long.jump ~ sport1900$year)
abline(lm3)

## the Mexico City Olympics in 1968 saw unusually good track and field performances, possibly because of the high altitude. To investigate this question we must establish some expected performance level.
## exclude the outlier row from data
sportNO68 <- sport1900[!(sport1900$year == 68),]
## create plot with prediction interval
par(mfrow=c(1,1))
plot(sportNO68$long.jump ~ sportNO68$year, ylim = c(280, 400))
lm4 <- lm(long.jump ~ year, data = sportNO68)
abline(lm4)

## calculate the prediction interval and show it up on the plot
range.pred <- predict(lm4, data.frame(YEAR = sportNO68$year), interval = "prediction")
matlines(sportNO68$year, range.pred[,2:3], col = 3, lty = c(2,2))

## add the examined value (in year 68) to the plot
points(sport$long.jump[sport$year == 68] ~ sport$year[sport$year == 68], 
       ylim = c(280, 400), pch = 2)
legend("topleft", legend = "prediciton interval", col = "green", lty = 2)
## pch is for different sign for the new point

## Could you predict the winning result in long jump for the Olympic games in Greece 2004?
predict(lm4, data.frame(year = 104), interval = "prediction")






