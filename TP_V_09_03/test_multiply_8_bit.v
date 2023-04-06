`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg [7:0] x;
	reg [7:0] y;
	// Outputs
	wire [15:0] z;
	// Instantiate the Unit Under Test (UUT)
	multiply_8_bit uut (
		x, 
		y,
		z
	);
 
	initial begin
	$dumpfile("multiply_8_bit_test.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		x = 10;
		y = 2;
 
	#20 y = 4;
	#20 x = 20;
	#20 y = 5; 
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d x=%d,y=%d,\tz=%d, \n",$time,x,y,z, );
		 end
 
endmodule
 
 
