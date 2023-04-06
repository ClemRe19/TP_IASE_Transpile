`timescale 1ns / 1ps
module stimulus;
	// Input
	reg signed [15:0] X1;

	// Output
  	wire signed [31:0] y;
  
	// Instantiate the Unit Under Test (UUT)
	linear_regression uut (
		X1,
		y
	);
	
	initial begin
		$dumpfile("linear_reg_test.vcd");
		$dumpvars(0,stimulus);
			// Initialize Input
			X1 = 0;

		#10 X1 = 1000;
		#10 X1 = -500;
		#10 X1 = -10000;
		#10 ; 
	end

		initial begin
			$monitor("t=%3d X1=%d \ty=%d \n", $time,X1,y);
		end
  
endmodule