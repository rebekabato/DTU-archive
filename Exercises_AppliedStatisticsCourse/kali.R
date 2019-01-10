setwd("/home/bebi/DTU_Studies/Applied Statistics/Day_3/Day3/")
kali <- read.table("kali.txt", header=TRUE)

# summary and print out box plots/groups
summary(kali)
plot(kali)

## Use a non-parametric test to examine if the content of kali depends on the different productions.
# check if the category is factor, if not it has to be converted
str(kali)
# non-parametric alternative to ANOVA: Kruskal-Wallis
kruskal.test(kali ~ production, data = kali)

## Use a one-way ANOVA to examine if the content of kali depends on the different productions.
lmKali <- lm(kali ~ production, data = kali)
anova(lmKali)

par(mfrow = c(1,2))
plot(lmKali, col = kali$production, which = 1:2)

## If the content of kali depends on the different productions, which of the production(s) yield the highest content?
summary(lmKali)
# ProductionA (intercept) is the most significant, becase the std.error is the less there compared to the estimate