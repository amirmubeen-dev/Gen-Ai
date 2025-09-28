import numpy as np

data = np.array([90, 85, np.nan, 70, 60, np.nan, 95])

print("Original:", data)

print("Is NaN?:", np.isnan(data))

mean_val = np.nanmean(data)  
cleaned = np.where(np.isnan(data), mean_val, data)

print("Cleaned Data:", cleaned)

high_scorers = cleaned[cleaned > 80]
print("High Scorers:", high_scorers)



