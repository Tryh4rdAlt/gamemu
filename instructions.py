import sys

def adc_a_r8(a,r8,carry_flag):
  result = a + r8 + flag
  zflag = (result & 0xFF) == 0
  cflag = result > 0xFF
  nflag = False
  hflag = ((a & 0xF) + (r8 & 0xF) + carry_flag) > 0xF
  return a,zflag,cflag,nflag,hflag
