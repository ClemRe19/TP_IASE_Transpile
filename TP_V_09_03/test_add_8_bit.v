`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg [7:0] x;
	reg [7:0] y;
	// Outputs
	wire [7:0] z;
	// Instantiate the Unit Under Test (UUT)
	add_8_bit uut (
		x, 
		y,
		z
	);
 
	initial begin
	$dumpfile("add_8_bit_test.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		x = 00000001;
		y = 00000010;
 
	#20 y = 10;
	#20 x = 35;
	#20 y = 0; 
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d x=%d,y=%d,\tz=%d, \n",$time,x,y,z, );
		 end
 
endmodule
 
 
