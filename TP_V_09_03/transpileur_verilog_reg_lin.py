from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

n_features = 5
input_bits = 16

df = pd.read_csv('houses.csv')
train,test = train_test_split(df)

X_train = train.drop(columns = ['price'])
y_train = train['price']

model = LinearRegression()
model = model.fit(X_train,y_train)

coef = model.coef_
intercept = model.intercept_

verilog_code = ""
verilog_code += "module regression_lineaire ("
for i in range(n_features):
    verilog_code += "x{0},".format(i)
verilog_code += "y);\n\n"

for i in range(n_features):
    verilog_code += "input signed [{0}-1:0] x{1};\n".format(input_bits, i)
verilog_code += "output signed [{0}-1:0] y;\n\n".format(input_bits)

verilog_code += "reg signed [{0}-1:0] y_int;\n".format(input_bits)
verilog_code += "reg signed [{0}-1:0] x_int;\n\n".format(input_bits)

verilog_code += "always @(*) begin\n"
verilog_code += "    y_int = {0}'d{1};\n".format(input_bits, int(intercept))
for i in range(n_features):
    verilog_code += "    x_int = {0}'d{x_val};\n".format(input_bits, x_val=int(coef[i]))
    verilog_code += "    y_int = y_int + x{0} * x_int;\n".format(i)
verilog_code += "    y = y_int;\n"
verilog_code += "end\n\n"

verilog_code += "endmodule\n"


with open("regression_lineaire.v", "w") as f:
    f.write(verilog_code)