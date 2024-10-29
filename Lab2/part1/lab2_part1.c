//*****************************************************************************
//*****************************    C Source Code    ***************************
//*****************************************************************************
//
//  DESIGNER NAME: 
//
//       LAB NAME:  Lab 2, part 1
//
//      FILE NAME:  lab2_part1.c
//
//-----------------------------------------------------------------------------
//
// DESCRIPTION:
//    This code provides ... <== FINISH ADDING DESCRIPTION OF WHAT THE CODE DOES
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
// Add #define here


//-----------------------------------------------------------
// Define global variable and structures here.
// NOTE: when possible avoid using global variables
//-----------------------------------------------------------
// Add global variable here

// Defines a structure to hold different data types
typedef struct 
{
  unsigned  long  int LA;
  signed    long  int LB;
  unsigned short  int SA[2];
  signed   short  int SB[2];
  unsigned        int IA[2];
  signed          int IB[2];
  unsigned       char CA[4];
  signed         char CB[4];
} test_struct;

// Define a union to hold values in different formats
typedef union 
{
  unsigned  long  int LA;
  signed    long  int LB;
  unsigned short  int SA[2];
  signed   short  int SB[2];
  unsigned        int IA;
  signed          int IB;
  unsigned       char CA[4];
  signed         char CB[4];
} union_32;

test_struct g_struct_var;
union_32    g_union_var;

int main(void)
{
  g_union_var.LA = 0x1234ABCD;

  printf("\e[1;1H\e[2J \n");
  printf("CPT210 Raspberry Pi C Data Type Tester\n");
  printf("--------------------------------------------------------\n");
  printf(" unsigned  long  int = 0x%lx bytes\n", sizeof(g_struct_var.LA));
  printf("   signed  long  int = 0x%lx bytes\n", sizeof(g_struct_var.LB));
  printf(" unsigned        int = 0x%lx bytes\n", sizeof(g_struct_var.IA[0])); 
  printf("   signed        int = 0x%lx bytes\n", sizeof(g_struct_var.IB[0])); 
  printf(" unsigned short  int = 0x%lx bytes\n", sizeof(g_struct_var.SA[0])); 
  printf("   signed short  int = 0x%lx bytes\n", sizeof(g_struct_var.SB[0])); 
  printf(" unsigned       char = 0x%lx bytes\n", sizeof(g_struct_var.CA[0])); 
  printf("   signed       char = 0x%lx bytes\n", sizeof(g_struct_var.CB[0])); 
  
  printf("\n");
  printf(" The structure = 0x%x bytes\n", sizeof(g_struct_var));
  printf("     The union = 0x%x bytes\n", sizeof(g_union_var));
  printf("\n");

  printf("Dumping data values from Union\n");
  printf("--------------------------------------------------------\n");
  printf("  union unsigned  long    int LA    = 0x%lX\n", g_union_var.LA);
  printf("  union   signed  long    int LB    = 0x%lX\n", g_union_var.LB);  
  printf("\n");

  printf("  union unsigned short    int SA[0] = 0x%X\n", g_union_var.SA[0]);
  printf("  union   signed short    int SB[0] = 0x%X\n", g_union_var.SB[0]);
  printf("  union unsigned short    int SA[1] = 0x%X\n", g_union_var.SA[1]);
  printf("  union   signed short    int SB[1] = 0x%X\n", g_union_var.SB[1]);
  printf("\n");

  printf("  union unsigned          int IA    = 0x%X\n", g_union_var.IA);
  printf("  union   signed          int IB    = 0x%X\n", g_union_var.IB);
  printf("\n");

  printf("  union unsigned         char CA[0] = 0x%X\n", g_union_var.CA[0]);
  printf("  union unsigned         char CA[1] = 0x%X\n", g_union_var.CA[1]);
  printf("  union unsigned         char CA[2] = 0x%X\n", g_union_var.CA[2]);
  printf("  union unsigned         char CA[3] = 0x%X\n", g_union_var.CA[3]);
  printf("\n");

  printf("  union   signed         char CB[0] = 0x%X\n", g_union_var.CB[0]);
  printf("  union   signed         char CB[1] = 0x%X\n", g_union_var.CB[1]);
  printf("  union   signed         char CB[2] = 0x%X\n", g_union_var.CB[2]);
  printf("  union   signed         char CB[3] = 0x%X\n", g_union_var.CB[3]);
  printf("\n");

  printf(" *** PROGRAM TERMINATED ***\n");  

} /* main */
