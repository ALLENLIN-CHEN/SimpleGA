# 0.0 coding:utf-8 0.0
# 找出最优解和最优解的基因编码

#每一个pop个体与对应的fitvalue位置一一对应，这里原来取的是最大值
def best(pop, fit_value):
    px = len(pop)
    best_individual = []
    best_fit = fit_value[0]
    print fit_value
    for i in range(1, px):
        if(fit_value[i] > best_fit):
            best_fit = fit_value[i]
            best_individual = pop[i]
    print best_individual
    return [best_individual, best_fit]

if __name__ == '__main__':
    pass
