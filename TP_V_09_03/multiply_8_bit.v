module multiply_8_bit (e1, e2, s);
    input [7:0] e1, e2;
    
    output [15:0] s; 

    assign s = e1 * e2;

endmodule