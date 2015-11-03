setwd("~/Documents/coursera_data_manipulation/assignment5")

sea <- read.csv("seaflow_21min.csv")

# Q2 How many particles labeled "synecho" are in the file provided?
sum(sea$pop == 'synecho')
# Q3 What is the 3rd Quantile of the field fsc_small?
summary(sea$fsc_small)
# Q4 What is the mean of the variable "time" for your training set?
mean(sea$time)

# Plot for Q5
library(ggplot2)
g <- ggplot(sea, aes(pe, chl_small, color = factor(pop))) +
  geom_point()
g

# Train a decision tree
# Q6, 7, 8
library(rpart)
fol <- formula(pop ~  fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
tree <- rpart(fol, method="class", data=sea)
print(tree)
# Q9 test the model
tp <- predict(tree, type = "class")
sum(tp == sea$pop)/dim(sea)[1]

# Train a random forest
library(randomForest)
rf <- randomForest(fol, sea) 
tr <- predict(rf)
# Q10 evaluate the rf
sum(tr == sea$pop)/dim(sea)[1]
# Q11 finding the most important factor
importance(rf)

# Train a svm
library(e1071)
mm <- svm(fol, sea)
ts <- predict(mm)
# Q12
sum(ts == sea$pop)/dim(sea)[1]

# Create confusion table for all 3 models
tt <- table(tp, sea$pop)
rt <- table(tr, sea$pop)
mt <- table(ts, sea$pop)
tt;rt;mt;
# Remove file_id == 208 & check the result
ssea <- sea[!(sea$file_id == 208), ]
smm <- svm(fol, ssea)
smp <- predict(smm)
sum(smp == ssea$pop)/dim(ssea)[1] - sum(ts == sea$pop)/dim(sea)[1]

g2 <- ggplot(sea, aes(time, fsc_big)) +
  geom_point()
g2
