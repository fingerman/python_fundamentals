import numpy as np
import matplotlib.pyplot as plt



class LinearRegressionGD:
    def __init__(self, eta=0.0001, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        # weights
        # array with 0s, for each x_i in X
        # shape[1] is the number of coulmns
        self.w_ = np.zeros(1 + X.shape[1])


        # save the progress of the cost function (MSE)
        self.cost_ = []


        for i in range(self.n_iter):

            # calculate
            output = self.predict(X)

            # y_predicted - y_real
            errors = y.flatten() - output

            # loss function computes the error for a single training example
            mse = ((errors**2).sum()/2)/len(X)

            # cost function is the average of the loss functions
            self.cost_.append(mse)

            # betas. Adjust it
            self.w_[1:] += self.eta * X.T.dot(errors)

            # adjust the  intercept
            self.w_[0] += self.eta * errors.sum()

        return self







    def predict(self, X):
        # y = X*b + b_0
        return np.dot(X, self.w_[1:]) + self.w_[0]



# dataset
X = 2 * np.random.rand(1000, 1)
#print(X.shape)
y = 5 + 2 * X + np.random.randn(1000, 1)

#plt.plot(X, y, 'o')
#plt.show()

# model
lrGD = LinearRegressionGD(n_iter=30)


lrGD.fit(X, y)

#training

plt.plot(X, y, 'o')
plt.plot(X, lrGD.predict(X), 'r-', linewidth=1)
plt.show()


plt.plot(range(1, lrGD.n_iter + 1), lrGD.cost_)
plt.xlabel('Epochs')
plt.ylabel('SSE')
plt.show()


# standardize

X_std = (X-X.mean())/X.std()
y_std = (y-y.mean())/y.std()

lrGD_S = LinearRegressionGD(n_iter=30)
lrGD_S.fit(X_std, y_std)
plt.plot(X_std, y_std, 'o')
plt.plot(X_std, lrGD_S.predict(X), 'r-', linewidth=1)
plt.show()


plt.plot(range(1, lrGD_S.n_iter + 1), lrGD_S.cost_)
plt.xlabel('Epochs')
plt.ylabel('SSE')
plt.show()


