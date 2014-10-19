
library(plyr)
set.seed(42)

n <- 1000

index <- 1:n

x_base <- round(rweibull(n, shape=2, scale=30))
x_1 <- pmax(3, x_base + rnorm(n, mean=0, sd=2))
x_2 <- pmax(3, x_base + rnorm(n, mean=2, sd=1))
x_3 <- pmax(3, x_base + rnorm(n, sample(c(-1, 0, 1, 2), n, replace=TRUE)))
x_4 <- x_base + rnorm(n)^2
x_5 <- sqrt(x_base)
x_true <- (x_base+x_1+x_2+x_3+x_4)/5

y_base <- ifelse(sample(c(TRUE, FALSE), n, replace=TRUE), 2*x_base, 3*x_base)

z_base <- sample(c(1:5/2, 1.5, 1.5), n, replace=TRUE)

color <- sample(rep(colorRampPalette(c("blue", "red"))(10), times=1:10), n, replace=TRUE)

noise_base <- pmax(3, round(rnorm(n, mean=100, sd=20)))
noise_diff <- noise_base + rnorm(n)

density <- sample(8:12/10, n, replace=TRUE)
coded_density <- mapvalues(density, 8:12/10, c(5, 1, 4, 2, 3))

response <- x_true * y_base * z_base * density + noise_diff - noise_base + index %% 3

data <- data.frame(x_1, x_2, x_3, x_4, x_5, y_base, z_base,
                   noise_base, noise_diff, color, coded_density)
data <- data[, sample(names(data))]
names(data) <- letters[1:ncol(data)]
data <- cbind(index, data, response)

train_i <- sample(index, 700)
train <- data[train_i, ]
test <- data[-train_i, ]

# recover perfectly
summary(lm(response ~ I(d-k) + I(index %% 3) + I((a+c+e+h+i^2)/5):b:j:factor(g), data=data))

rmse <- function(x, y) {
  return(sqrt(mean((x-y)^2)))
}
m <- lm(response ~ a, data=train)
p <- predict(m, test)
rmse(predict(m), train$response)
rmse(predict(m, test), test$response)

write.csv(train, 'train.csv', row.names=FALSE)
write.csv(test, 'test.csv', row.names=FALSE)
