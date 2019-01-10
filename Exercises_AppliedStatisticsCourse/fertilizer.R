pairs(NOISE ~., filter)

# Plot data
par(mfrow = c(1,2))
boxplot(NOISE ~ size, df, xlab = "Gender", ylab = "Distance", col = c(2,3))
boxplot(Distance ~ Grade, df, xlab = "Grade", ylab = "Distance")
boxplot(Distance ~ Gender, df, xlab = "Gender", ylab = "Distance", col = c(2,3))
plot(as.numeric(df$Gender), df$Distance, col = as.numeric(df$Gender)+1, 
     pch = as.numeric(df$Grade), xlab = "Gender", ylab = "Distance")
legend("center", legend = c("Boys 7th", "Boys 8th", "Girls 7th", "Girls 8th"), col = c(2,2,3,3), pch = c(1,1,2,2))
