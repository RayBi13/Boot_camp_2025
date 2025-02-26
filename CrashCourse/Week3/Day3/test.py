# # EXO 6


# import numpy as np
# import scipy.stats as stats



# productivity_before = np.random.normal(loc=50, scale=10, size=30)
# productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)

# # Hypothèse :
# # H0 : Le programme de formation n'a aucun effet sur la productivité (différence moyenne = 0).
# # H1 : Le programme de formation augmente la productivité (différence moyenne > 0).

# # Perform a paired t-test
# t_stat, p_value = stats.ttest_rel(productivity_after, productivity_before)

# # Calculate the mean difference
# mean_difference = np.mean(productivity_after) - np.mean(productivity_before)

# # Print results
# print("Mean productivity before training: {:.2f}".format(np.mean(productivity_before)))
# print("Mean productivity after training: {:.2f}".format(np.mean(productivity_after)))
# print("Mean Difference: {:.2f}".format(mean_difference))
# print("T-Statistic: {:.2f}".format(t_stat))
# print("P-Value: {:.10f}".format(p_value))

# # Conclusion
# alpha = 0.05  # Significance level
# if p_value < alpha:
#     print("Result: The training program significantly improves productivity (Reject H0).")
# else:
#     print("Result: No significant effect of the training program (Fail to reject H0).")

#     ------------------------------------------


import numpy as np
import scipy.stats as stats

# Productivity scores of employees before the training program
productivity_before = np.random.normal(loc=50, scale=10, size=30)

# Productivity scores of the same employees after the training program
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)

# Performing a paired t-test
t_stat, p_value = stats.ttest_rel(productivity_before, productivity_after)
print("t-statistic:", t_stat)
print("p-value:", p_value)