setwd("/home/bebi/DTU_Studies/Applied Statistics/1_Day/Day1 (2)/")
clima<-read.table("clima.txt", header=TRUE)

# Plot the two time series and compute the correlation
plot(clima$time, clima$denmark, xlab="Time", ylab ="Denmark",ylim = c(-12,3))
points(clima$time, clima$greenland, xlab="Time", ylab="Greenland")
plot(clima$greenland, clima$denmark, xlab="", ylab ="Denmark")
cor(clima$denmark, clima$greenland)
# cor(clima[,c("denmark","greenland")], use="pairwise.complete.obs") - pairwise comparison

# do a subset of data between 1900 - 1960
clima1960 <- clima[clima$time<1961,]

# Is the temperature in Denmark increasing when considering the time series 1900-1960?
plot(clima1960$time, clima1960$denmark, xlab="Time", ylab="Denmark")
cor(clima1960$time, clima1960$denmark)

# Is the temperature in Denmark increasing when considering the time series 1960-2000?
clima60to2000 <- clima[clima$time>1961,]
plot(clima60to2000$time, clima60to2000$denmark, xlab="Time", ylab="Denmark")
cor(clima60to2000$time, clima60to2000$denmark)

