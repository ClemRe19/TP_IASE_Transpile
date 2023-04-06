module linear_regression (size, price);
    input [15:0] size;
    output [31:0] price;

    reg signed [31:0] b0 = 10000;
    reg signed [31:0] b1 = 10000;

    reg signed [31:0] y_int;
    reg signed [31:0] x_int;
    always @(*) begin
        x_int = b1 * size;
        y_int = b0 + x_int;
        price = y_int;

    end

endmodule