// Verilog test fixture created from schematic C:\Users\ericj\Documents\EE 118\lab2\Reduced_Z\Reduced_Z.sch - Thu Sep 12 10:53:36 2019

`timescale 1ns / 1ps

module Reduced_Z_Reduced_Z_sch_tb();

// Inputs
   reg A;
   reg B;
   reg C;

// Output
   wire X;

// Bidirs

// Instantiate the UUT
   Reduced_Z UUT (
		.A(A), 
		.B(B), 
		.C(C), 
		.X(X)
   );
// Initialize Inputs

       initial begin
		B = 0;
		C = 0;
    
	#5 B=0; C=1;
	#5 B=1; C=0;
	#5 B=1; C=1;
    #5 $finish ;
    end
endmodule
