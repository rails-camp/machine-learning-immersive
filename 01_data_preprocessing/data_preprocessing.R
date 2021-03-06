# Import the CSV data
raw_data = read.csv('raw_data.csv')
# Fix missing data
raw_data$Age = ifelse(is.na(raw_data$Age),
                      ave(raw_data$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                      raw_data$Age)
raw_data$Income = ifelse(is.na(raw_data$Income),
                      ave(raw_data$Income, FUN = function(x) mean(x, na.rm = TRUE)),
                      raw_data$Income)