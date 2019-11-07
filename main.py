

def IterationFunction1(x):
    x_next = 20/(x**2+2*x+10)
    return x_next

def IterationFunction2(x):
    x_next = (20-2*x**2-x**3)/10
    return x_next

def IterationFunctionNewton(x):
    x_next = x - (x**3 + 2*x**2 + 10*x - 20)/(3*x**2 + 4*x + 10)
    return x_next

def IterationSolve(iteration_function, x0=1, precision=1e-9, max_iteration_num=1000):
    result_list=[x0]
    while len(result_list)<=max_iteration_num:
        x_current = result_list[-1]
        x_next = iteration_function(x_current)
        result_list.append(x_next)
        if abs(x_next - x_current)<=precision:
            break
    else:
        print("after {} iterations, the precision can't get below {}".format(max_iteration_num, precision))
    return result_list

def SteffensenFunction(iteration_function, x):
    x_i1 = iteration_function(x)
    x_i2 = iteration_function(x_i1)
    x_next = (x*x_i2 - x_i1**2)/(x_i2 - 2*x_i1 + x)
    return x_next

def SteffensenSolve(iteration_function, x0=1, precision=1e-9, max_iteration_num=1000):
    result_list=[x0]
    while len(result_list)<=max_iteration_num:
        x_current = result_list[-1]
        x_next = SteffensenFunction(iteration_function, x_current)
        result_list.append(x_next)
        if abs(x_next - x_current)<=precision:
            break
    else:
        print("after {} iterations, the precision can't get below {}".format(max_iteration_num, precision))
    return result_list

def PrintResult(f, result_list, precision=1e-9, max_iteration_num=1000):
    l = len(result_list)
    if l > max_iteration_num:
        f.write("!!!After {} iterations, the precision can't get below {}\n".format(max_iteration_num, precision))
    else:
        f.write("It takes {} iterations, to get a result with the precision below {}\n".format(l-1, precision))
    if l > 20:
        f.write("result list:\n{}\n\n".format(result_list[0:9] + ["..."] + result_list[-10:]))
    else:
        f.write("result list:\n{}\n\n".format(result_list))




f = open("output.txt", "w")

PrintResult(f, IterationSolve(IterationFunction1))
PrintResult(f, IterationSolve(IterationFunction2))
PrintResult(f, SteffensenSolve(IterationFunction1))
PrintResult(f, SteffensenSolve(IterationFunction2))
PrintResult(f, IterationSolve(IterationFunctionNewton))

f.close()
print("finish!")