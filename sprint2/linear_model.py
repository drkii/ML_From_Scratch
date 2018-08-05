class LinearModel():

    def __init__(self):
        pass

    def compute_cost(self, X, y, theta):
        #sample 数
        ids = len(X)
        #naiseki
        naiseki = np.dot(X, theta)
        #distance
        distance = (naiseki - y) # (Hypothesis value -- Actual value)
        #distance**2 の合計
        total_distance = (distance**2).sum()
        #total_distanceの平均
        J = total_distance / (2 * ids)
        return J

    def gradient_descent(self, X, y, theta, iterations, alpha):
        #ここにいれていく
        past_costs = []
        past_thetas = [theta]
        m = len(X)

        for i in range(iterations):
            #距離を出す
            distance = (np.dot(X, theta) - y)
            #勾配を出す
            gradient = np.dot(X.T, distance) /m
            #thetaを更新
            theta = theta - (alpha * gradient)
            # New Cost
            new_cost = compute_cost(X, y, theta)

            # thetaとcostを保持する変数past_costsとpast_thetasに順次過去の値をappendする
            past_costs.append(new_cost)
            past_thetas.append(theta)
        return past_costs, past_thetas

    def plot_learning_curve(self, X, y, theta, alpha, iterations):
      past_costs, _ =gradient_descent(X, y, theta, alpha, iterations)
      plt.xlabel('No.of iterations')
      plt.ylabel('Cost')
      plt.title("Cost Function")
      print("last cost : {}".format(past_costs[-1]))
      print("learning rate : {}".format(alpha))
      print("iteration : {}".format(iterations))
      plt.plot(past_costs)
