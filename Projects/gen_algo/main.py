''' The problem: Maximizing the percentage of time spent being productive while still finding time to be happy 
    ASSUMPTIONS:
        - Percents are displayed in integers (70 = 0.7 or 70%)
        - Items to complete are no more than 3
        - Optimal percentages are given as a reference
'''

class SolvingMyProblem(object):
    OPTIMAL_PROD = 70
    OPTIMAL_LAZY = 30
    MAX_ITEMS = 3
    def population(self):
        # This will be the percentage of time I spend being productive (HW, personal projects, home projects, etc. )
        self.productiveTime = 0
        # This will be the percentage of time I spend doing "unproductive" things (hobbies, Netflix, etc.)
        self.lazyTime = 0
    
    def fitness_function(self ,prod_perc, lazy_perc, itemsToComplete):
        # In general, if the productive time is greater than the lazy time, then the solution is good.
        # This function will determine a score for the best possible time usage based on the optimal rates,
        #   and each percentage will be within range of +/- 20 of the optimal levels
        # itemsToComplete will be assumed to be no more than 3 for this particular model.

        self.fit_score = 0
        # run through the number of items to complete
        for i in range(0, itemsToComplete):

            # if the prod percent is higher, the fit_score will be both percents added with an additional reward of
            # the items * 10 
            if prod_perc > lazy_perc:
                self.fit_score = (prod_perc + lazy_perc + (itemsToComplete * 10)) - 10
            # if the lazy percent is higher, the fit_score will be the sum of both percents with a penalty of 
            # items * 10, then divided by 2
            elif lazy_perc < prod_perc:
                self.fit_score = lazy_perc + prod_perc - ((itemsToComplete * 10) / 2)

            def __check_optimal_prod(p):
                if p > OPTIMAL_PROD:
                    return True
                return False
            
            def __check_optimal_lazy(p):
                if p > OPTIMAL_LAZY:
                    return True
                return False
        return self.fit_score
