//*****************************************************************************
//*****************************    C Source Code    ***************************
//*****************************************************************************
//
//  DESIGNER NAME:  
//
//       LAB NAME:  Lab 2, part 4
//
//      FILE NAME:  lab2_part4.c
//
//-----------------------------------------------------------------------------
//
// DESCRIPTION:
//    This code is intended to run on the Raspberry Pi single board computer
//    provides a test vehicle to understand the bitwise manipulation
//    using C programming language.
//
//*****************************************************************************
//*****************************************************************************

//-----------------------------------------------------------
// Required system include file for design
//-----------------------------------------------------------
#include <stdio.h>


//-----------------------------------------------------------
// Required user support files below
//-----------------------------------------------------------
// Add user include files here


//-----------------------------------------------------------
// Define symbolic constants used by program
//-----------------------------------------------------------
#define PIE_BIT_MASK        0x0001
#define RD_BIT_MASK			0x0004	
#define CRS_BIT_MASK        0x0070
#define MD_BIT_MASK			0x0008
#define MODE10_BIT_MASK		0x0100
#define MODE11_BIT_MASK		0x0180
#define PRS_BIT_MASK		0x0E00
#define A0_BIT_MASK			0x1000
#define A1_BIT_MASK			0x2000
#define A2_BIT_MASK			0x4000
#define A3_BIT_MASK			0x8000

//-----------------------------------------------------------
// Define global variable and structures here.
// NOTE: when possible avoid using global variables
//-----------------------------------------------------------

// this is simulated external peripheral register
unsigned int test_reg32 = 0x00000000;

int main(void)
{
  // create variable to hold reg value
  unsigned int reg_value;

  printf("\e[1;1H\e[2J \n");      // clear screen and home cursor

  printf("\n");
  printf("CPT210 Raspberry Pi C Bitwise Test Program (Part4)\n");
  printf("---------------------------------------------------\n");

  // Display the size of the test register
  printf("The size of the test reg is 0x%X bytes\n", (int)sizeof(test_reg32));

  // Display the value of the test register
  printf("The starting value of test reg is 0x%08X\n", test_reg32);
  printf("\n");

  // *********************************************************************
  // PROBLEM 1: Set the PIE bit in test register (test_reg32)
  // *********************************************************************
  printf("PROBLEM 1: Setting PIE bit\n");

  reg_value = test_reg32;
  reg_value |= PIE_BIT_MASK;
  test_reg32 = reg_value;

  printf("    --> Test reg = 0x%08X\n", test_reg32);
  printf("\n");

  // *********************************************************************
  // PROBLEM 2: Set the RD bit in test register
  // *********************************************************************
  printf("PROBLEM 2: Setting RD bit\n");

  reg_value = test_reg32;
  reg_value |= RD_BIT_MASK;
  test_reg32 = reg_value;

  printf("    --> Test reg = 0x%08X\n", test_reg32);
  printf("\n");

  // *********************************************************************
  // PROBLEM 3: Set the CRS bits in test register
  // *********************************************************************
  printf("PROBLEM 3: Setting CRS bits\n");

  reg_value = test_reg32;
  reg_value |= CRS_BIT_MASK;
  test_reg32 = reg_value;

  printf("    --> Test reg = 0x%08X\n", test_reg32);
  printf("\n");

  // *********************************************************************
  // PROBLEM 4: Set the A[3:0] bits in test register
  // *********************************************************************
  printf("PROBLEM 4: Setting A[3:0] bits\n");

  reg_value = test_reg32;
  reg_value |= (A3_BIT_MASK | A2_BIT_MASK | A1_BIT_MASK | A0_BIT_MASK);
  test_reg32 = reg_value;

  printf("    --> Test reg = 0x%08X\n", test_reg32);
  printf("\n");

  // *********************************************************************
  // PROBLEM 5: Use an IF statement to test it A2 is set
  //            if A2 = 1 then 
  //                print "Bit A2 is 1"
  //            else 
  //                print "The bit A2 is 0"
  // *********************************************************************
  printf("PROBLEM 5: Testing bit A2\n");

  reg_value = test_reg32;
  if ((reg_value & A2_BIT_MASK) == A2_BIT_MASK)
  {
	  printf("    --> Bit A2 is 1");
  } else
  {
	  printf("    --> Bit A2 is 0");
  }
  test_reg32 = reg_value;
  
  printf("\n");
  printf("\n");

  // *********************************************************************
  // PROBLEM 6: Clear A2 bit in test register
  // *********************************************************************
  printf("PROBLEM 6: Clearing A[2] bit\n");
  
  reg_value = test_reg32;
  reg_value &= ~A2_BIT_MASK;
  test_reg32 = reg_value;

  printf("    --> Test reg = 0x%08X\n", test_reg32);
  printf("\n");

  // *********************************************************************
  // PROBLEM 7: Clear CRS bits and set PRS bits in test register
  // *********************************************************************
  printf("PROBLEM 7: Clear CRS bits and set PRS bits\n");
  
  reg_value = test_reg32;
  reg_value &= ~CRS_BIT_MASK;
  reg_value |= PRS_BIT_MASK;
  test_reg32 = reg_value;

  printf("    --> Test reg = 0x%08X\n", test_reg32);
  printf("\n");

  // *********************************************************************
  // PROBLEM 8: Use an IF statement to test if A2 is set
  //            if A2 = 1 then
  //                print "Bit A2=1 so clearing it"
  //                modify the reg to clear the bit
  //            else
  //                print "Bit A2=0 so setting it"
  //                modify the reg to set the bit
  // *********************************************************************
  printf("PROBLEM 8: Testing bit A2\n");

  reg_value = test_reg32;
  if ((reg_value & A2_BIT_MASK) == A2_BIT_MASK)
  {
     printf("    --> Bit A2=1 so clearing it\n");
     reg_value &= ~A2_BIT_MASK;
  } else 
  {
	 printf("    --> Bit A2=0 so setting it\n");
	 reg_value |= A2_BIT_MASK;
  }
  test_reg32 = reg_value;
  
  printf("    --> Test reg = 0x%08X\n", test_reg32);
  printf("\n");

  // *********************************************************************
  // PROBLEM 9: Use an IF statement to test it MD is 0
  //            if MD = 0 then
  //                print "Bit MD=0, setting mode=10"
  //                set MODE to 10
  //            else
  //                print "Bit MD=1, setting mode=11"
  //                set MODE to 11
  // *********************************************************************
  printf("PROBLEM 9: Testing bit MD & setting mode bits\n");

  reg_value = test_reg32;
  if ((reg_value & MD_BIT_MASK) != MD_BIT_MASK)
  {
     printf("    --> Bit MD=0, setting mode=10\n");
     reg_value |= MODE10_BIT_MASK;
  } else 
  {
	 printf("    --> Bit MD=1, setting mode=11\n");
	 reg_value |= MODE11_BIT_MASK;
  }
  test_reg32 = reg_value;

  printf("    --> Test reg = 0x%08X\n", test_reg32);
  printf("\n");

  // *********************************************************************
  // PROBLEM 10: Clear all bits in test register
  // *********************************************************************
  printf("PROBLEM 10: Clearing all bits\n");

  reg_value = test_reg32;
  reg_value &= ~reg_value;
  test_reg32 = reg_value;

  printf("    --> Test reg = 0x%08X\n", test_reg32);
  printf("\n");

  printf(" *** PROGRAM TERMINATED ***\n");

} /* main */

