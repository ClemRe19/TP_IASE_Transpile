`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg w;
	reg x;
	reg y;
	// Outputs
	wire z;
	// Instantiate the Unit Under Test (UUT)
	and_gate3 uut (
		w,
		x, 
		y, 
		z
	);
 
	initial begin
	$dumpfile("and_test3.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		w = 0;
		x = 0;
		y = 0;
 
	#20 y = 1;
	#20 x = 1;
	#20 y = 0;
	#20 w = 1;	
	#20 y = 1;
	#20 x = 0;
	#20 y = 0;	  
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d w=%d x=%d,y=%d,z=%d \n",$time,w,x,y,z, );
		 end
 
endmodule
 
 
