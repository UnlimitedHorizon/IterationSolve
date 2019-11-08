class IterationSolve:
    def __init__(self):
        super().__init__()
        self.f = open("output.txt", "w")
        self.IterationFunction1 = lambda x : 20/(x**2+2*x+10)
        self.IterationFunction2 = lambda x : (20-2*x**2-x**3)/10
        self.IterationFunctionNewton = lambda x : x - (x**3 + 2*x**2 + 10*x - 20)/(3*x**2 + 4*x + 10)
        self.precision = 1e-9
        self.max_iteration_num = 500
        self.x0 = 1

    def __del__(self):
        self.f.close()

    def SteffensenFunction(self, iteration_function, x):
        x_i1 = iteration_function(x)
        x_i2 = iteration_function(x_i1)
        x_next = (x*x_i2 - x_i1**2)/(x_i2 - 2*x_i1 + x)
        return x_next

    def IterationSolve(self, iteration_function):
        result_list=[self.x0]
        while len(result_list) <= self.max_iteration_num:
            x_current = result_list[-1]
            x_next = iteration_function(x_current)
            result_list.append(x_next)
            if abs(x_next - x_current) <= self.precision:
                break
        else:
            print("after {} iterations, the precision can't get below {}".format(self.max_iteration_num, self.precision))
        return result_list

    def SteffensenSolve(self, iteration_function):
        result_list=[self.x0]
        while len(result_list) <= self.max_iteration_num:
            x_current = result_list[-1]
            x_next = self.SteffensenFunction(iteration_function, x_current)
            result_list.append(x_next)
            if abs(x_next - x_current) <= self.precision:
                break
        else:
            print("after {} iterations, the precision can't get below {}".format(self.max_iteration_num, self.precision))
        return result_list

    def PrintResult(self, result_list):
        l = len(result_list)
        if l > self.max_iteration_num:
            self.f.write("!!!After {} iterations, the precision can't get below {}\n".format(self.max_iteration_num, self.precision))
        else:
            self.f.write("It takes {} iterations, to get a result with the precision below {}\n".format(l-1, self.precision))
        if l > 20:
            self.f.write("result list:\n{}\n\n".format(result_list[0:9] + ["..."] + result_list[-10:]))
        else:
            self.f.write("result list:\n{}\n\n".format(result_list))




# def IterationFunction1(x):
#     x_next = 20/(x**2+2*x+10)
#     return x_next

# def IterationFunction2(x):
#     x_next = (20-2*x**2-x**3)/10
#     return x_next

# def IterationFunctionNewton(x):
#     x_next = x - (x**3 + 2*x**2 + 10*x - 20)/(3*x**2 + 4*x + 10)
#     return x_next

iteration_solve = IterationSolve()
iteration_solve.PrintResult(iteration_solve.IterationSolve(iteration_solve.IterationFunction1))
iteration_solve.PrintResult(iteration_solve.IterationSolve(iteration_solve.IterationFunction2))
iteration_solve.PrintResult(iteration_solve.SteffensenSolve(iteration_solve.IterationFunction1))
iteration_solve.PrintResult(iteration_solve.SteffensenSolve(iteration_solve.IterationFunction2))
iteration_solve.PrintResult(iteration_solve.IterationSolve(iteration_solve.IterationFunctionNewton))

# PrintResult(f, IterationSolve(IterationFunction1))
# PrintResult(f, IterationSolve(IterationFunction2))
# PrintResult(f, SteffensenSolve(IterationFunction1))
# PrintResult(f, SteffensenSolve(IterationFunction2))
# PrintResult(f, IterationSolve(IterationFunctionNewton))

# f.close()
print("finish!")