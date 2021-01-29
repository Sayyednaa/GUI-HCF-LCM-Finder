# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x
# num = int(input('Enter First Number:\n'))
# ns = int(input('Enter Second Number:\n'))
# hcf = compute_hcf(num, ns)
# print("The HCF is", hcf)