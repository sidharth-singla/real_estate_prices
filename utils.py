import re

def process_prop_type(x):
    x = x.strip()[:-3]
    try:
        x = float(eval(x))
    except:
        x = re.sub("\D", "", x)
        if(x is None or (x=='')):
            x=0
        else:
            x = float(x)
    return x

def process_prop_area(x):
    try:
        x = float(x)
    except:
        if 'to' in x:
            xs = x.split()
        elif ',' in x:
            xs = x.split(',')
        elif x.endswith('+'):
            xs = [x.split(' ')[0]]
        else:
            xs=[0]
        x = (float(xs[0]) + float(xs[-1]))/2
    return x

# Function to detect outliers using IQR
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)  # First quartile (25th percentile)
    Q3 = df[column].quantile(0.75)  # Third quartile (75th percentile)
    IQR = Q3 - Q1  # Interquartile range
    lower_bound = Q1 - 1.5 * IQR  # Lower outlier threshold
    upper_bound = Q3 + 1.5 * IQR  # Upper outlier threshold
    
    # Identify outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers