`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg x;
	reg y;
	reg r;
	// Outputs
	wire z;
	wire r1;
	// Instantiate the Unit Under Test (UUT)
	add_1_bit uut (
		x, 
		y,
		r,
		z,
		r1
	);
 
	initial begin
	$dumpfile("add_1_bit_test.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		x = 0;
		y = 0;
		r = 0;
 
	#20 y = 1;
	#20 x = 1;
	#20 y = 0;
	#20 r = 1;	
	#20 y = 1;
	#20 x = 0;
	#20 y = 0;  
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d r0=%d x=%d,y=%d, \tz=%d, r1=%d \n",$time,r,x,y,z,r1, );
		 end
 
endmodule
 
 
