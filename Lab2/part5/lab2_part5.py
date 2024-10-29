#*****************************************************************************
#***************************** Python Source Code  ***************************
#*****************************************************************************
#
#  DESIGNER NAME:  
#
#      FILE NAME:  lab2_part5.c
#
#-----------------------------------------------------------------------------
#
# DESCRIPTION:
#   This code is intended to run on the Raspberry Pi single board computer
#   provides a test vehicle to understand the bitwise manipulation
#   using Python programming language.
#
#*****************************************************************************
#*****************************************************************************

# this is simulated external peripheral register
test_reg32 = 0x00000000

def main():
  global test_reg32
  
  # Constants
  PIE_BIT_MASK		= 0x0001
  RD_BIT_MASK			= 0x0004
  CRS_BIT_MASK		= 0x0070
  MD_BIT_MASK			= 0x0008
  MODE10_BIT_MASK		= 0x0100
  MODE11_BIT_MASK		= 0x0180
  PRS_BIT_MASK		= 0x0E00
  A0_BIT_MASK			= 0x1000
  A1_BIT_MASK			= 0x2000
  A2_BIT_MASK			= 0x4000
  A3_BIT_MASK			= 0x8000

  # create variable to hold reg value
  reg_value = 0x00000000

  print(f"\e[1;1H\e[2J ")      # clear screen and home cursor

  print()
  print(f"CPT210 Raspberry Pi Python Bitwise Test Program Part5)")
  print(f"---------------------------------------------------")

  # Display the value of the test register
  print(f"The starting value of test reg is 0x{test_reg32:08X}")
  print()

  # *********************************************************************
  # PROBLEM 1: Set the PIE bit in test register (test_reg32)
  # *********************************************************************
  print(f"PROBLEM 1: Setting PIE bit")

  reg_value = test_reg32
  reg_value |= PIE_BIT_MASK
  test_reg32 = reg_value

  print(f"    --> Test reg = 0x{test_reg32:08X}")
  print()

  # *********************************************************************
  # PROBLEM 2: Set the RD bit in test register (test_reg32)
  # *********************************************************************
  print(f"PROBLEM 2: Setting RD bit")

  reg_value = test_reg32
  reg_value |= RD_BIT_MASK
  test_reg32 = reg_value

  print(f"    --> Test reg = 0x{test_reg32:08X}")
  print()

  # *********************************************************************
  # PROBLEM 3: Set the CRS bits in test register
  # *********************************************************************
  print(f"PROBLEM 3: Setting CRS bits")

  reg_value = test_reg32
  reg_value |= CRS_BIT_MASK
  test_reg32 = reg_value

  print(f"    --> Test reg = 0x{test_reg32:08X}")
  print()

  # *********************************************************************
  # PROBLEM 4: Set the A[3:0] bits in test register
  # *********************************************************************
  print(f"PROBLEM 4: Setting A[3:0] bits")

  reg_value = test_reg32
  reg_value |= (A3_BIT_MASK | A2_BIT_MASK | A1_BIT_MASK | A0_BIT_MASK)
  test_reg32 = reg_value

  print(f"    --> Test reg = 0x{test_reg32:08X}")
  print()

  # *********************************************************************
  # PROBLEM 5: Use an IF statement to test it A2 is set
  #            if A2 = 1 then 
  #                print "Bit A2 is 1"
  #            else 
  #                print "The bit A2 is 0"
  # *********************************************************************
  print(f"PROBLEM 5: Testing bit A2")

  reg_value = test_reg32
  if (reg_value & A2_BIT_MASK) == A2_BIT_MASK:
    print("    --> Bit A2 is 1")
  else:
    print("    --> Bit A2 is 0")
  test_reg32 = reg_value

  print()

  # *********************************************************************
  # PROBLEM 6: Clear A2 bit in test register
  # *********************************************************************
  print(f"PROBLEM 6: Clearing A[2] bit")

  reg_value = test_reg32
  reg_value &= ~A2_BIT_MASK
  test_reg32 = reg_value

  print(f"    --> Test reg = 0x{test_reg32:08X}")
  print()

  # *********************************************************************
  # PROBLEM 7: Clear CRS bits and set PRS bits in test register
  # *********************************************************************
  print(f"PROBLEM 7: Clear CRS bits and set PRS bits")

  reg_value = test_reg32
  reg_value &= ~CRS_BIT_MASK
  reg_value |= PRS_BIT_MASK
  test_reg32 = reg_value

  print(f"    --> Test reg = 0x{test_reg32:08X}")
  print()

  # *********************************************************************
  # PROBLEM 8: Use an IF statement to test if A2 is set
  #            if A2 = 1 then
  #                print "Bit A2=1 so clearing it"
  #                modify the reg to clear the bit
  #            else
  #                print "Bit A2=0 so setting it"
  #                modify the reg to set the bit
  # *********************************************************************
  print(f"PROBLEM 8: Testing bit A2")

  reg_value = test_reg32;
  if (reg_value & A2_BIT_MASK) == A2_BIT_MASK:
    print("    --> Bit A2=1 so clearing it")
    reg_value &= ~A2_BIT_MASK
  else:
    print("    --> Bit A2=0 so setting it")
    reg_value |= A2_BIT_MASK
  test_reg32 = reg_value;

  print(f"    --> Test reg = 0x{test_reg32:08X}")
  print()

  # *********************************************************************
  # PROBLEM 9: Use an IF statement to test it MD is 0
  #            if MD = 0 then
  #                print "Bit MD=0, setting mode=10"
  #                set MODE to 10
  #            else
  #                print "Bit MD=1, setting mode=11"
  #                set MODE to 11
  # *********************************************************************
  print(f"PROBLEM 9: Testing bit MD & setting mode bits")

  reg_value = test_reg32;
  if (reg_value & MD_BIT_MASK) != MD_BIT_MASK:
    print("    --> Bit MD=0, setting mode=10")
    reg_value |= MODE10_BIT_MASK
  else:
    print("    --> Bit MD=1, setting mode=11")
    reg_value |= MODE11_BIT_MASK
  test_reg32 = reg_value;

  print(f"    --> Test reg = 0x{test_reg32:08X}")
  print()

  # *********************************************************************
  # PROBLEM 10: Clear all bits in test register
  # *********************************************************************
  print(f"PROBLEM 10: Clearing all bits")

  reg_value = test_reg32
  reg_value &= ~reg_value
  test_reg32 = reg_value

  print(f"    --> Test reg = 0x{test_reg32:08X}")
  print()

  print(f" *** PROGRAM TERMINATED ***")

# if file execute standalone then call the main function.
if __name__ == '__main__':
  main()