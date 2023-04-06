module add_1_bit (e1, e2, r0, s, r1);
    input e1;
    input e2;
    input r0;
    output s;
    output r1;


    assign r1 = (e1 & e2) | (e1 & r0) | (e2 & r0);
    assign s = e1 ^ e2 ^ r0;

endmodule


//module reg_lin(X, s):



//end module